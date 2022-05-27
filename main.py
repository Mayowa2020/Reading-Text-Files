import string


# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}



def read_file_content(filename):
    # open the file and read the content
    with open(filename) as file:
        contents = file.read()
        # print contents of the file
    return contents

# Calling the function
print(read_file_content("hello.txt"))

print()

def count_words():  
    text = read_file_content("story.txt")
    
      # Create an empty dictionary   
    di = {}

    # Remove punctuations from the text
    new_text = text.translate(str.maketrans("", "", string.punctuation))

    # Remove the leading spaces
    new_text = new_text.strip()

    # Convert the characters to lowercase to avoid mismatch
    new_text = new_text.lower()

    # Split the text into words
    words = new_text.split()
    
    # Iterate over each word in the text
    for word in words:
        # Check if the word is already in the dictinary
        if word in di:
            # Increment count of word by 1
            di[word] += 1
        else:
            # Add the word to dictionary with count 1
            di[word] = 1
    # Print the contents of the dictionary
    print(di) 
           
count_words()     
 
