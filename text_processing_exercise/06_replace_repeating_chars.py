text = input()
new_text = ''
for i in range(len(text)):
    if text[i] == text[i - 1] and not i == 0:
        continue
    else:
        new_text += text[i]
print(new_text)