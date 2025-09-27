"""
Homework: Python Refresher - Basics up to Loops

Rules:
- Write plain Python (no imports, no functions)
- Fill in the code after each task
- Keep variable names in snake_case (e.g. my_variable)

Tips:
- Run the script often to test your work
- The usual shortcut to run a Python script in VSC is "Ctrl - F5"
- If this doesn't work, you can assign your own shortcut as follows:
- Press Ctrl + K Ctrl + S to open keyboard shortcuts
- Search for "Python: Run Python File in Terminal"
- Set Keybinding to your preferred key (e.g. "Ctrl + Shift + R")
"""

# 1) Setup basic variables
# Create variables for: current_date (string like "2025-09-17"), work_hours (float), records_count (int), is_remote_day (bool)

# 2) Casting and simple arithmetic
# Create a float pending_ratio by dividing a whole number by another (e.g., 7/3)
# Cast it to int and print both values

# 3) Strings
# Create customer_name = "Alex Morgan"
# Print a slice containing the surname only (no spaces)
# Print the name in uppercase
# Print: "<customer_name> — processed on <current_date>"

# 4) Collections — Lists
# Create a list amounts with at least 3 integers
# Append one more amount
# Using a for-loop, print each amount and, on the same line, whether it is "even" or "odd"
# Calculate total amount (sum of the amounts list)

# 6) Collections — Sets
# Create a set seen_categories from a list (e.g., ["A", "B", "A", "C"])
# Print the set and its length
# Convert the set to a list and print any one element by index

# 7) Collections — Dictionaries
# Create a dictionary record with keys: id (string), value (int), meta (a nested dict with keys prio (int) and channel (string))
# Print the nested prio value
# If value is below a threshold (choose one), print "Flag: low value", elif equal to threshold print "Boundary", else print "OK"

# 8) Combined conditionals
# Using variables from above, print "Review needed" if work_hours > 6 and is_remote_day, or records_count > 10. Otherwise print "No review"

# 10) For loops
# For each item in amounts, print the index and the amount on one line

# References vs Copy
# Create a list employees = ["Anna", "Bob", "Chris"]
# Create a new list team that has equal values as employees
# Remove the first element from team and append a new element, while employees shouldn't change
# Print team and employees
