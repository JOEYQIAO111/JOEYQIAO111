"""
PROBLEM: Given a sentence (up to 1024 characters long), output the following:
1) The number of different letters. This will be a number from 1 to 26, inclusive.
2) The number of vowels. Vowels are the letters a, e, i, o, and u.
3) The number of uppercase letters.
4) The number of times that the most frequent letter appears. There is no distinction between lowercase and uppercase letters.
5) The longest word in the sentence. If there is a tie, print the one that appears first when sorting these words alphabetically without regard to lowercase and uppercase

INPUT: One line of data, containing a sentence, up to 1024 characters long
OUTPUT: Print the five statistics specified above in that order
SAMPLE INPUT
The quick brown fox named Roxanne, jumped over Bruno， a lazy dog.
SAMPLE OUTPUT
25
19
3
6
Roxanne
TEST INPUT
The 2019 All-Star Competition is at Wayne Hills HS in Wayne, New Jersey.
"""

inputs = 'The quick brown fox named Roxanne, jumped over Bruno， a lazy dog.'
letter = []


def first():
    for i in inputs:
        if i.isalpha():
            a = i.lower()
            if a not in letter:
                letter.append(a)

    print(len(letter))


def second():
    letters = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in inputs:
        if i.lower() in vowels:
            letters += 1
    print(letters)


def third():
    letters = 0
    for i in inputs:
        if i.isupper():
            letters += 1
    print(letters)


def forth():
    letters = {}
    for i in inputs:
        if i.isalpha():
            a = i.lower()
            if a not in letters:
                letters[a] = 1
            else:
                letters[a] += 1
    print(max(letters.values()))
    print(letters)


first()
second()
third()
forth()
