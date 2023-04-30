#  1-  Given a list of numbers, 
#  create a function that returns a list where all similar adjacent elements have been reduced to a single element,
#  so [1,2,3,3] returns [1,2,3]


# def similar_adjacent_elements (repeated_elements_list : list ): 

#     if (len(repeated_elements_list) <= 1 ):
#         return repeated_elements_list
    
#     head = 0 
#     tail = 1
#     repeated_elements_list.sort() # sorting 
#     list_size = len(repeated_elements_list)
#     while ( tail < list_size  ): # while this value exists
#         if ( repeated_elements_list[head] == repeated_elements_list[tail] ):
#             del repeated_elements_list[head]
#             list_size = len(repeated_elements_list) # refresh size value after delete
#             # if element deleted, that's means the array index shiftedd to the left so no head or tail index will be changed 
#             # it will already point to a new elemnts, the head to the old tail value and the tail will point to a new value  
#         else :
#             # if both values not the same go to the neext 2 vales 
#             head = head + 1
#             tail = tail + 1
    
#     return repeated_elements_list

# print ( similar_adjacent_elements([8,8,3,1,1,9,50,5,6,1,1,1,5,8,8]) );

# ==================================================================================

# 2 - Dividing a string into two halves

# def divid_string (my_string1 : str , my_string2 : str):
#     string_size1 = len(my_string1)
#     string_size2 = len(my_string2)
#     if ( string_size1 <= 1 and string_size2 <= 1):  
#         return my_string1+my_string2
    
#     head_string1 = tail_string1= head_string2= tail_string2 = ""
    
#     if (string_size1 % 2 == 0 ): # even number
#         head_string1 = my_string1[0: int(string_size1 / 2)]
#         tail_string1 = my_string1[int(string_size1 / 2) :]
#     else:
#         head_string1 = my_string1[0: int(string_size1 / 2) + 1]
#         tail_string1 = my_string1[int(string_size1 / 2) + 1 :]

#     if ( string_size2 % 2 == 0  ):
#         head_string2 = my_string2[0: int(string_size2 / 2)]
#         tail_string2 = my_string2[int(string_size2 / 2) :]
#     else:
#         head_string2 = my_string2[0: int(string_size2 / 2) + 1]
#         tail_string2 = my_string2[int(string_size2 / 2) + 1 :]    

#     return head_string1+head_string2+ " "+tail_string1+tail_string2 

# print ( divid_string("Ahmed","Zein") ) # AhmZe, edin

# =============================================================================================

# 3-  Write a Python function that takes a sequence of numbers and determines
# whether all the numbers are different from each other.


# def is_different_numbers (my_list : list):
    
#     # Assuming the list is not sorted.
    
#     if ( len(my_list) <= 1 ):
#         return True
#     #temp = { "2" : 1  , "3" : 1  }
#     temp = {}
#     for i in my_list:
#         if str(i) in temp: # Check if the number exists as a key in the temp
#             return False
#         else:
#             temp[str(i)] = 1 
#     return True
        
# print (is_different_numbers( [5,5,1,1,9] ) )


# =============================================================================================

# 4-  Given unordered list, sort it using algorithm bubble sort

# def bubble_sort(arr):
#     n = len(arr)
#     # Traverse through all array elements
#     for i in range(n):
#         # Last i elements are already in place
#         for j in range(0, n-i-1):
#             # Traverse the array from 0 to n-i-1
#             # Swap if the element found is greater than the next element
#             if arr[j] > arr[j+1] :
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

# # Example usage:
# my_list = [64, 34, 25, 12, 22, 11, 90]
# bubble_sort(my_list)
# print(my_list) # Output: [11, 12, 22, 25, 34, 64, 90]

# =============================================================================================

# import random

# def guessing_game():
#     secret_number = random.randint(1, 100)
#     num_tries = 10
#     guessed_numbers = set()

#     while num_tries > 0:
#         user_input = input(f"Guess the secret number (between 1 and 100). You have {num_tries} tries left: ")
#         try:
#             guess = int(user_input)
#         except ValueError:
#             print("Invalid input. Please enter an integer.")
#             continue
        
#         if guess < 1 or guess > 100:
#             print("Your guess is out of range (1-100).")
#             continue
        
#         if guess in guessed_numbers:
#             print("You already guessed this number.")
#             continue
        
#         guessed_numbers.add(guess)
#         num_tries -= 1
        
#         if guess == secret_number:
#             print("Congratulations! You guessed the secret number!")
#             play_again = input("Do you want to play again? (y/n) ")
#             if play_again.lower() == 'y':
#                 guessing_game()
#             else:
#                 print("Thanks for playing!")
#             return
        
#         elif guess < secret_number:
#             print("Your guess is too low.")
#         else:
#             print("Your guess is too high.")
    
#     print(f"Sorry, you have run out of tries. The secret number was {secret_number}.")
#     play_again = input("Do you want to play again? (y/n) ")
#     if play_again.lower() == 'y':
#         guessing_game()
#     else:
#         print("Thanks for playing!")

# # Example usage:
# guessing_game()
