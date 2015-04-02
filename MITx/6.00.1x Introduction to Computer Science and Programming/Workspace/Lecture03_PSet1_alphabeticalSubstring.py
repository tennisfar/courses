s = 'azcbobobegghakl'
s = 'abcdefghijklmnopqrstuvwxyz'

num = 1
highestNum = 0
subStr = ''
longestSubstring = ''
char = ''

for i in range(len(s)-1):

    str1 = s[i:i+1]
    str2 = s[i+1:i+2]

    if i == 0:
        subStr = str1
        longestSubstring = subStr

    if str2 >= str1:
        num += 1
        subStr += str2
        if num > highestNum:
            highestNum = num
            longestSubstring = subStr
    else:
        num = 1
        subStr = str2

print('Longest substring in alphabetical order is: ' + longestSubstring)
