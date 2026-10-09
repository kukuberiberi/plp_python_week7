"""
Part A: List Warmup
Demonstrates index access, append, remove, and len().
"""

# 1. Create a list called fruits containing four fruits
fruits = ["lemon", "banana", "guava", "mango"]

# 2. Print the first and the last item using indexes
print("First item:", fruits[0])
print("Last item:", fruits[-1])

# 3. .append() a fifth fruit, then print the whole list
fruits.append("grape")
print("After append:", fruits)

# 4. .remove() one fruit, then print the list again
fruits.remove("banana")
print("After remove:", fruits)

# 5. Print how many fruits remain using len()
print("Remaining count:", len(fruits))