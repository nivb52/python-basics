text = " file close automatically (if found) because of the WITH STEATMENT"
try:
    with open("text2.txt") as file, open("text.txt") as target:
        print("file opened")
        # CREATE ERROR
        x = 10 / 0  # error
except (ZeroDivisionError, FileNotFoundError):
    print('some error but - ')
    print(text)

else:
    print(text)
