
dictionary = {}
highest = ""
game = 1
while game != 'n': 
    name = input("Enter name: ")    
    bid = input("Place bid: ")
    
    dictionary[name] = bid 
    game = input("Place another bid by entering non 'n': ")
    print('\n' * 2)
    
for i in dictionary:
    if dictionary[i] > highest:
        highest = i
 

print(dictionary)
print("highest bidder is", highest)