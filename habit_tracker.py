import datetime

class HabitTracker:
    def __init__(self):
        # Format: { "Habit Name": [ "YYYY-MM-DD", ... ] }
        self.habits = {}

    def add_habit(self):
        name = input("Enter new habit name: ").strip().capitalize()
        if name in self.habits:
            print("Habit already exists.")
        else:
            self.habits[name] = []
            print(f"Habit '{name}' created successfully!")

    def log_habit(self):
        if not self.habits:
            print("No habits available to log.")
            return
        
        print("\nSelect a habit to log for today:")
        names = list(self.habits.keys())
        for i, name in enumerate(names, 1):
            print(f"{i}. {name}")
        
        try:
            choice = int(input("Enter choice number: ")) - 1
            if 0 <= choice < len(names):
                selected_habit = names[choice]
                today = str(datetime.date.today())
                
                if today in self.habits[selected_habit]:
                    print(f"You already logged '{selected_habit}' for today!")
                else:
                    self.habits[selected_habit].append(today)
                    streak = len(self.habits[selected_habit])
                    print(f"Logged! Current streak for {selected_habit}: {streak} day(s)")
            else:
                print("Invalid selection.")
        except ValueError:
            print("Please enter a valid number.")

    def view_progress(self):
        if not self.habits:
            print("No habits tracked yet.")
            return
        
        print("\n--- Habit Progress ---")
        for name, logs in self.habits.items():
            print(f"Habit: {name} | Total Days Completed: {len(logs)}")
            if logs:
                print(f"  Last logged: {logs[-1]}")


if __name__ == "__main__":
    tracker = HabitTracker()
    while True:
        print("\n=== Habit Tracker Menu ===")
        print("1. Add New Habit")
        print("2. Log Habit for Today")
        print("3. View Progress")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            tracker.add_habit()
        elif choice == "2":
            tracker.log_habit()
        elif choice == "3":
            tracker.view_progress()
        elif choice == "4":
            print("Keep up the great habits!")
            break
        else:
            print("Invalid choice.")
