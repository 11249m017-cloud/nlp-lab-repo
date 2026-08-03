import re

# Input text
text = input("Enter text: ")

# Regular expression pattern for email ID
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

# Find email ID
email = re.findall(pattern, text)

# Display result
print("Extracted Email ID:")

for e in email:
    print(e)