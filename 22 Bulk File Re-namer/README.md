# 📁 Bulk File Renamer

A simple Python script to rename multiple files in a directory with a new consistent naming pattern.

## 📌 Features

* Renames all files in the specified directory
* Applies a new name pattern like `img0.jpg`, `img1.jpg`, etc.

## 🧠 How It Works

The script loops through all files in a target directory and renames them in sequential order using the format `imgX.jpg`, where `X` is an incrementing number.

## 🖥️ Requirements

* Python 3
* Access to the directory containing the files you want to rename

## 🛠️ Setup & Usage

1. Modify the `path` variable to point to your target directory:

   ```python
   path = "E:/Giaic/QUATER 3/class assigment/Bulk File Re-namer"
   ```
2. Run the script:

   ```bash
   python bulk_renamer.py
   ```
3. All files in the specified folder will be renamed to the format `img0.jpg`, `img1.jpg`, and so on.

## ⚠️ Note

* Ensure you back up your files before running the script.
* The script will rename **all** files in the specified folder regardless of type.

## 📄 Example

Before:

```
photoA.png
photoB.png
screenshot123.jpg
```

After:

```
img0.jpg
img1.jpg
img2.jpg
```

## 🧑‍💻 Author

Tayyeba Ali

---
