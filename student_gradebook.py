class Student:
    """Represents an individual student with personal details and course marks."""

    def __init__(self, student_id: str, name: str):
        self.student_id = student_id
        self.name = name
        self.scores = {}

    def add_score(self, subject: str, score: float) -> None:
        """Adds or updates a score for a specific subject."""
        if 0 <= score <= 100:
            self.scores[subject] = score
        else:
            print("Invalid score! Must be between 0 and 100.")

    def calculate_average(self) -> float:
        """Computes the average score across all subjects."""
        if not self.scores:
            return 0.0
        return sum(self.scores.values()) / len(self.scores)


class GradeBook:
    """Manages a collection of students and performs aggregate operations."""

    def __init__(self):
        self.students = {}

    def add_student(self, student_id: str, name: str) -> None:
        """Registers a new student in the grade book."""
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name)
            print(f"Student '{name}' added successfully.")
        else:
            print("Student ID already exists!")

    def record_score(self, student_id: str, subject: str, score: float) -> None:
        """Records a grade for a specific student and subject."""
        if student_id in self.students:
            self.students[student_id].add_score(subject, score)
            print(f"Recorded score {score} for {subject}.")
        else:
            print("Student not found!")

    def display_report(self, student_id: str) -> None:
        """Displays academic performance summary for a specific student."""
        if student_id not in self.students:
            print("Student not found!")
            return

        student = self.students[student_id]
        average = student.calculate_average()

        print(f"\n--- Academic Report: {student.name} (ID: {student.student_id}) ---")
        if not student.scores:
            print("No grades recorded yet.")
        else:
            for subject, score in student.scores.items():
                print(f"  - {subject}: {score}")
            print(f"Average Score: {average:.2f}")


# --- Example Usage ---
if __name__ == "__main__":
    gradebook = GradeBook()

    # Add students
    gradebook.add_student("S001", "Vidyavathi")
    gradebook.add_student("S002", "Rahul")

    # Record grades
    gradebook.record_score("S001", "Python Programming", 88.5)
    gradebook.record_score("S001", "Database Management", 92.0)
    gradebook.record_score("S001", "Data Structures", 85.0)

    # Display reports
    gradebook.display_report("S001")
