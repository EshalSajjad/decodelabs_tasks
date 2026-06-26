# ── Phase 2: Caesar cipher + Vigenère cipher ─────────────────────────────────


# ─── Caesar ──────────────────────────────────────────────────────────────────

def caesar_encrypt(text: str, shift: int) -> str:
    """Shift each letter by `shift` positions; preserve case, spaces, symbols."""
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)  # spaces, digits, punctuation unchanged
    return "".join(result)


def caesar_decrypt(text: str, shift: int) -> str:
    return caesar_encrypt(text, -shift)


# ─── Vigenère ────────────────────────────────────────────────────────────────

def _clean_key(key: str) -> str:
    """Strip non-alpha characters from the key and uppercase it."""
    return "".join(ch.upper() for ch in key if ch.isalpha())


def vigenere_encrypt(text: str, key: str) -> str:
    """
    Encrypt using the Vigenère cipher.
    Key cycles only over alphabetic characters in the text.
    """
    key = _clean_key(key)
    if not key:
        raise ValueError("Key must contain at least one letter.")

    result = []
    key_index = 0
    for ch in text:
        if ch.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
            key_index += 1
        else:
            result.append(ch)
    return "".join(result)


def vigenere_decrypt(text: str, key: str) -> str:
    key = _clean_key(key)
    if not key:
        raise ValueError("Key must contain at least one letter.")

    result = []
    key_index = 0
    for ch in text:
        if ch.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base - shift) % 26 + base))
            key_index += 1
        else:
            result.append(ch)
    return "".join(result)


# ── Menu helpers ──────────────────────────────────────────────────────────────

def get_caesar_shift() -> int:
    while True:
        raw = input("  Shift (1–25): ").strip()
        if raw.lstrip('-').isdigit():
            shift = int(raw) % 26
            return shift
        print("  Please enter an integer.")


def get_vigenere_key() -> str:
    while True:
        key = input("  Keyword (letters only): ").strip()
        cleaned = _clean_key(key)
        if cleaned:
            return key
        print("  Key must contain at least one letter.")


def run_caesar(mode: str) -> None:
    text = input("  Text: ")
    shift = get_caesar_shift()
    if mode == "encrypt":
        print(f"\n  Ciphertext : {caesar_encrypt(text, shift)}")
    else:
        print(f"\n  Plaintext  : {caesar_decrypt(text, shift)}")


def run_vigenere(mode: str) -> None:
    text = input("  Text: ")
    key = get_vigenere_key()
    if mode == "encrypt":
        print(f"\n  Ciphertext : {vigenere_encrypt(text, key)}")
    else:
        print(f"\n  Plaintext  : {vigenere_decrypt(text, key)}")


# ── Entry point ───────────────────────────────────────────────────────────────

CIPHERS = {
    "1": ("Caesar cipher",   run_caesar),
    "2": ("Vigenère cipher", run_vigenere),
}

def main():
    print("=== Encryption / Decryption Tool ===")

    while True:
        print("\nCiphers:")
        for key, (name, _) in CIPHERS.items():
            print(f"  {key}. {name}")
        print("  q. Quit")

        choice = input("\nChoose a cipher: ").strip().lower()
        if choice == "q":
            print("Goodbye.")
            break
        if choice not in CIPHERS:
            print("  Invalid choice.")
            continue

        cipher_name, cipher_fn = CIPHERS[choice]
        print(f"\n── {cipher_name} ──")
        print("  1. Encrypt")
        print("  2. Decrypt")
        mode_choice = input("  Choose: ").strip()

        if mode_choice == "1":
            cipher_fn("encrypt")
        elif mode_choice == "2":
            cipher_fn("decrypt")
        else:
            print("  Invalid choice.")
            continue

        print()


if __name__ == "__main__":
    main()
