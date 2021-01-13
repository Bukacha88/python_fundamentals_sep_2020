import re
text = input()
word = input()

pattern = f"\\b{word}\\b"

match = re.findall(pattern, text, re.IGNORECASE)

print(len(match))