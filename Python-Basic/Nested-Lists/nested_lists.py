n = int(input())
data = []
for i in range(n):
    name = input()
    score = float(input())
    data.append([score, name])
    
data.sort()

lowest = data[0][0]

for score, name in data:
    if score > lowest:
        second = score
        break

for score, name in data:
    if score == second:
        print(name)