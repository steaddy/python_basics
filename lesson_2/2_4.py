user_input = input("Введите предложение: ")

input_list = user_input.split()

i = 0
word = ''
while i < len(input_list):
    word = input_list[i]
    if len(word) > 10:
        word = word[0:9]
    print(f"{i + 1}) {word}")
    i += 1
