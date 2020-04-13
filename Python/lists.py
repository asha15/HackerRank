lst = []
n = int(input())

for x in range (n):
    user_input = input()
    
    if('insert' in user_input):
        position = int(user_input[6: 8])
        value = int(user_input[8:])
        lst.insert(position, value)
    elif('print' in user_input):
        print(lst)
    elif('remove' in user_input):
        lst.remove(int(user_input[6:]))
    elif('append' in user_input):
        lst.append(int(user_input[6:]))
    elif('sort' in user_input):
        lst.sort()
    elif('pop' in user_input):
        lst.pop()
    elif('reverse' in user_input):
        lst.reverse()

