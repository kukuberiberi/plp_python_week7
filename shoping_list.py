"""
Part B: Shopping List Manager
Interactive manager supporting add, remove, show, and done operations.
"""

shopping_list = []

print("Welcome to the Shopping List Manager!")
print("Commands available: add, remove, show, done")

while True:
    choice = input("\nEnter command (add / remove / show / done): ").strip().lower()
    
    if choice == "add":
        item = input("Enter item to add: ").strip()
        if item:
            shopping_list.append(item)
            print(f"'{item}' added to the list.")
        else:
            print("Item cannot be empty.")
            
    elif choice == "remove":
        item = input("Enter item to remove: ").strip()
        # Safe check using 'in' to prevent ValueError crashes
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' removed from the list.")
        else:
            print("That item is not on your list.")
            
    elif choice == "show":
        print("\n--- Current Shopping List ---")
        if not shopping_list:
            print("Your list is currently empty.")
        else:
            for item in shopping_list:
                print(f"- {item}")
        print("-----------------------------")
        
    elif choice == "done":
        print("Goodbye! Thank you for using Shopping List Manager.")
        break
        
    else:
        print("Invalid command. Please choose: add, remove, show, or done.")