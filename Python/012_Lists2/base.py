import random 
elist = []
x = int(input("how many nums you want "))
for q in range(0, x):
    k = random.randrange(1,10)
    elist.append(k)
print(elist)
    