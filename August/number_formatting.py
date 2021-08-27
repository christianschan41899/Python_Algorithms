#Count up from number in decimal, octal, hex, and binary.
#[2:] removes the prefix Python ascribes to each number to identify them as octal, hex, or binary.
def count_up(target_num):
   for num in range(target_num):
        print(f"{num} {oct(num)[2:]} {hex(num)[2:]} {bin(num)[2:]}")

#Check if input for position was an integer
def int_check(user_input):
    #Attempt conversion to int
    try:
        convert_input = int(user_input)
        return convert_input
    #If it fails (ValueError), display message and prompt another input
    except ValueError:
        print("Input was not an integer. Try again.")
        target_input = input("Count up to number ... ")
        #Check if this new input is an int through a recursive call
        return int_check(target_input)

target_input = input("Count up to number ... ")
target_num = int_check(target_input)
count_up(target_num)


