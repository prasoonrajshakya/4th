import os

os.system("cls")  # Windows

a=input("Enter a string: ")
vowelSet="aeiouAEIOU"
vowel=0
consonant=0
for ch in a:
  if ch.isalpha():
    if ch in vowelSet:
      vowel +=1
    else:
      consonant +=1
print(f"Number of vowels={vowel}")
print(f"Number of consonants={consonant}")
