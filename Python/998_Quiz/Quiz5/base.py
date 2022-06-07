q = input("say your fav number in sentence ")
w = int(input("what y age? "))

x = 0

for e in range(0, len(q)):
    if q[e:x] == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 0:
        num = 4
    x=x+1
    
final = w * num  
print(final)