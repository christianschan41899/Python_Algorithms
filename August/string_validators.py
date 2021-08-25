# Output if string contains characters that are uppercase, lowercase, and/or numbers
# And if string is alphanumeric and/or alphabetic
def string_contains(input_str):
    is_alphanumeric = input_str.isalnum()
    is_alphabetic = input_str.isalpha()
    contains_lower = False
    contains_upper = False
    contains_num = False
    #Iterates through each character in the string to see if it is a number, lowercase, or uppercase and flips the appropriate variable to True.
    for char in input_str:
        if char.isdigit():
            contains_num = True
        elif char.islower():
            contains_lower = True
        elif char.isupper():
            contains_upper = True
    #Conditional strings formatted to print a specific response depending on if the boolean variables above are True or not.
    print("The string {alphanumeric} alphanumeric".format(alphanumeric="is" if is_alphanumeric else "is not" ))
    print("The string {alphabetic} alphabetic".format(alphabetic="is" if is_alphabetic else "is not" ))
    print("The string {lower} contain lowercase characters".format(lower="does" if contains_lower else "does not" ))
    print("The string {upper} contain uppercase characters".format(upper="does" if contains_upper else "does not" ))
    print("The string {num} contain numbers".format(num="does" if contains_num else "does not" ))

str = input("Type a string: ")
string_contains(str)
