"""
Part C: List Report
Generates numbered lists, condition counts, and identifies the longest name.
"""

items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

print("--- Numbered Items ---")
# Loop through the list and print each item numbered
for index, item in enumerate(items, start=1):
    print(f"{index}. {item}")

# Count how many item names have more than 4 letters
count_long_names = 0
for item in items:
    if len(item) > 4:
        count_long_names += 1

print(f"\nItems with more than 4 letters: {count_long_names}")

# Find and print the longest item name using loop comparison
longest_item = items[0]
for item in items:
    if len(item) > len(longest_item):
        longest_item = item

print(f"The longest item name is: {longest_item}")