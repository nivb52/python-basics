letters = ["a", "b", "c"]

print("""
we must verify the item exsist
since otherwise we will get an error
(not as in JavaScript Java and C base language)
""")

if "d" in letters:
    print(letters.index("d"))

print("we can also use method count:")
print( letters.count('d') )
