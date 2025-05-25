from __future__ import print_function


__version__ = "0.0.18"

import itertools
import math
import re
# http://www.python.org/doc/2.4.4/lib/module-operator.html
import operator
import struct
import sys
# http://www.python.org/doc/2.4.4/lib/module-warnings.html
import warnings
import zlib

from array import array
from functools import reduce

# The optional Cython module 'cpngfilters' is not available; pure Python filters will be used.


__all__ = ['Image', 'Reader', 'Writer', 'write_chunks', 'from_array']


# The PNG signature.
# http://www.w3.org/TR/PNG/#5PNG-file-signature
_signature = struct.pack('8B', 137, 80, 78, 71, 13, 10, 26, 10)

_adam7 = ((0, 0, 8, 8),
          (4, 0, 8, 8),
          (0, 4, 4, 8),
          (2, 0, 4, 4),
          (0, 2, 2, 4),
          (1, 0, 2, 2),
          (0, 1, 1, 2))

def group(s, n):
    # See http://www.python.org/doc/2.6/library/functions.html#zip
    return list(zip(*[iter(s)]*n))

def isarray(x):
    return isinstance(x, array)

def tostring(row):
    return row.tobytes()

def interleave_planes(ipixels, apixels, ipsize, apsize):
    """
    Interleave (colour) planes, e.g. RGB + A = RGBA.
    Return an array of pixels consisting of the `ipsize` elements of
    data from each pixel in `ipixels` followed by the `apsize` elements
    of data from each pixel in `apixels`.  Conventionally `ipixels`
    and `apixels` are byte arrays so the sizes are bytes, but it
    actually works with any arrays of the same type.  The returned
    array is the same type as the input arrays which should be the
    same type as each other.
    """

    itotal = len(ipixels)
    atotal = len(apixels)
    newtotal = itotal + atotal
    newpsize = ipsize + apsize
    # Set up the output buffer
    # See http://www.python.org/doc/2.4.4/lib/module-array.html#l2h-1356
    out = array(ipixels.typecode)
    # It's annoying that there is no cheap way to set the array size :-(
    out.extend(ipixels)
    out.extend(apixels)
    # Interleave in the pixel data
    for i in range(ipsize):
        out[i:newtotal:newpsize] = ipixels[i:itotal:ipsize]
    for i in range(apsize):
        out[i+ipsize:newtotal:newpsize] = apixels[i:atotal:apsize]
    return out

def check_palette(palette):
    """Check a palette argument (to the :class:`Writer` class)
    for validity.  Returns the palette as a list if okay; raises an
    exception otherwise.
    """

    # None is the default and is allowed.
    if palette is None:
        return None

    p = list(palette)
    if not (0 < len(p) <= 256):
        raise ValueError("a palette must have between 1 and 256 entries")
    seen_triple = False
    for i,t in enumerate(p):
        if len(t) not in (3,4):
            raise ValueError(
              "palette entry %d: entries must be 3- or 4-tuples." % i)
        if len(t) == 3:
            seen_triple = True
        if seen_triple and len(t) == 4:
            raise ValueError(
              "palette entry %d: all 4-tuples must precede all 3-tuples" % i)
        for x in t:
            if int(x) != x or not(0 <= x <= 255):
                raise ValueError(
                  "palette entry %d: values must be integer: 0 <= x <= 255" % i)
    return p

def check_sizes(size, width, height):
    """Check that these arguments, in supplied, are consistent.
    Return a (width, height) pair.
    """

    if not size:
        return width, height

    if len(size) != 2:
        raise ValueError(
          "size argument should be a pair (width, height)")
    if width is not None and width != size[0]:
        raise ValueError(
          "size[0] (%r) and width (%r) should match when both are used."
            % (size[0], width))
    if height is not None and height != size[1]:
        raise ValueError(
          "size[1] (%r) and height (%r) should match when both are used."
            % (size[1], height))
    return size

def isinteger(x):
    """Check if x is an integer (works for int and long in Python 2, int in Python 3)."""
    return isinstance(x, int)

def check_color(c, greyscale, which):
    """Checks that a colour argument for transparent or
    background options is the right form.  Returns the colour
    (which, if it's a bar integer, is "corrected" to a 1-tuple).
    """

    if c is None:
        return c
    if greyscale:
        try:
            len(c)
        except TypeError:
            c = (c,)
        if len(c) != 1:
            raise ValueError("%s for greyscale must be 1-tuple" %
                which)
        if not isinteger(c[0]):
            raise ValueError(
                "%s colour for greyscale must be integer" % which)
    else:
        if not (len(c) == 3 and
                isinteger(c[0]) and
                isinteger(c[1]) and
                isinteger(c[2])):
            raise ValueError(
                "%s colour must be a triple of integers" % which)
    return c

class Error(Exception):
    def __str__(self):
        return self.__class__.__name__ + ': ' + ' '.join(self.args)

class FormatError(Error):
    """Problem with input file format.  In other words, PNG file does
    not conform to the specification in some way and is invalid.
    """

class ChunkError(FormatError):
    pass
