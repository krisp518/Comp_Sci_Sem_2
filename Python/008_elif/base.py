x = int(input("ayo gimme first number "))
z = input("gimme operation symbol ")
y = int(input("gimme second number brother "))
if z == "+":
    print(str(x) + "+" + str(y) + "=" + str(x+y))
elif z == "-":
    print(str(x) + "-" + str(y) + "=" + str(x-y))
elif z == "*":
    print(str(x) + "*" + str(y) + "=" + str(x*y))
elif z == "/":
    print(str(x) + "/" + str(y) + "=" + str(x//y))