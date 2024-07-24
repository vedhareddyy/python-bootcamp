#find even or add
# Function to check if the number is even or odd
'''def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Input: Enter a number
num = int(input("Enter a number: "))

# Output: Display whether the number is even or odd
result = check_even_odd(num)
print(f"The number {num} is {result}.")'''
  
       

#find greatest of 3
# Function to find the greatest of three numbers
'''def find_greatest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Input: Enter three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Output: Display the greatest number
greatest = find_greatest(num1, num2, num3)
print(f"The greatest number among {num1}, {num2}, and {num3} is {greatest}.")'''



#find sum of all elements in array
# Function to find the sum of all elements in an array
'''def array_sum(arr):
    total = 0
    for element in arr:
        total += element
    return total

# Input: Enter the elements of the array
# Example: [1, 2, 3, 4, 5]
array = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

# Output: Display the sum of all elements in the array
sum_of_elements = array_sum(array)
print(f"The sum of all elements in the array is {sum_of_elements}.")'''



#find peak element in array
'''def find_peak(arr):
    n = len(arr)
    
    # If there's only one element, it's the peak
    if n == 1:
        return arr[0]
    
    # Check if the first element is a peak
    if arr[0] >= arr[1]:
        return arr[0]
    
    # Check if the last element is a peak
    if arr[n - 1] >= arr[n - 2]:
        return arr[n - 1]
    
    # Check for peak in the rest of the array
    for i in range(1, n - 1):
        if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
            return arr[i]
    
    return None

# Input: Enter the elements of the array
array = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

# Output: Display the peak element
peak = find_peak(array)
if peak is not None:
    print(f"The peak element in the array is {peak}.")
else:
    print("No peak element found.")'''



#find max element in an array
# Function to find the maximum element in an array
'''def find_max(arr):
    if not arr:
        return None  # Return None if the array is empty
    max_element = arr[0]
    for element in arr:
        if element > max_element:
            max_element = element
    return max_element

# Input: Enter the elements of the array
array = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

# Output: Display the maximum element
max_element = find_max(array)
if max_element is not None:
    print(f"The maximum element in the array is {max_element}.")
else:
    print("The array is empty.")'''



#find 2nd max element in an array
# Function to find the second maximum element in an array
'''def find_second_max(arr):
    if len(arr) < 2:
        return None  # Return None if there are fewer than 2 elements
    
    first_max = second_max = float('-inf')
    
    for element in arr:
        if element > first_max:
            second_max = first_max
            first_max = element
        elif element > second_max and element != first_max:
            second_max = element
    
    if second_max == float('-inf'):
        return None  # Return None if there is no second maximum
    return second_max

# Input: Enter the elements of the array
array = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

# Output: Display the second maximum element
second_max = find_second_max(array)
if second_max is not None:
    print(f"The second maximum element in the array is {second_max}.")
else:
    print("The array does not have a second maximum element.")'''



#reverse an array without using built in functions
# Function to reverse an array
'''def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        # Swap the elements at the start and end
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

# Input: Enter the elements of the array
array = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

# Reverse the array
reversed_array = reverse_array(array)

# Output: Display the reversed array
print("The reversed array is:", reversed_array)'''



#find the sum of squares of given number
# Function to find the sum of squares of digits of a given number
'''def sum_of_squares(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit * digit
        n = n // 10
    return total

# Input: Enter a number
num = int(input("Enter a number: "))

# Output: Display the sum of squares of the digits
result = sum_of_squares(num)
print(f"The sum of squares of the digits of {num} is {result}.")'''



#find sum of squares of even and odd digits
# Function to find the sum of squares of even and odd digits
'''def sum_of_squares_even_odd(n):
    even_sum = 0
    odd_sum = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            even_sum += digit * digit
        else:
            odd_sum += digit * digit
        n = n // 10
    return even_sum, odd_sum

# Input: Enter a number
num = int(input("Enter a number: "))

# Get the sum of squares of even and odd digits
even_sum, odd_sum = sum_of_squares_even_odd(num)

# Output: Display the sums
print(f"The sum of squares of the even digits of {num} is {even_sum}.")
print(f"The sum of squares of the odd digits of {num} is {odd_sum}.")'''



#check whether palindrome or not using loop
# Function to check if a string is a palindrome
def is_palindrome(s):
    # Remove any non-alphanumeric characters and convert to lowercase
    s = ''.join(filter(str.isalnum, s)).lower()
    
    start = 0
    end = len(s) - 1
    
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    
    return True

# Input: Enter a string
string = input("Enter a string: ")

# Output: Check and display if the string is a palindrome
if is_palindrome(string):
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')



#write a program to print 1st n phebinokic series