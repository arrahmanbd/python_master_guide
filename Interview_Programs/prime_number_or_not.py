user_input = int(input('enter a number:- '))
if user_input > 1:
    for i in range(2, user_input):
        if (user_input % i)==0:
            print('it is not a prime number')
            break
        
    else:
        print('it is a prime number')
        
else:
    print('enter a valid number')
    
    
    
# Another way of approach

num = int(input('enter a number:- '))
if num == 1:
    print('prime number of 1 is 1')
elif num < 1:
    print('enter number greater than 1')
else:
    for i in range(2, num):
        if num % i ==0 :
            print('not a prime number')
            break
    else:
        print('prime number')
            
#Another way
num = int(input('enter a number:- ')) 
if num <= 1: 
     print('enter number greater than 1') 
else: 
     for i in range(2, num): 
         if num % i ==0 : 
             print('{num} not a prime number') 
             break 
     else: 
         print(f'{num} is prime number')



#Workingway
num = int(input("Enter a number: "))

# If number is greater than 1
if num > 1:
   # Check if factor exist  
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
   else:
       print(num,"is a prime number")
       
# Else if the input number is less than or equal to 1
else:
   print(num,"is not a prime number")