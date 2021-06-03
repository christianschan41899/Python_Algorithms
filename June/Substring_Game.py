def Substring_game(string):
    #Generate a dictionary with Keys as substrings and their Values as occurences
    all_substrings = {} #Empty dict
    length = len(string) #string length
    for i in range(0, length):
        for j in range(i+1, length+1):
            substring = string[i:j]
            #Debug: print(substring)
            #Check for repeat keys. If so, increment. If not, add.
            if substring in all_substrings:
                all_substrings[substring] += 1
            else:
                all_substrings[substring] = 1
    #Debug: print(all_substrings)
    #Go through dictionary
    consonant_score = 0
    vowel_score = 0
    for key in all_substrings:
        #If starts with vowel, increment vowel frequency
        if(key[0] == "a" or key[0] == "A" or key[0] == "e" or key[0] == "E" or key[0] == "i" or key[0] == "I" or key[0] == "o" or key[0] == "O" or key[0] == "u" or key[0] == "U"):
            vowel_score = vowel_score + all_substrings[key]
        #else means it's a consonant
        else:
            consonant_score = consonant_score + all_substrings[key]
    
    #Determine winner
    if(consonant_score > vowel_score):
        print(f"Stuart {consonant_score}")
    elif(consonant_score < vowel_score):
        print(f"Kevin {vowel_score}")
    else:
        print("Draw")
    

Substring_game("anana")