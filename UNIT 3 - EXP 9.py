# Assignment 3:
# Find and extract email addresses from a given text using Regular Expressions.

# Step 1: Import the regular expression module
import re

# Step 2: Store the text in a variable
text = """
Hello students!
For any queries, contact abc@gmail.com or teacher123@college.edu.
You can also contact support@yahoo.com.
"""

# Step 3: Create a regular expression pattern for email addresses
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Step 4: Find all email addresses in the text
emails = re.findall(email_pattern, text)

# Step 5: Display a heading
print("Email addresses found:")

# Step 6: Display each email address
for email in emails:
    print(email)
