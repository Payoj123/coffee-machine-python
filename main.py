print(" _  _   _  _  _  _              _     ___       _ ")      
print("/  / \ |_ |_ |_ |_   |\/|  /\  /  |_|  |  |\ | |_ | |" )  
print("\_ \_/ |  |  |_ |_   |  | /--\ \_ | | _|_ | \| |_ o o ") 
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    print("\nWelcome to the Coffee Shop")
    print("1. Display Menu")
    print("2. Make Coffee")
    print("3. Report")
    print("4. Exit")

    choice = input("Enter your choice:\n").lower()

    if choice == "1":
        print(menu.get_items())

    elif choice == "2":
        order_name = input("Enter the name of the drink:\n").lower()
        drink = menu.find_drink(order_name)

        if drink:  
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
                    print(f"Here is your {drink.name}. Thanks for ordering!")
                else:
                    print("Payment failed. Money refunded.")
            
        else:
            print("That drink is not available.")

    elif choice == "3":
        coffee_maker.report()
        money_machine.report()

    elif choice == "4":
        print("Thanks for purchasing!")
        print("Goodbye!")
        break

    elif choice == "close":  
        print("Machine under MAINTENANCE!")
        exit()

    else:
        print("Invalid choice. Please choose a valid option.")
