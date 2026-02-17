char = input("Enter a character: ")

if len(char) != 1:
    print("Please enter only ONE character.")

elif ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
    print("It is an alphabet letter.")

else:
    print("It is NOT an alphabet letter.")
 