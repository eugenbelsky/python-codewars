
def is_valid_walk(walk):

    n = walk.count("n")
    s = walk.count("s")
    w = walk.count("w")
    e = walk.count("e")

    if (n == s) and (w == e) and (len(walk) == 10):
        return True

    return False


print(is_valid_walk(['w', 'e', 'w', 'e', 'w',
      'e', 'w', 'e', 'w', 'e', 'w', 'e']))
