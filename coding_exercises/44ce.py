#CE1 
#My code
# user_amount = input("How many dollars have you got? ")
# user_amount = int(user_amount) * 0.95

# print(f"The amount in euros is : {user_amount}")
#Teachers Code
# rate = 0.95

# dollars = float(input("How many dollars have you got? "))
# euros = dollars * rate
# print("The amount in euros is: ")
# print(euros)

#CE2
#My Code
# ranking = ['John', 'Sen', 'Lisa']
 
# user_rank = int(input("Enter a rank number: "))
# user_rank = user_rank - 1

 #Teacher Code       
# ranking = ['John', 'Sen', 'Lisa']
# rank = int(input("Enter rank number: ")) - 1
# name = ranking[rank]
# print(name)


# CE3
#my code didnt work
# ranking = ['John', 'Sen', 'Lisa']
# rank = input("Enter a name: ")
# match ranking:
#     case 'John':
#         print(ranking.index("John"))

#teachers code
ranking = ['John', 'Sen', 'Lisa']
name = input("Enter a name: ")
rank = ranking.index(name) + 1
print(rank)