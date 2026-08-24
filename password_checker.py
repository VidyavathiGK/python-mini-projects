import re


def check_password_strength(password):
  score = 0
  feedback = []

  # Length check
  if len(password) >= 8:
    score += 1
  else:
    feedback.append("Password should be at least 8 characters long.")

  # Uppercase check
  if re.search(r"[A-Z]", password):
    score += 1
  else:
    feedback.append("Add at least one uppercase letter.")

  # Lowercase check
  if re.search(r"[a-z]", password):
    score += 1
  else:
    feedback.append("Add at least one lowercase letter.")

  # Digit check
  if re.search(r"\d", password):
    score += 1
  else:
    feedback.append("Add at least one number.")

  # Special character check
  if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1
  else:
    feedback.append("Add at least one special character.")

  # Rating evaluation
  print(f"\n--- Password Strength Evaluation ---")
  if score == 5:
    print("Rating: Strong 💪")
  elif score >= 3:
    print("Rating: Moderate ⚠️")
  else:
    print("Rating: Weak ❌")

  if feedback:
    print("\nSuggestions to improve:")
    for item in feedback:
      print(f"- {item}")


if __name__ == "__main__":
  print("--- Python Password Strength Checker ---")
  pwd = input("Enter a password to test: ")
  check_password_strength(pwd)
