import random

# it's independent module, not part of characterMAIN.py

while True:
    a = int(input(":"))
    if a != 0:
        print(random.randrange(101))
        print(random.randrange(11))