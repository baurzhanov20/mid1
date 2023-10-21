# User interface
print("Please chose the task you want to perform:")
print("1. Enter items")
print("2. Exit")

while True:
    try:
        choice = int(input("User Input: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if choice == 1:
        items = input("Please enter items separated by comma\n").split(',')
        unique_items = set()
        non_unique_items = {}

        for item in items:
            item = item.strip()
            if item in non_unique_items:
                non_unique_items[item] += 1
            else:
                non_unique_items[item] = 1
            unique_items.add(item)

        non_unique_items = tuple((item, count) for item, count in non_unique_items.items() if count > 1)

        print("Items are saved")
        print("Unique items:", unique_items)
        print("Not unique items:", non_unique_items)

    elif choice == 2:
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter a valid option.")


