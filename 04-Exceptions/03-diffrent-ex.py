
try:
    age = int(input("Your Age: (for testing enter zero)"))
    factor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print(" no exceptions were thrown")

print("....")
print("....")
print("code continues")


try:
    age = int(input("Your Age: (for testing enter zero)"))
    factor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")

except (ZeroDivisionError):
    print("You enter 0.")
    print("""THIS WILL BE IGNORED - IF THERE IS AN ERROR 
    SINCE WE ALREADY CHECK THIS TYPE OF ERROR IN THE ABOVE.
    SO THE EXCUTION WILL STOP THERE AND NOT GET TO HERE 
    """)
else:
    print(" no exceptions were thrown")

print("....")
print("....")
print("code continues")
