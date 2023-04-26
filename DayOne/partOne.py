# 1- Write a Python program which accepts the user's first and last name and print them in
#reverse order with a space between them

# firstName = input('Hello, please enter your first name: ');
# lastName = input('Second, enter your last name: ');

# print(f'Your name is: {lastName[::-1]} {firstName[::-1]}');


# 2- Write a Python program that accepts an integer (n)
#  and computes the value of n+nn+nnn.

# userDummyInput = input('Enter your number: ');

# if( userDummyInput.isdigit() ) :
#     userDummyInput = int(userDummyInput); 
#     result = 123 * userDummyInput; # n + nn + nnn = n + (10 * n + n) + (100 * n + 10 * n + n)= n + 10n + n + 100n + 10n + n = 123n

#     print(f"The result is {result} ");
# else:
#     print("Invalid input! You should only enter a number not a character.");

# 3- Write a Python program to print the following here document

# print(""" 
#     Sample string :
#     a string that you "don't" have to escape
#     This
#     is a ....... multi-line
#     heredoc string 
# """);

# 4- Write a Python program to get the volume of a sphere with radius 6.
# PI = 3.14159;
# radius = 6 ; # given
# result = round((3/4)*PI*(radius)**3)
# print ( result );

# 5-  Write a Python program that will accept the base and height of a triangle and compute the area.

# width = input(' Please enter the width of the triangle: ');
# height = input(' Now enter the height: ');

# if ( width.isdigit() and height.isdigit() ):
#     width = int (width);
#     height = int (height);
#     triangleArea = (0.5)* width * height;
#     print(f'The area equals to : {triangleArea}');
# else:
#     print('Please make sure that you entered a valid width and height !');

# 6-  Write a Python program to construct the following pattern, using a nested for loop.

# n = input("Enter your magic number: ");
# if (n.isdigit() ):
#     n = int(n);
#     for i in range(1, n+1):
#         for j in range(1, i+1):
#             print("*", end=" ")
#         print();
#     for i in range(n-1, 0, -1):
#         for j in range(1, i+1):
#             print("*", end=" ")
#         print();
# else :
#     print ("Please enter a valid number");

# 7- Write a Python program that accepts a word from the user and reverse it

# reverseThis = input('Enter the word that you want to be reversed: ');
# if ( reverseThis.isalpha() ):
#     print(f' {reverseThis[::-1]} ');
# else:
#     print('You entered a non-valid input, please make sure you entered a string');

# 8- Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

# for i in range (0,6):
#     if (i != 3):
#         print (f'{i}' , end=" ");    

# 9- Write a Python program to get the Fibonacci series between 0 to 50

# a = 0;
# b = 1;
# while b < 50:
#     print(b, end=' ')
#     a, b = b, a + b;

# 10- Write a Python program that accepts a string and calculate the number of digits and letters

# calculateMyChar = input('Please enter your string: ');
# counter = 0 ;
# for c in calculateMyChar:
#     if ( c != " " ):
#         counter = counter + 1 ;

# print(f'the Count = {counter}');