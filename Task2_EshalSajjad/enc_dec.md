## 🔑 Phase 2 — Cipher Tool (`cipher_tool.py`)
 
### What it does
 
Encrypt or decrypt text using two classical substitution ciphers:
 
**Caesar cipher** — shifts every letter by a fixed number of positions.
`"Hello" + shift 3 → "Khoor"`
 
**Vigenère cipher** — uses a keyword to apply a different shift to each letter, making it much harder to break than Caesar.
`"Hello" + key "KEY" → "Rijvs"`
 
Both ciphers:
- Preserve uppercase/lowercase
- Leave spaces, digits, and punctuation unchanged
- The key cycles only over alphabetic characters
### Running it
 
```bash
python cipher_tool.py
```
 
**Example session:**
 
```
=== Encryption / Decryption Tool ===
 
Ciphers:
  1. Caesar cipher
  2. Vigenère cipher
  q. Quit
 
Choose a cipher: 1
 
── Caesar cipher ──
  1. Encrypt
  2. Decrypt
  Choose: 1
  Text: Hello World
  Shift (1–25): 13
 
  Ciphertext : Uryyb Jbeyq
```
 
### Key concepts
 
- **Caesar cipher** — `(ord(ch) - base + shift) % 26` wraps the alphabet
- **Vigenère cipher** — key index advances only for alphabetic characters, leaving punctuation and spaces in place
- **Modular arithmetic** — both encrypt and decrypt use `% 26` to stay within the alphabet
---
 
## ▶️ Requirements
 
- Python 3.8+
- No third-party libraries — standard library only (`string` module)
---
 
## 💡 Tips & Extensions
 
- **Password checker:** add a common-password blocklist (e.g. `rockyou.txt`) to catch `Password1!`-style entries
- **Cipher tool:** try implementing a brute-force Caesar cracker (only 25 possibilities!) or a frequency-analysis attack on Vigenère
- **Combine them:** encrypt a strong password hint and store the ciphertext — decrypt only when needed