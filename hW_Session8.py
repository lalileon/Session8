import requests
r = requests.get("https://raw.githubusercontent.com/itb-ie/contest/master/text.txt")
print(r.text)
a = r.text
lines = a.split()

vowels = "aeiou"
alphabet = "abcdefghijklmnopqrstuvwxyz"

sentence = ""
for line in lines:
    vowel_count = 0
    for char in line:
        if char in vowels:
            vowel_count += 1
    if vowel_count == 0:
        sentence += " "
    else:
        sentence += alphabet[vowel_count-1]
print(sentence)

shift = 3
encrypted_sentence = ""

for char in sentence:
    if char == " ":
        encrypted_sentence += " "
    else:
        index = alphabet.index(char)
        shifted_index = (index + shift) % 26
        encrypted_sentence += alphabet[shifted_index]

print(encrypted_sentence)





