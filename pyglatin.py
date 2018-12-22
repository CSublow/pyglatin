#Introduction
print("Pyglatin Translator\n")
print("Pyglatin is an argot which rearranges words to conceal their meaning from people unfamiliar with the rules.\n")
print("You convert a word to pig latin by transferring the initial consonant or consonant cluster of the word to the end of the word with -ay appended to the end.\n")
print("If the word starts with a vowel (including y), append -yay to the end. For example, \"pig\" would become igpay (taking the 'p' and 'ay' to create a suffix\n\n")

# Create a list of consonants and vowels
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
vowels = ["a", "e", "i", "o", "u"]

# The suffixes to be used
c_suffix = "ay"
v_suffix = "yay"

# Counter to use to make sure that a word is always outputted, including when the word has no vowels
counter = 0

# Variable used for while loop, kept true as long as the user wants to translate words
translate = True

while translate == True:
    # Get user input and make sure it is lower case so it can be compared across lower and upper cases
    user_input = input("Please enter your word to translate to Pyglatin: ").lower()

    # Turn the inputted word into a list
    list_word = list(user_input)
    # Python works on working_list_word to create the pyglatin word
    # This keeps the original list intact so python can loop through it correctly
    working_list_word = list(list_word)
    # later_vowel represents if a vowel is found as the 2nd or above character of a word
    later_vowel = False

    # For each character in the inputted word
    for x in list_word:
        # If a vowel is found first, we don't need to worry about any consonants
        # So we just convert the word into a string, add the suffix and break the loop
        if x in vowels:
            # If the vowel is found AFTER a consonant, we need to add the consonant suffix
            if later_vowel == True:
                # Convert the list into a string and add the suffix
                pyg_word = ''.join(working_list_word).capitalize() + c_suffix
                break
            # If the vowel is the first character found, we want to add the vowel suffix
            else:
                # Convert the list into a string and add the suffix
                pyg_word = ''.join(working_list_word).capitalize() + v_suffix
                break
        # If a consonant is found
        elif x in consonants:
            # Append the consonant to the end of the word
            working_list_word.append(working_list_word[0])
            # Remove that consonant from the beginning of the word
            working_list_word.pop(0)
            counter += 1
            # Once the counter is the same number as the length of the word, this means that no vowels are in the word
            # So format the word and output it
            if counter == len(working_list_word):
                # Convert the list into a string and add the suffix
                pyg_word = ''.join(working_list_word).capitalize() + c_suffix
                break
            # If we have found at least one consonant, any vowel we find must be either the 2nd or later character
            later_vowel = True

    # Print the word that has been generated
    print(pyg_word)

    # Exit the loop unless the user wants to translate another word
    print("Do you want to translate another word?")
    # Initialise yes/no response input
    response = ''
    # While the user doesn't type either yes or no...
    while response.lower() not in {"yes", "no"}:
        response = input("Please enter yes or no: ")
    # If the user types 'no'...
    if response.lower() == "no":
        print("Exiting program...")
        # Break out of the loop
        translate = False
    # If the user types yes, the while loop will go back to the beginning


