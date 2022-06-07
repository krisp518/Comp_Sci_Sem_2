sentence = "whale hello there. Don't we all love whales? I absolutely love whales! whales are so huge!!!"
counter = 0
w = 0
for q in range(0, len(sentence)):
    counter = counter+1
    if sentence[q:counter+4] == "whale":
        w = w + 1
    elif sentence[q:counter+4] == "Whale":
        w = w + 1

print(w)


with open('moby.txt') as f:
    for line in f:
        sentence = line.strip()
        w = 0
for e in range(0, len(sentence)):
    counter = counter+1
    if sentence[e:counter+4] == "whale":
        w = w + 1
    elif sentence[e:counter+4] == "Whale":
        w = w + 1

print(w)

f.close()
