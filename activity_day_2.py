# 1
def max_num(a, b, c):
    return max(max(a, b), c)

result = max_num(55, 15, 77)
print("The max number between the three numbers is:", result)

# 2
def mult_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


my_list_numbers = [1, 2, 3, 4, 5, 6]
result = mult_list(my_list_numbers)
print("The result of multiplying all the numbers in my list is:", result)

# 3 - had to search this up - slicing the string is very interesting!
def rev_string(input_string):
    return input_string[::-1]

original_string = "I love Python!"
reversed_string = rev_string(original_string)
print("The original string is:", original_string)
print("The reversed string would be:", reversed_string)

#4
def num_within(number, start_range, end_range):
    return start_range <= number <= end_range


number = 55
start_range = 15
end_range = 77
if num_within(number, start_range, end_range):
    print(f"{number} falls within the range [{start_range}, {end_range}]")
    print("True")
else:
    print(f"{number} does not fall within the range [{start_range}, {end_range}]")
    print("False")

#5 - had to search this up as the solution code provided did not work - very interesting though!
def pascal(n):
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(previous_row[j - 1] + previous_row[j])
            row.append(1)

        print(row)
        previous_row = row

n = 6
pascal(n)


