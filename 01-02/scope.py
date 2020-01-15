avaible_in_the_all_file = ':::: avaible_in_the_all_file ::::'

def scope():
    avaible_in_the_all_file = 'you cant change global like this'
    print(avaible_in_the_all_file)

    if True:
        i_am_avaible_in_the_function = """
        avaible_in_the_function 
        even when i am in a if or for scope
        """    
    print(i_am_avaible_in_the_function)
    
    global message 
    message = "OVERRIDE global message  --> this is a bad practice"

# // PRINT AND GLOBAL 
message = 'global message'
print(avaible_in_the_all_file)
scope()
print(message)
