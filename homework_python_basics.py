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

current_date = "2025-09-26"   # string like "2025-09-17"
work_hours = 7.30            # float
records_count = 9             # int
is_remote_day = True          # bool
print("#1:", current_date, work_hours, records_count, is_remote_day)

# 2) Casting and simple arithmetic
# Create a float pending_ratio by dividing a whole number by another (e.g., 7/3)
# Cast it to int and print both values

pending_ratio = 7 / 3
pending_ratio_int = int(pending_ratio)
print("float: ", pending_ratio, "int: ", pending_ratio_int)

# 3) Strings
# Create customer_name = "Alex Morgan"
# Print a slice containing the surname only (no spaces)
# Print the name in uppercase
# Print: "<customer_name> — processed on <current_date>"

customer_name = "Alex Morgan"
surname_only = customer_name[5:]
print("#3 surname:", surname_only)
print("#3 upper:", customer_name.upper())
print("#3 log:", f"{customer_name} — processed on {current_date}")



# 4) Collections — Lists
# Create a list amounts with at least 3 integers
# Append one more amount
# Using a for-loop, print each amount and, on the same line, whether it is "even" or "odd"
# Calculate total amount (sum of the amounts list)

amounts = [120, 75, 33]
amounts.append(42)
for a in amounts:
    kind = "even" if a % 2 == 0 else "odd"
    print(f"item: {a} - {kind}")
total_amount = sum(amounts)
print("total:", total_amount)

# 6) Collections — Sets   
# Create a set seen_categories from a list (e.g., ["A", "B", "A", "C"])
# Print the set and its length                                                              
# Convert the set to a list and print any one element by index

categories_list = ["A", "B", "A", "C", "B"]
seen_categories = set(categories_list)
print("set:", seen_categories, "length:", len(seen_categories))
seen_categories_list = list(seen_categories)
print("any element:", seen_categories_list[0])


# 7) Collections — Dictionaries
# Print the nested prio value
# Cr l;,,,]=l[.peate a dictionary record with keys: id (string), value (int), meta (a nested dict with keys prio (int) and channel (string))
# If value is below a threshold (choose one), print "Flag: low value", elif equal to threshold print "Boundary", else print "OK"

record = {
    "id": "rec-001",
    "value": 50,
    "meta": {"prio": 2, "channel": "email"}
}
print("prio:", record["meta"]["prio"])
threshold = 50
if record["value"] < threshold:
    print("status: Flag: low value")
elif record["value"] == threshold:
    print("status: Boundary")
else:
    print("status: OK")


# 8) Combined conditionals
# Using variables from above, print "Review needed" if work_hours > 6 and is_remote_day, or records_count > 10. Otherwise print "No review"

if (work_hours > 6 and is_remote_day) or (records_count > 10):
    print("Review needed")
else:
    print("No review")

# 10) For loops
# For each item in amounts, print the index and the amount on one line

for idx, amount in enumerate(amounts):
    print("idx:", idx, "amount:", amount)



# References vs Copy
# Create a list employees = ["Anna", "Bob", "Chris"]
# Create a new list team that has equal values as employees
# Remove the first element from team and append a new element, while employees shouldn't change
# Print team and employees

employees = ["Anna", "Bob", "Chris"]
team = employees.copy()  # copy
team.pop(0)            # remove first element
team.append("Dana")    # add new element
print("team:", team)
print("employees:", employees)