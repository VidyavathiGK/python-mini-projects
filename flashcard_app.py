import json
import os
import random


class Flashcard:

  def __init__(self, question, answer):
    self.question = question
    self.answer = answer


class FlashcardDeck:

  def __init__(self, filename="flashcards.json"):
    self.filename = filename
    self.cards = self.load_cards()

  def load_cards(self):
    if os.path.exists(self.filename):
      try:
        with open(self.filename, "r") as file:
          data = json.load(file)
          return [Flashcard(item["question"], item["answer"]) for item in data]
      except json.JSONDecodeError:
        return []
    return []

  def save_cards(self):
    data = [{"question": card.question, "answer": card.answer} for card in self.cards]
    with open(self.filename, "w") as file:
      json.dump(data, file, indent=4)

  def add_card(self, question, answer):
    self.cards.append(Flashcard(question, answer))
    self.save_cards()
    print("✨ Flashcard added successfully!")

  def view_cards(self):
    if not self.cards:
      print("📭 No flashcards available.")
      return
    print("\n--- All Flashcards ---")
    for index, card in enumerate(self.cards, 1):
      print(f"{index}. Q: {card.question} | A: {card.answer}")

  def delete_card(self, index):
    if 0 <= index < len(self.cards):
      removed = self.cards.pop(index)
      self.save_cards()
      print(f"🗑️ Deleted card: '{removed.question}'")
    else:
      print("❌ Invalid card number.")

  def study_session(self):
    if not self.cards:
      print("📭 No flashcards to study. Add some first!")
      return

    print("\n--- Starting Study Session ---")
    print("Type your answer, or type 'quit' to exit session.")
    
    score = 0
    shuffled_cards = self.cards.copy()
    random.shuffle(shuffled_cards)

    for card in shuffled_cards:
      user_ans = input(f"\nQ: {card.question}\nYour Answer: ").strip()
      if user_ans.lower() == 'quit':
        break
      
      if user_ans.lower() == card.answer.lower():
        print("✅ Correct!")
        score += 1
      else:
        print(f"❌ Incorrect. The correct answer was: {card.answer}")

    print(f"\n🎉 Session finished! Your score: {score}/{len(shuffled_cards)}")


def main():
  deck = FlashcardDeck()

  while True:
    print("\n=== Flashcard Study App ===")
    print("1. View All Flashcards")
    print("2. Add New Flashcard")
    print("3. Delete a Flashcard")
    print("4. Start Study Quiz")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == '1':
      deck.view_cards()
    elif choice == '2':
      q = input("Enter the question: ").strip()
      a = input("Enter the answer: ").strip()
      if q and a:
        deck.add_card(q, a)
      else:
        print("❌ Question and answer cannot be empty.")
    elif choice == '3':
      deck.view_cards()
      try:
        idx = int(input("Enter card number to delete: ")) - 1
        deck.delete_card(idx)
      except ValueError:
        print("❌ Please enter a valid number.")
    elif choice == '4':
      deck.study_session()
    elif choice == '5':
      print("Goodbye! Keep learning 🚀")
      break
    else:
      print("❌ Invalid choice. Please choose between 1 and 5.")


if __name__ == "__main__":
  main()
