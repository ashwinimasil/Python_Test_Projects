# #Greater no in the list
# def Find_max(numbers):
#
#     b = numbers[0]
#     for maxno in numbers:
#         if maxno > b:
#             b = maxno
#     return maxno

# i=0
# while i<= 4:
#     print (i)
#     i = i+ 1
# print ("Done")

#Refresh

secret_number='4'
guess_lower=0
guess_upperlimit=2
while guess_lower<=guess_upperlimit:
    Guess_no=input("Enter the Guess no")
    guess_lower += 1
    if Guess_no==secret_number:
        print("you win")
        break

else:
    print("you lost")
print("The End")


