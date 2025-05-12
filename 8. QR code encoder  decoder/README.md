# 🔗 QR Code Generator for LinkedIn Profile

This is a simple Python script that generates a **QR code** for a LinkedIn profile using the `qrcode` library.

---

## 📌 What It Does

The script:

* Takes your LinkedIn profile link
* Creates a QR code image
* Saves the image as a PNG file on your system

---

## 📁 File

* `myqrcode.png`: The generated QR code image
* Python script to generate it (see below)

---

## 💻 Python Script

```python
import qrcode

linkdin_acount_link = "https://www.linkedin.com/in/tayyeba-ali-71a66029a/"

img = qrcode.make(linkdin_acount_link)

img.save('E:/Giaic/QUATER 3/class assigment/QrCode/myqrcode.png')
```

---

## ⚙️ Requirements

Install the `qrcode` library:

```bash
pip install qrcode[pil]
```

---

## 🧠 Tips

* You can scan the QR code with your mobile device to quickly access the LinkedIn profile.
* Customize the file path as per your own folder structure.

---

## 👩‍💻 Author

**Tayyeba Ali** — Sharing and building smart tools with Python. 😊

---

Happy coding and networking! 🤝
