# 🔐 Security Tools Suite
 
A pair of beginner-friendly Python command-line tools covering password security and classical cryptography.
 
---
 
## 📁 Project Structure
 
```
.
├── password_checker.py   # Phase 1 – Password Strength Checker
└── cipher_tool.py        # Phase 2 – Caesar & Vigenère Cipher Tool
```
 
---
 
## 🛡️ Phase 1 — Password Strength Checker (`password_checker.py`)
 
### What it does
 
Analyzes a password and rates it as **Weak**, **Medium**, or **Strong** based on:
 
| Check | Points |
|---|---|
| Length ≥ 16 characters | +3 |
| Length ≥ 12 characters | +2 |
| Length ≥ 8 characters | +1 |
| Contains uppercase letters (A–Z) | +1 |
| Contains lowercase letters (a–z) | +1 |
| Contains digits (0–9) | +1 |
| Contains symbols (!@#$%…) | +2 |
 
**Score thresholds:**
 
| Score | Strength |
|---|---|
| 0–3 | Weak |
| 4–6 | Medium |
| 7–8 | Strong |
 
Passwords under 8 characters fail immediately regardless of other criteria.
 
### Running it
 
```bash
python password_checker.py
```
 
**Example session:**
 
```
=== Password Strength Checker ===
Type 'quit' to exit.
 
Enter a password to check: hunter2
 
  Strength : [ WEAK   ]
  Score    : 0/8
  Tips:
    • Password must be at least 8 characters long.
 
Enter a password to check: MyP@ssw0rd!99
 
  Strength : [ STRONG ]
  Score    : 8/8
```
 
### Key concepts
 
- **String handling** — iterating characters with `.isupper()`, `.isdigit()`, `string.punctuation`
- **Condition checks** — scoring system with branching logic
- **Security basics** — length and character diversity as core password hygiene
---