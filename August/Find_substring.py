#Take an input string and substring and return how many times that substring occurs within the string

def search_substring(input_str, substring):
    # The string will be searched for in chunks of length equal to the substring's length
    # To do this, start by setting an initial idx of 0 and end idx =equal to the length of the substring 
    i = len(substring)
    initial_idx = 0
    # Initialize value of number of substrings found. Will be modified below and returned after.
    substrings_found = 0
    # Loop until the end index (i) reaches outside the indeces of the input string (until i < len(input_str) is false)
    while i <= len(input_str):
        # Save the string between our initial idx and end idx  
        test_substring = input_str[initial_idx:i]
        # Test this saved substring against what we are search for. If it matches, increase the substrings found counter by 1
        if test_substring == substring :
            substrings_found = substrings_found + 1
        #Incerement our search indeces by 1 so we search the rest of the string and so the while loop has an end point.
        initial_idx = initial_idx + 1
        i = i + 1
    return substrings_found

input_string = input("Type a string: ")
input_substring = input("Type a string you wish to search for: ")
print(f"{input_substring} occured {search_substring(input_string, input_substring)} times in {input_string}")