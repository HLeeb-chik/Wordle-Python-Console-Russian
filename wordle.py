from colorama import Fore, Back, Style
import random
import os
import time
from colorama import init
init()


alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
            "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]


def russianWord(text):
    for letter in text:
        if letter.lower() not in alphabet:
            break
        else:
            continue
        break
    else:
        return True
    return False


script_dir = os.path.dirname(__file__)
word5_file_path = os.path.join(script_dir, 'word5.txt')


num_word = -1
hidden_word = []
word = ""


def randomWord():
    with open(word5_file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    file.close()
    num_word = random.randint(1, len(lines))
    return list(lines[num_word].upper()), num_word


def Game():
    hidden_word, num_word = randomWord()
    print(Style.BRIGHT+Fore.CYAN+"\nСлово загадано, У тебя 6 попыток")
    print("Введите слова: " + Style.RESET_ALL)
    for i in range(6):

        word_is_true = False

        while not word_is_true:
            word = input().upper()
            if russianWord(word) and len(word) == 5:
                word_is_true = True
            else:
                print(Style.DIM + Fore.LIGHTRED_EX +
                      "Введите слово из 5 букв русского алфавита!:\n" + Style.RESET_ALL)
        word = list(word)

        if word+["\n"] == hidden_word:
            for h in word:
                print(Style.BRIGHT + Back.GREEN +
                      h + Style.RESET_ALL, end=" ", flush=True)
                time.sleep(0.2)

            print(Back.GREEN+" ".join(word))
            print(Fore.MAGENTA+"Ты угадал! Молодец!" + Fore.BLACK +
                  f"index={num_word+1}" + Style.RESET_ALL)
            break

        for l in range(len(word)):
            if word[l] in hidden_word:
                if word[l] == hidden_word[l]:
                    print(Style.BRIGHT + Back.GREEN +
                          word[l] + Style.RESET_ALL, end=" ", flush=True)
                else:
                    print(Style.BRIGHT + Back.YELLOW +
                          word[l] + Style.RESET_ALL, end=" ", flush=True)
            else:
                print(Back.LIGHTBLACK_EX +
                      word[l] + Style.RESET_ALL, end=" ", flush=True)

            time.sleep(0.1)

        print()

    else:
        print("К сожилению ты проиграл... Повезёт в следующий раз!")
        print(Fore.YELLOW+Back.BLACK +
              f"Загаданое слово - {"".join(hidden_word)}"+Fore.BLACK+f"index={num_word+1}" + Style.RESET_ALL)


# Wordle
print("-----------------"+Fore.BLACK+Back.YELLOW+"W"
      + Fore.YELLOW+Back.BLACK+"O" + Style.RESET_ALL + " "
      + Fore.BLACK+Back.YELLOW+"R" + Style.RESET_ALL + " "
      + Fore.YELLOW+Back.BLACK+"D" + Style.RESET_ALL + " "
      + Fore.BLACK+Back.YELLOW+"L" + Style.RESET_ALL + " "
      + Fore.YELLOW+Back.BLACK+"E" + Style.RESET_ALL + " "
      + Style.RESET_ALL+"----------------")

time.sleep(0.2)

# logo
print("                                   ", end="")
for _ in "by HLeeb_":
    print(Fore.CYAN+_, end="", flush=True)
    time.sleep(0.1)
else:
    print("\n"+Style.RESET_ALL)
time.sleep(0.2)

# rule
print("Правила очень просты:",
      "•Загадано слово из 5 русских букв.",
      "•Каждым ходом игрок вводит свое слово, а програма определяет какие буквы входят в слово.",
      " " + Style.BRIGHT+Back.GREEN + " " + Style.RESET_ALL +
      " " + "- Буква есть в слове и стоит на своём месте",
      " " + Style.BRIGHT+Back.YELLOW + " " + Style.RESET_ALL +
      " " + "- Буква есть в слове, но она стоит не на своём месте",
      " " + Back.LIGHTBLACK_EX + " " + Style.RESET_ALL +
      " " + "- Буквы нет в загаданом слове", "Удачи!",
      sep="\n")


Game()  # Enter Game
while input('Enter -> продолжить;\nЛюбая клавиша-> выйти:\n') == "":  # relode

    Game()

# print(Fore.GREEN + 'зеленый текст')
# print(Back.YELLOW + 'на желтом фоне')
# print(Style.BRIGHT + 'стал ярче' + Style.RESET_ALL)
# print('обычный текст')
input()

print(num_word, hidden_word, word)
