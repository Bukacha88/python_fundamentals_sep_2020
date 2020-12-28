message = input().split(' ')


def get_digits(text):
    return "".join(list(filter(str.isdigit, text)))


word = ''
for el in range(len(message)):
    word += (chr(int(get_digits(message[el]))))
    for character in message[el]:
        if character.isalpha():
            word += character
    list_of_word = list(word)
    list_of_word[1], list_of_word[-1] = list_of_word[-1], list_of_word[1]
    word = "".join(list_of_word)
    print(word, end=" ")
    word = ''
