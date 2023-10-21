try:
    name = input("Enter your name please: ")
    salary = int(input("Enter your desired salary level: "))

    tax_level = salary * 0.2

    print(f"{name}, the tax level you will pay with the salary {salary} is {tax_level}")
except ValueError:
    print("Please enter your desired salary as a digit.")