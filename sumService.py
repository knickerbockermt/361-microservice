import time
import random

while True:
    file = open("sumService.txt", "r")
    r = file.read()
    file.close()

    if "," in r:
        r = r.split(",")

        for i in range(len(r)):
            r[i] = int(r[i])

        mult, rng, modif = r

        total = modif

        for i in range(mult):
            total += (random.randint(1, rng))

        file = open("sumService.txt", "w")
        file.write(str(total))
        file.close()

