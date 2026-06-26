import string

# ── Phase 1: Core strength analysis ─────────────────────────────────────────

def check_password(password: str) -> dict:
    """
    Evaluate password strength and return a result dict:
      {
        "strength": "Weak" | "Medium" | "Strong",
        "score": int,
        "feedback": [list of improvement hints],
        "passed_minimum": bool,
      }
    Score accumulates points; future phases can add more checks here.
    """
    feedback = []
    score = 0
    passed_minimum = True

    # Hard minimum: under 8 chars fails immediately
    if len(password) < 8:
        return {
            "strength": "Weak",
            "score": 0,
            "feedback": ["Password must be at least 8 characters long."],
            "passed_minimum": False,
        }

    # Length bonuses
    if len(password) >= 16:
        score += 3
    elif len(password) >= 12:
        score += 2
    else:
        score += 1
        feedback.append("Use 12+ characters for a stronger password.")

    # Character-type checks
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    if has_upper:
        score += 1
    else:
        feedback.append("Add uppercase letters (A–Z).")

    if has_lower:
        score += 1
    else:
        feedback.append("Add lowercase letters (a–z).")

    if has_digit:
        score += 1
    else:
        feedback.append("Add numbers (0–9).")

    if has_symbol:
        score += 2  # symbols are weighted higher
    else:
        feedback.append("Add symbols (!@#$%^&* …) for a big boost.")

    # Classify
    if score >= 7:
        strength = "Strong"
    elif score >= 4:
        strength = "Medium"
    else:
        strength = "Weak"

    return {
        "strength": strength,
        "score": score,
        "feedback": feedback,
        "passed_minimum": passed_minimum,
    }


def display_result(result: dict) -> None:
    strength_styles = {
        "Weak":   "[ WEAK   ]",
        "Medium": "[ MEDIUM ]",
        "Strong": "[ STRONG ]",
    }
    label = strength_styles.get(result["strength"], result["strength"])
    print(f"\n  Strength : {label}")
    print(f"  Score    : {result['score']}/8")
    if result["feedback"]:
        print("  Tips:")
        for tip in result["feedback"]:
            print(f"    • {tip}")
    print()


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    print("=== Password Strength Checker ===")
    print("Type 'quit' to exit.\n")

    while True:
        password = input("Enter a password to check: ").strip()
        if password.lower() == "quit":
            print("Goodbye.")
            break
        if not password:
            print("  (no input — try again)\n")
            continue

        result = check_password(password)
        display_result(result)


if __name__ == "__main__":
    main()
