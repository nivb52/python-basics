letters = ["a","b","c","d"]

# // enumerate will give us the index
print(" using enumerate to get index: ")
# regular option: 
for letter in enumerate(letters):
    print(letter)
print(' but the above is a tupale (read only)')

# then we will extract it with prev lesson knowladge
print(" better option, if we don't want read-only vars :")
for index,letter in enumerate(letters):
    print(index,'-->',letter)
