import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Generate Password!!")
number_letters = int(input("Enter ammount of letters.\n")) 
numberr_numbers = int(input(f"Enter ammount of numbers.\n"))
numberr_symbols = int(input(f"Enter ammount of symbols.\n"))

passowordList = []

for characters in range(1, number_letters + 1):
    passowordList += random.choice(letters)

for characters in range(1, numberr_numbers + 1):
    passowordList += random.choice(numbers)
    
for characters in range(1, numberr_symbols + 1):
    passowordList += random.choice(symbols)
    
random.shuffle(passowordList)

password = ""

for characters in passowordList:
    password += characters
    

print(f"Generated password: {password}")