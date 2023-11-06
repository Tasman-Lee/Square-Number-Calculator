# What does this program does:
# - Identify and remove duplicating numbers in an array
# - Filter out non-square numbers in an array
# - Calculate the sum

def is_squared_number(num):
    root = int(num ** 0.5)
    return root * root == num

def remove_duplicates_and_sum_squared(numbers):
    unique_numbers = set()
    sum_squared_numbers = 0

    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.add(num)
            if is_squared_number(num):
                sum_squared_numbers += num

    return list(unique_numbers), sum_squared_numbers

if __name__ == "__main__":
    numbers = [4, 7, 9, 9, 16, 25, 36, 36, 49]  # Replace with your list of numbers

    unique_numbers, sum_squared_numbers = remove_duplicates_and_sum_squared(numbers)

    if not unique_numbers:
        print("No unique numbers found.")
    else:
        print("Unique numbers:", unique_numbers)
        print("Sum of squared numbers:", sum_squared_numbers)
