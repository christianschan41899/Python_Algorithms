import math

def mutate_string(string, position, character):
    str_list = list(string)
    str_list[position] = character
    new_str = ''.join(str_list)
    return new_str

#Check if input for position was an integer
def int_check(user_input):
    #Attempt conversion to int
    try:
        convert_input = int(user_input)
        return convert_input
    #If it fails (ValueError), display message and prompt another input
    except ValueError:
        print("Input was not an integer. Try again.")
        pos = input("Select postition in string, starting at 0 for first letter: ")
        #Check if this new input is an int through a recursive call
        return int_check(pos)

#inputs are treated as strings by default. No conversion necessary.
input_str = input("Enter String:")
input_pos = input("Select postition in string, starting at 0 for first letter: ")
position = int_check(input_pos)

# If this input exceeds the length of the string, the mutate function will go out of range
# Check if position is in range first
# Since position can be negative (going backwards) check absolute value
while abs(position) >= len(input_str):
    print(f"String position outside of range.")
    position = int_check(input(f"Enter a number less than {len(input_str)}: "))

replacement_char = input("Type character to replace")
# Characters are similar to strings of length 1.
# Since input is a string, the string must have a length of 1 to be analagous to a character
while len(replacement_char) != 1:
    print("Input must be a character. length of the input must be equal to 1.")
    replacement_char = input("Enter a new character: ")

final_str = mutate_string(input_str, position, replacement_char)
print(f"Your new string is {final_str}.")