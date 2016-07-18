def histogram(word):
    d = dict()
    for char in word:
        d[char] = d.get(char, 0) + 1
    return d

print histogram('brontosaurus')

