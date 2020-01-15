values = []

# we can write:
# for x in range(5):
#     values.append(x * 2)

# OR USE COMPREHENSIONS :
# [expression for item in items]
values = [item * 2 for item in range(5)]
print(values)


# AND FOR A SET :
values = {item * 2 for item in range(5)}
print(values)

# SET IS {} AND ALSO DIC, BUT IN DIC THERE IS NO ()
print("""
        SET IS DECLARE WITH {} 
        AND ALSO DIC, 
        BUT IN SET THERE IS NO KEY
        """)
values = {x: x*2 for x in range(5)}
print(values)

print(' set with COMPREHENSIONS: ')
values = {x*2 for x in range(5)}
print(values)
