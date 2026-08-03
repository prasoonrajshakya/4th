#14. Write a Python program to count the occurrence of each word in a given sentence.
import os
from collections import Counter
os.system("cls")

sentence = input("Enter a sentence: ")
sentence = sentence.lower()
word = sentence.split()
word_counter= Counter(word)

for word, count in word_counter.items():
    print(f"{word:<10} {count}")