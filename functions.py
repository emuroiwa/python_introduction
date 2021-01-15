def add_two_numbers (num_one, num_two):
    total = num_one + num_two
    return total
total = add_two_numbers(32,34)
print(total)


print('Function with Default Parameters-----------------------')

def generate_full_name (first_name = 'Asabeneh', last_name = 'Yetayeh'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('David','Smith'))