import re


class MarkdownConverter:

  @staticmethod
  def convert(markdown_text: str) -> str:
    lines = markdown_text.strip().split("\n")
    html_lines = []
    in_list = False

    for line in lines:
      line = line.strip()

      # Headers
      if line.startswith("### "):
        if in_list:
          html_lines.append("</ul>")
          in_list = False
        html_lines.append(f"<h3>{line[4:]}</h3>")
      elif line.startswith("## "):
        if in_list:
          html_lines.append("</ul>")
          in_list = False
        html_lines.append(f"<h2>{line[3:]}</h2>")
      elif line.startswith("# "):
        if in_list:
          html_lines.append("</ul>")
          in_list = False
        html_lines.append(f"<h1>{line[2:]}</h1>")

      # Unordered Lists
      elif line.startswith("- ") or line.startswith("* "):
        if not in_list:
          html_lines.append("<ul>")
          in_list = True
        item_text = line[2:]
        # Apply inline formatting inside list items
        item_text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", item_text)
        item_text = re.sub(r"\*(.*?)\*", r"<em>\1</em>", item_text)
        html_lines.append(f"  <li>{item_text}</li>")

      # Regular Paragraphs
      elif line:
        if in_list:
          html_lines.append("</ul>")
          in_list = False
        # Inline bold and italics
        formatted = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", line)
        formatted = re.sub(r"\*(.*?)\*", r"<em>\1</em>", formatted)
        html_lines.append(f"<p>{formatted}</p>")

    if in_list:
      html_lines.append("</ul>")

    return "\n".join(html_lines)


if __name__ == "__main__":
  sample_md = """
    # Hello World
    This is a **bold** statement and this is *italic*.
    - Python Programming
    - Automation Scripts
    """
  print(MarkdownConverter.convert(sample_md))
