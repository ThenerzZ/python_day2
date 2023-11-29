num_char = len(input("Whats your name?"))
#print("your name has " + num_char + " characters")
#-> output: TypeError: can only concatenate str (not "int") to str
#print(type(num_char)) #wenn man sich nicht sicher ist was für variable ist
new_num_char = str(num_char) #conversuion from int to string
print("your name has " + new_num_char + " characters.")


a = str(123) # oder = float(123) etc...

