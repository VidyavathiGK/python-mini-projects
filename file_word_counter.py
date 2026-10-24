import os
from collections import Counter

class FileAnalyzer:
    @staticmethod
    def analyze_file(filepath):
        if not os.path.exists(filepath):
            print(f"Error: The file '{filepath}' does not exist.")
            return

        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            lines = content.splitlines()
            words = content.split()
            characters = len(content)

        word_counts = Counter(w.lower().strip(".,!?()[]{}\"'") for w in words)
        most_common = word_counts.most_common(5)

        print(f"\n--- File Analysis Report: {filepath} ---")
        print(f"Total Lines: {len(lines)}")
        print(f"Total Words: {len(words)}")
        print(f"Total Characters: {characters}")
        print("Top 5 Most Frequent Words:")
        for word, freq in most_common:
            if word:
                print(f"  - '{word}': {freq} time(s)")


if __name__ == "__main__":
    print("=== File Word Counter ===")
    path = input("Enter the path/name of the text file (e.g., sample.txt): ").strip()
    FileAnalyzer.analyze_file(path)
