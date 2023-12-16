decimal_number = 159
octal_representation = oct(decimal_number)

octal_representation_without_prefix = octal_representation[2:]

print(f"The octal representation of {decimal_number} is: {octal_representation_without_prefix}")

# what i did to remove the "0o" prefix indicates that the number was to use string slicing