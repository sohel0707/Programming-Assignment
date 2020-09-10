string=input()
words = string.split()

occ = {}

for word in words:
    occ[word] =occ.get(word,0) + 1

print(occ)
