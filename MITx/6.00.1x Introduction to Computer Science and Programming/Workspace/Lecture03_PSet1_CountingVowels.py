s = 'azcbobobegghakl'

numOfVowels = 0
char = ''

for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        numOfVowels += 1

print('Number of vowels: ' + str(numOfVowels))
