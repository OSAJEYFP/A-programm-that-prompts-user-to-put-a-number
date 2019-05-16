##Write a program that prompts the user to input a number. The program
##should then output the number and a message saying whether the number is
##positive, negative, or zero.

number = input('Enter any number: ')
if number:
     number = int(number)
     if number < 0:
         print(f"You put a negative number {number}")
     elif number > 0:
         print(f"You put a postive number  {number}")
     else:
         print(f"You put a zero  {number}")       
else:
    print('put a number')
