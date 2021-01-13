import re

numbers = []
pattern = r"\d+"
while True:

    text = input()
    if text:
        numbers += re.findall(pattern, text)
    else:
        break
print(*numbers)