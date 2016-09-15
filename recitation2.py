didBreak = False
word = raw_input("Enter word: ")
word2 = raw_input("Enter word2: ")
for ch in word:
    for ch2 in word2:
        if ch == ch2:
            didBreak = True
            break
        else:
            print ch, ch2
    print "done with first"
    if didBreak == True:
        break
print "end"
