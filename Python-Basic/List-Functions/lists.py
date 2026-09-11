N = int(input())
data = []
for i in range(N):
    command = input().split(' ')
    if command[0] == 'insert':
        data.insert(int(command[1]), int(command[2]))
    elif command[0] == 'print':
        print(data)
    elif command[0] == 'remove':
        data.remove(int(command[1]))
    elif command[0] == 'append':
        data.append(int(command[1]))
    elif command[0] == 'sort':
        data.sort()
    elif command[0] == 'pop':
        data.pop()
    elif command[0] == 'reverse':
        data.reverse()
    else:
        pass