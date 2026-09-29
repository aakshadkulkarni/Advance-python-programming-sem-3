# Assignment 2:
# Read data from a CSV file and convert it into JSON format.
# Then write the JSON data into a .json output file.

# Step 1: Import the required modules
import csv
import json

# Step 2: Specify the name of the input CSV file
input_file = "students.csv"

# Step 3: Specify the name of the output JSON file
output_file = "students.json"

# Step 4: Open the CSV file in read mode
with open(input_file, "r", newline="") as csv_file:

    # Step 5: Read the CSV file using DictReader
    # Each row will be converted into a dictionary
    csv_reader = csv.DictReader(csv_file)

    # Step 6: Convert all CSV rows into a list
    data = list(csv_reader)

# Step 7: Open/create the JSON file in write mode
with open(output_file, "w") as json_file:

    # Step 8: Convert the Python list into JSON format
    # indent=4 makes the JSON file easy to read
    json.dump(data, json_file, indent=4)

# Step 9: Display a success message
print("CSV data successfully converted to JSON.")

# Step 10: Display the name of the output file
print("JSON file created:", output_file)
