import random

# it's independent module, not part of character generator

while True:
    a = int(input(":"))
    if a != 0:
        print(random.randrange(101))
        print(random.randrange(11))
