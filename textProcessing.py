#Develop a script to extract specific information from a formatted text. The text contains data entries delimited by semicolons and 
# formatted as 'Key: Value'. Extract the value corresponding to a specific key.

#Code Example:

import re

#text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"
# Extract the Occupation from the text
#Expected Outcome:
#Correctly identify and categorize valid and invalid URLs from the list.
#Use regex to validate the format of each URL.

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"
occupation = re.search(r'Occupation: ([^;]+)', text).group(1)
print(occupation)