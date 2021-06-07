def swapcase(str_input):
    uppercase_chars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    lowercase_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    output_str = ""
    for char in  str_input:
        if char in uppercase_chars:
            output_str = output_str + char.lower()
        elif char in lowercase_chars:
            output_str = output_str + char.upper()
        else:
            output_str = output_str + char
    
    return output_str


convert = "helLo WoRLd"
print(convert)
print(swapcase(convert))