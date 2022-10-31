space_count, word_count = 4, 1

while word_count != 4:
    print(" " * space_count + "#" * word_count * 2)
    space_count -= 1
    word_count += 1

while word_count != 0:
    print(" " * space_count + "#" * word_count * 2)
    space_count += 1
    word_count -= 1
