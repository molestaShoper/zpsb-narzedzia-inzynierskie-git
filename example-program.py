#!/usr/bin/env python3

word = input("Please enter a word: ").lower()

vowels_list = ["a", "e", "i", "o", "u"]
vowels = 0
consonants = 0

for letter in word:
    if letter.isalpha():
        if letter in vowels_list:
            vowels += 1
        else:
            consonants += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)

#Dobrze napisany kodzik pozdrawiam
#Również potwierdzam - bardzo fajny kod (12.01.2025)
#Ok 
