# 🔐Password Strength Checker

A command-line password strength analyzer built in Python that evaluates passwords based on multiple security criteria and provides actionable improvement suggestions.

---

## 📌Description

This project checks the strength of a password by analyzing it against 5 security criteria — length, uppercase, lowercase, numbers and special characters. It gives a score out of 5, rates the password as Strong, Moderate or Weak, and provides specific suggestions to improve it. Built as part of a Python internship project to practice string manipulation and regular expressions.

---

## ✨Features

- Checks 5 security criteria
- Scores password out of 5
- Rates as Strong / Moderate / Weak
- Provides specific improvement suggestions
- Uses `re` (regex) module for pattern matching
- Continuous checking until user exits

---

## 🛠️Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| re (regex) | Pattern matching |
| Functions | Modular design |

---

## 📁Project Structure

```
password-strength-checker/
├── password_checker.py    # Main script
└── README.md              # Project documentation
```

---

## 🚀How to Run

```bash
git clone https://github.com/gunn0067/password-strength-checker.git
cd password-strength-checker
python password_checker.py
```

---

## 📊Sample Output

```
========================================
      PASSWORD STRENGTH CHECKER
========================================

Enter a password to check: hello
----------------------------------------
Result: WEAK PASSWORD
Score: 1/5

Suggestions:
  - Password must be at least 8 characters long.
  - Add at least 1 uppercase letter.
  - Add at least 1 number.
  - Add at least 1 special character (!@#$%^&* etc.)
----------------------------------------

Enter a password to check: Hello@123
----------------------------------------
Result: STRONG PASSWORD
Your password meets all requirements!
Score: 5/5
----------------------------------------
```

---

## 📚Learnings

- Regular expressions with `re` module
- String analysis and pattern matching
- Scoring logic and conditional feedback
- Building security-focused CLI tools

---

## 👤Author

**Gunn Fulwani**
B.Tech CS — Symbiosis Institute of Technology, Nagpur
📧 fulwanigunn06@gmail.com
🔗 [LinkedIn](https://www.linkedin.com/in/gunn-fulwani-b9350631a/) | [GitHub](https://github.com/gunn0067)
