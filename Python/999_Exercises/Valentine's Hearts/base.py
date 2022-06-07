import random

people = ["You", "U", "Your Mom", "Your Dad", "Your Dog", "Your Family", "Your Cousin", "Angel", "The One", "Your Friend", "Your Lover", "Dear"]
compliments = ["is hot", "has a big ol shmeat", "is packin", "deez nuts", "is gamer"]

x = random.randrange(0, len(people))
y= random.randrange(0, len(compliments))

print(people[x] + " " + compliments[y])
