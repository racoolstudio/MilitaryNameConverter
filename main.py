# Import the pandas library for reading CSV files
import pandas

# Read the 'nato_phonetic_alphabet.csv' file into a DataFrame called 'database'
database = pandas.read_csv('nato_phonetic_alphabet.csv')

# Create a dictionary called 'database_dict' where the keys are letters and the values are codes,
# using a dictionary comprehension to iterate through the rows of the 'database' DataFrame
database_dict = {row.letter: row.code for (index, row) in database.iterrows()}

# Define a function called 'generator'
def generator():
    # Get user input and convert it to uppercase to ensure consistency
    user_input = input('Enter Your Name: ').upper()
    
    try:
        # Use list comprehension to look up the codes for each letter in the user's input
        result = [database_dict[n] for n in user_input]
    except KeyError:
        # If a letter is not found in the 'database_dict', handle the KeyError and print an error message
        print('Sorry, only letters in the alphabet please.')
        # Call the 'generator' function recursively to prompt the user for input again
        generator()
    else:
        # If there are no exceptions, print the result (list of codes)
         print("Your Military Name 🫡🪖 :\n", " ".join(result))


# Call the 'generator' function to start the process
generator()
