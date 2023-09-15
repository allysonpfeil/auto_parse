import os

# Set the directory you want to search
directory = "//path//"

# Set the keywords you want to search for
keywords = ["insert your keywords here"]

# Iterate through the files in the directory
for filename in os.listdir(directory):
    # Open the file and read through it line by line
    with open(os.path.join(directory, filename)) as file:
        keyword_list = []
        for line_number, line in enumerate(file):
            # Check if any of the keywords are in the line
            for keyword in keywords:
                if keyword in line:
                    # If a keyword is found, add the keyword to the list
                    keyword_list.append(keyword)
        # If the keyword list is not empty, print the list
        if keyword_list:
            print(f"Keywords found in {filename}: {keyword_list}")
        else:
            # If none of the keywords are found, print a message
            print(f"None of the keywords were found in {filename}")
#END
