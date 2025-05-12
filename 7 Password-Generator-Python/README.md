# 🔐 Password Generator 

A customizable and secure password generator built using Python. It allows users to define password length and choose whether to include digits and special characters.

---

## 🚀 Features

* User-defined password length
* Option to include:

  * Numbers (`0-9`)
  * Special characters (`!@#$%^&*...`)
* Ensures password strength:

  * At least one lowercase letter
  * At least one uppercase letter
  * At least one digit (if enabled)
  * At least one symbol (if enabled)

---

## 📌 Sample Usage

```
Enter the length of password: 12  
Include numbers? (y/n): y  
Include special characters? (y/n): y  

Generated Password: k7Y$eT#bV9pL
```

---

## 🧠 Concepts Used

* `random.choice()` for random character selection
* `string` module for letters, digits, and punctuation
* `any()` for validation checks
* Loops and conditionals

---

## ▶️ How to Run

1. Save the script as `password_generator.py`
2. Run using Python:

```bash
python password_generator.py
```

3. Follow the prompts in the terminal

---

## 👩‍💻 Author

**Tayyeba Ali** — Building tools to make security simple and effective. 😊

---

Stay secure with strong passwords! 🔒
