
n = 132189


def digital_root(n):

    while len(str(n)) > 1:
        sum = 0
        for x in list(str(n)):
            sum += int(x)
        n = sum

    return n

print(digital_root(n))
