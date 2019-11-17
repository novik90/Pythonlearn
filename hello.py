from datetime import datetime
import time
import random


def lesson_1():
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21,
            23, 25, 27, 29, 31, 33, 35, 37, 41,
            43, 45, 47, 49, 51, 53, 55, 57, 59]

    for i in range(5):
        right_this_time = datetime.today().minute

        if right_this_time in odds:
            print("This minute seems a little odd.")
        else:
            print("Not an odd minute")
        wait_time = random.randint(1, 60)
        print(wait_time)
        if i != 5:
            time.sleep(wait_time)


def lesson_2():
    word = "bottles"

    for beer_num in range(99, 0, -1):
        print(beer_num, word, "of beer on the wall.")
        print(beer_num, word, "of beer.")
        print("Take one down.")
        print("Paste around.")

        if beer_num == 1:
            print("No more bottles of beer on the wall.")
        else:
            new_num = beer_num - 1
            if new_num == 1:
                word == "bottle"
            print(new_num, word, "of beer on the wall.")
        print()


def factorial(x):
    if x <= 0:
        return 1
    elif x > 10:
        return "number so lagre"
    else:
        return x * factorial(x - 1)


def lesson_3():
    vowels = ['a', 'e', 'i', 'o', 'u']
    word = input("write the word... ")
    found = []
    for letter in word:
        if letter in vowels:
            if letter not in found:
                found.append(letter)
    for vowel in found:
        print(vowel)


def lesson_4():
    phrase = "Don't panic"
    plist = list(phrase)
    print(phrase)
    print(plist)
    for i in range(3):
        plist.pop()
    plist.remove("'")
    plist.remove("D")
    plist.insert(2, plist.pop(3))
    new_phrase = ''.join(plist)
    plist.extend([plist.pop(), plist.pop()])
    print(plist)
    print(new_phrase)


def lesson_5():
    phrase = "Don't panic"
    plist = list(phrase)
    print(phrase)
    print(plist)
    new_phrase = ''.join(phrase[1:3] +
                         phrase[-6:3:-1] +
                         phrase[-4:5:-1])
    print(plist)
    print(new_phrase)


def lesson_6():
    paranoid_android = "Marvin"
    letters = list(paranoid_android)
    for char in letters:
        print(char)


def lesson_6_2():
    paranoid_android = "Marvin, the Paranoid Andorid"
    letters = list(paranoid_android)
    for char in letters[:6]:
        print('\t', char)
    for char in letters[-7:]:
        print('\t' * 2, char)
    for char in letters[12:20]:
        print('\t' * 3, char)


def lesson_7():
    vowels = {'a', 'e', 'i', 'o', 'u'}
    word = input('Provide a word to search for vowels: ')
    found = {}
    for letters in word:
        if letters in vowels:
            found.setdefault(letters, 0)
            found[letters] += 1

    for k, v in sorted(found.items()):
        print(k, 'was found', v, 'times.')
