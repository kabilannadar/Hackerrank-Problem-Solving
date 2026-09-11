n = int(input())
arr = [ int(i) for i in input().split() ]

mx = arr[0]
for score in arr:
    if score > mx:
        mx = score
    
sm = -101
for score in arr:
    if score > sm and score < mx:
        sm = score
print(sm)