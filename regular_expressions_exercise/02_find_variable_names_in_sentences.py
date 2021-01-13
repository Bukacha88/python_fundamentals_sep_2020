import re

data = input()
pattern = r"((?<=^_)|(?<=\s_))[a-zA-Z0-9]+\b"


numbers = [el.group() for el in re.finditer(pattern, data)]
print(','.join(numbers))