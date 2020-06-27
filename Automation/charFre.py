def character_frequency(filename):
    '''Count the frequency of each character in the given filename'''
    try:
        f = open(filename)
    except OSError:
        return None

    characters = {}
    for line in f:
        for char in line:
            characters[char] = characters.get(char,0) + 1
    f.close()
    return characters
