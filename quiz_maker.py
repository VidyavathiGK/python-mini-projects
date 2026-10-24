class QuizMaker:
    def __init__(self):
        self.questions = []

    def add_question(self):
        question = input("Enter the question text: ").strip()
        options = []
        print("Enter 4 options:")
        for i in range(1, 5):
            opt = input(f"  Option {i}: ").strip()
            options.append(opt)

        try:
            correct_num = int(input("Enter the correct option number (1-4): "))
            if 1 <= correct_num <= 4:
                correct_answer = options[correct_num - 1]
                self.questions.append({"q": question, "options": options, "answer": correct_answer})
                print("Question added successfully!")
            else:
                print("Invalid option number. Must be between 1 and 4.")
        except ValueError:
            print("Please enter a valid number for the correct answer.")

    def take_quiz(self):
        if not self.questions:
            print("No questions available in the quiz generator.")
            return

        score = 0
        print(f"\n--- Starting Custom Quiz ({len(self.questions)} Questions) ---")
        for idx, item in enumerate(self.questions, 1):
            print(f"\nQ{idx}: {item['q']}")
            for opt_idx, opt in enumerate(item['options'], 1):
                print(f"  {opt_idx}. {opt}")

            try:
                ans_choice = int(input("Your choice (1-4): "))
                if item['options'][ans_choice - 1] == item['answer']:
                    print("Correct! ✅")
                    score += 1
                else:
                    print(f"Incorrect. ❌ The correct answer was: {item['answer']}")
            except (ValueError, IndexError):
                print(f"Invalid input. ❌ The correct answer was: {item['answer']}")

        print(f"\nQuiz Complete! Your Score: {score}/{len(self.questions)}")


if __name__ == "__main__":
    qm = QuizMaker()
    while True:
        print("\n=== Quiz Maker Menu ===")
        print("1. Add Question")
        print("2. Take Quiz")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()
        if choice == "1":
            qm.add_question()
        elif choice == "2":
            qm.take_quiz()
        elif choice == "3":
            print("Good luck with your studies!")
            break
        else:
            print("Invalid option.")
