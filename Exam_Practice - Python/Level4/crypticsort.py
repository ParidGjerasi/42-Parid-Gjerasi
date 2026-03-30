#not confirmed solution
import sys

if len(sys.argv) == 2:
    word = sys.argv[1]
    sorted_word = sorted(word)
    print("".join(sorted_word))