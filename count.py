word = raw_input("Enter a word: ")
letter = raw_input('Enter a letter: ')

count = 0

for character in word:
    if character == letter:
        count += 1

print count
