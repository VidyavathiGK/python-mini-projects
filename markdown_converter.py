import re

class MarkdownConverter:
    @staticmethod
    def convert_line(line):
        # Headers: #, ##, ###
        if line.startswith("# "):
            return f"<h1>{line[2:]}</h1>"
        elif line.startswith("## "):
            return f"<h2>{line[3:]}</h2>"
        elif line.startswith("### "):
            return f"<h3>{line[4:]}</h3>"

        # Bold: **text**
        line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line)
        # Italics: *text*
        line = re.sub(r'\*(.*?)\*', r'<em>\1</em>', line)

        # Default paragraph
        if line.strip():
            return f"<p>{line}</p>"
        return "<br>"

    @classmethod
    def convert_text(cls, markdown_text):
        lines = markdown_text.splitlines()
        html_lines = [cls.convert_line(line) for line in lines]
        return "\n".join(html_lines)


if __name__ == "__main__":
    print("=== Markdown to HTML Converter ===")
    print("Enter your Markdown text (type 'END' on a new line when finished):")
    
    input_lines = []
    while True:
        line = input()
        if line == "END":
            break
        input_lines.append(line)

    raw_markdown = "\n".join(input_lines)
    html_output = MarkdownConverter.convert_text(raw_markdown)

    print("\n--- Converted HTML Output ---")
    print(html_output)
