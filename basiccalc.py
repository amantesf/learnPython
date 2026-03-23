#define the functions needed: add, sub, multi, div
#print options
#ask for values
#call the functions
#add while loop to continue until the user wants to exit
def add(x, y):
    answer = x + y
    print(str(x) + " + " + str(y) + " = " + str(answer) + "\n")
def sub(x, y):
    answer = x - y
    print(str(x) + " - " + str(y) + " = " + str(answer) + "\n")
def multi(x, y):
    answer = x * y
    print(str(x) + " * " + str(y) + " = " + str(answer) + "\n")
def div(x, y):
    answer = x / y
    print(str(x) + " / " + str(y) + " = " + str(answer) + "\n")
while True:
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")
    choice = input("Enter choice(1, 2, 3, 4, 5): ")
    if choice == '1':
        print("You chose addition.")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        add(num1, num2)
    elif choice == '2':
        print("You chose subtraction.")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter first number: "))
        sub(num1, num2)
    elif choice == '3':
        print("You chose multiplication.")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter first number: "))
        multi(num1, num2)
    elif choice == '4':
        print("You chose division.")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter first number: "))
        div(num1, num2)
    elif choice == '5':
        print("Exiting the program.")
        quit()
    
    
    