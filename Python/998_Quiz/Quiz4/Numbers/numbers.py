#redoing it 
mynumbers = [6,9,32,28,15,22,3,18]

themax = mynumbers[0]
themin = mynumbers[0]
add = 0
avg = 0

for q in range (0, len(mynumbers)):
    if (mynumbers[q] > themax):
       ararar = themax = mynumbers[q]
print(ararar)

for w in range (0, len(mynumbers)):
    if (mynumbers[w] < themin):
      hee = themin = mynumbers[w]
print(hee)
        
for e in range(0, len(mynumbers)):
    add = add+mynumbers[e]
avg = add/len(mynumbers)
print(avg)

        
