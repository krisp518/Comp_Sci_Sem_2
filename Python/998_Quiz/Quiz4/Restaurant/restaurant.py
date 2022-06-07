import random

restraunt = ["big ol smeat pizzaeria", "authentic mexican food no cap", "sushi bushi wushi kooshi"]
mexican = ["meat burrito", "better buritto", "the bestest greatest but also the worst burrito"]
italiano = ["lazagnah", "pizzer", "big ol shmeat for like 3 cents"]
sushi = ["bushi", "wushi", "kooshi"]

print("alright so like pick one of these given restrqaunts.")
print("b for pizzeria, a for mexican, and s for sushi bushi wushi kooshi")
q = input(restraunt)

if q == "a":
    print("aye we suggest the one the only... ")
    print(mexican[random.randrange(0, 3)])

elif q == "b":
    print("we ah seuggest tha one and tha only...")
    print(italiano[random.randrange(0, 3)])
    
elif q == "s":
    print("私たちは唯一無二を提案します...")
    print(sushi[random.randrange(0, 3)])
    
    
    


