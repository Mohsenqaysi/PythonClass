# Variables and Types
# This is a list of numbers:
n = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,20,24,27,30]

# go though the list and print out each number:

for number in n:
    print(number)
    
    
print('\n\n----------------------\n\n')


for number in range(0,100):

    if (number % 2) == 0: # if the reminder is 0 that means the number is EVEN.
        print("The number is even: {} ".format(number))
    else:
        print("The number is odd: {} ".format(number))


"""
Task:
Given an integer, , perform the following conditional actions:
If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5 , print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
"""

for index, is_odd in enumerate(n):
    is_odd = is_odd % 2
    
    if is_odd == 1 :
        print('Weird Odd: {} '.format(n[index]))   
    elif is_odd == 0 and index in range(2,5):
        print('Not Weird Even: {} '.format(n[index]))   
    elif is_odd == 0 and index in range(6,20):
        print('Weird Odd: {} '.format(n[index]))   
    else:
        print('Not Weird Even: {} '.format(n[index]))   
  
