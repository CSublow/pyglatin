# Get user input and make sure it is lower case so it can be compared across lower and upper cases
user_input = input("Please enter your word: ").lower()

# Create a list of consonants and vowels
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
vowels = ["a", "e", "i", "o", "u"]

# The suffixes to be used
c_suffix = "ay"
v_suffix = "yay"

# Counter to use to make sure that a word is always outputted
counter = 0

# Turn the inputted word into a list
list_word = list(user_input)
working_list_word = list(list_word)
later_vowel = False

# For each character in the inputted word
for x in list_word:
    # If a vowel is found first, we don't need to worry about any consonants. So we just convert the word into a string, add the suffix and print it, breaking from the loop
    if x in vowels:
        # If the vowel is found AFTER a consonant, we need to add the consonant suffix
        if later_vowel == True:
            pyg_word = ''.join(working_list_word).capitalize() + c_suffix
            print(pyg_word)
            break
        # If the vowel is the first character found, we want to add the vowel suffix
        else:
            pyg_word = ''.join(working_list_word).capitalize() + v_suffix
            print(pyg_word)
            break
    # If a consonant is found
    elif x in consonants:
        working_list_word.append(working_list_word[0])
        working_list_word.pop(0)
        counter += 1
        # Once the counter is the same amount as the length of the word, this means that no vowels are in the word. So format the word and output it
        if counter == len(working_list_word):
            pyg_word = ''.join(working_list_word).capitalize() + c_suffix
            print(pyg_word)
            break
        later_vowel = True

# Exit the loop unless the user wants to translate another word
print("Do you want to translate another word?")
response = ''
while response.lower() not in {"yes", "no"}:
    response = input("Please enter yes or no: ")
if response.lower() == "no":
    print("Exiting program...")
    eng_pyg_translate = False


