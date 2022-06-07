import random 
word_list = []
with open('allow_words.txt') as f:
    for line in f:
        l = line.strip()
        word_list.append(l)

num = random.randrange(0, 12972)
answer = word_list[num]
print(answer)
a = 0
for q in range(0,6):
    guess = input("guess word ")
    if guess == answer:
        print("u won")
        a = 1
        break
    else:
        print("guess again")
if a == 0:
    print("you lost retard")
    print("the answer was " + answer)
    
    
    
    
f.close()
