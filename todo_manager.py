from datetime import datetime
import json
import os


class Task:

  def __init__(self, title, category, priority, due_date):
    self.title = title
    self.category = category
    self.priority = priority.capitalize()  # High, Medium, Low
    self.due_date = due_date  # YYYY-MM-DD
    self.completed = False

  def mark_completed(self):
    self.completed = True

  def to_dict(self):
    return {
        "title": self.title,
        "category": self.category,
        "priority": self.priority,
        "due_date": self.due_date,
        "completed": self.completed,
    }


class TodoManager:

  def __init__(self, filename="tasks.json"):
    self.filename = filename
    self.tasks = self.load_tasks()

  def load_tasks(self):
    if os.path.exists(self.filename):
      try:
        with open(self.filename, "r") as file:
          data = json.load(file)
          tasks = []
          for item in data:
            task = Task(
                item["title"],
                item["category"],
                item["priority"],
                item["due_date"],
            )
            task.completed = item["completed"]
            tasks.append(task)
          return tasks
      except json.JSONDecodeError:
        return []
    return []

  def save_tasks(self):
    data = [task.to_dict() for task in self.tasks]
    with open(self.filename, "w") as file:
      json.dump(data, file, indent=4)

  def add_task(self, title, category, priority, due_date):
    new_task = Task(title, category, priority, due_date)
    self.tasks.append(new_task)
    self.save_tasks()
    print("✅ Task added successfully!")

  def view_tasks(self):
    if not self.tasks:
      print("📭 No tasks found.")
      return

    print("\n--- Your To-Do List ---")
    for index, task in enumerate(self.tasks, 1):
      status = "🟢 Done" | task.completed else "🔴 Pending"
      print(
          f"{index}. [{status}] {task.title} (Category: {task.category} |"
          f" Priority: {task.priority} | Due: {task.due_date})"
      )

  def complete_task(self, index):
    if 0 <= index < len(self.tasks):
      self.tasks[index].mark_completed()
      self.save_tasks()
      print(f"🎉 Task '{self.tasks[index].title}' marked as completed!")
    else:
      print("❌ Invalid task number.")

  def delete_task(self, index):
    if 0 <= index < len(self.tasks):
      removed = self.tasks.pop(index)
      self.save_tasks()
      print(f"🗑️ Deleted task: '{removed.title}'")
    else:
      print("❌ Invalid task number.")


def main():
  manager = TodoManager()

  while True:
    print("\n=== Task & Todo Manager ===")
    print("1. View Tasks")
    print("2. Add New Task")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
      manager.view_tasks()
    elif choice == "2":
      title = input("Enter task title: ").strip()
      category = input("Enter category (e.g., Work, Personal): ").strip()
      priority = (
          input("Enter priority (High, Medium, Low): ").strip().capitalize()
      )
      if priority not in ["High", "Medium", "Low"]:
        priority = "Medium"  # Default fallback

      due_date = input("Enter due date (YYYY-MM-DD): ").strip()
      # Simple validation for date format
      try:
        datetime.strptime(due_date, "%Y-%m-%d")
      except ValueError:
        print("⚠️ Invalid date format. Defaulting to today's date.")
        due_date = datetime.now().strftime("%Y-%m-%d")

      if title:
        manager.add_task(title, category, priority, due_date)
      else:
        print("❌ Task title cannot be empty.")
    elif choice == "3":
      manager.view_tasks()
      try:
        idx = int(input("Enter task number to mark complete: ")) - 1
        manager.complete_task(idx)
      except ValueError:
        print("❌ Please enter a valid number.")
    elif choice == "4":
      manager.view_tasks()
      try:
        idx = int(input("Enter task number to delete: ")) - 1
        manager.delete_task(idx)
      except ValueError:
        print("❌ Please enter a valid number.")
    elif choice == "5":
      print("Goodbye! Stay productive 🚀")
      break
    else:
      print("❌ Invalid choice. Please choose between 1 and 5.")


if __name__ == "__main__":
  main()
