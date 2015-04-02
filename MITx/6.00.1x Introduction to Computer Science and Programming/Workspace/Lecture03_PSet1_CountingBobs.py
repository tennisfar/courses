s = 'pcobooobobobobobbobb'
#s = 'abcdefghijklmnopqrstu'

num = 0

for i in range(len(s)-2):
    j = i+3
    # print(s[i:j])
    if s[i:j] == 'bob':
        num +=1

print('Number of times bob occurs is: ' + str(num))
