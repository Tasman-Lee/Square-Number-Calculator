# What does this program does:
# - Identify and remove duplicating numbers in an array
# - Filter out non-square numbers in an array
# - Calculate the sum

#main function
if __name__ == "__main__":
    #variables to accept return value from the function
    unique_numbers, sum_squared_numbers = remove_duplicates_and_sum_squared(numbers)

    #if statement to print output
    if not unique_numbers:
        print("No unique numbers found.")
    else:
        print("Unique numbers:", unique_numbers)
        print("Sum of squared numbers:", sum_squared_numbers)

    #end of if statement

#function to check if the numbers are squared numbers
def is_squared_number(num):
    root = int(num ** 0.5)

    #return values
    return root * root == num

#function to remove duplication, and find sum
def remove_duplicates_and_sum_squared(numbers):
    
    #variables to accept array of numbers, set(0 to remove duplicates
    unique_numbers = set()

    #variables to accept sum
    sum_squared_numbers = 0

    #for loop to find sum
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.add(num)
            if is_squared_number(num):
                sum_squared_numbers += num

    #return values
    return list(unique_numbers), sum_squared_numbers


