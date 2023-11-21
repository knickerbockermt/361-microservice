import random

def read_request():
    file = open("diceService.txt", "r")
    r = file.read()
    file.close()
    return r


def dice_roll(r):
    r = r.split(",")

    for i in range(len(r)):
        r[i] = int(r[i])

    mult, rng, modif = r
    total = modif

    for i in range(mult):
        total += (random.randint(1, rng))

    return total


def write_sum(total):
    file = open("diceService.txt", "w")
    file.write(str(total))
    file.close()


def main():
    while True:
        r = read_request()
        if "," in r:
            total = dice_roll(r)
            write_sum(total)


if __name__ == "__main__":
    main()
