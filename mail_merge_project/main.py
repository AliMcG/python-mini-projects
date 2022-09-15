PLACEHOLDER = "[name]"
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# opens the txt.file of names
with open("./Input/Names/invited_names.txt") as file:
    # .readlines() extracts the lines from the text (the names) into a list
    # But .readlines adds a line break (\n) to end of each name
    names_with_space = file.readlines()
    # .strip() removes the empty space at the end or beginning of a string
    names = [ line.strip() for line in names_with_space] 
    print(names)

# opens the txt.file with the letter to edit
with open("./Input/Letters/starting_letter.txt") as file:
    # cretaes a list of the text lines from the file
    lines = file.readlines()
    
    # Uses the names list for the 1st function to loop through
    for name in names:
        # new_letter = letter_contents.replace(PLACEHOLDER, name)
        # print(new_letter)
        # Takes the [0] line from the text .replace( thing-to-replace, replacedWith)
        # Here with a new name
        new_line = lines[0].replace(f"[name]", str(name))
        # or each new line .write writes the new line
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as new_file:
            new_file.write(new_line)
            # Use the range function to loop throught the maining lines from orginal txt.file 
            # and .writes them to the new txt.file
            for x in range(1, len(lines)):
                new_file.write(lines[x])
    

