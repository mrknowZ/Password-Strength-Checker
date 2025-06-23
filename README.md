
# 🔐 Password Strength Checker (Tkinter GUI)

A beginner-friendly Python desktop application that evaluates the strength of a password in real-time using a graphical user interface built with Tkinter.

---

## 🖥️ Features

✅ Built with **Python** and **Tkinter**  
✅ Real-time password strength analysis  
✅ Visual feedback with color-coded labels  
✅ Password visibility toggle (Show/Hide)  
✅ Progress bar indicating password strength  

---

## 🎯 How It Works

The application checks your password against the following criteria:
- Length (≥ 8 characters)
- Contains lowercase letters
- Contains uppercase letters
- Contains digits (0–9)
- Contains special characters (`@$!%*?&`)

Each condition adds 1 point (out of 5), and a progress bar & label show strength as:
- 🔴 Weak (0–2 points)
- 🟠 Moderate (3 points)
- 🟢 Strong (4–5 points)

---

## 📸 Screenshot

> ![image](https://github.com/user-attachments/assets/d5965d05-d548-46b4-93bc-b2f35ae1224d)


---

## 🛠️ Getting Started

### Requirements
- Python 3.x  
- No additional packages needed (Tkinter is built-in with Python)

### Run the App
```bash
python password_checker.py
