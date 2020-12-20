text = input()
occurrences = {}
for char in text:
    if not char == ' ':
        occurrences[char] = text.count(char)
for key, value in occurrences.items():
    print(f"{key} -> {value}")