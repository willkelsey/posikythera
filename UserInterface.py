def view_system():
    print("I am viewing the whole system")


# will need some input for sure not sure of how that will go yet
def search_event():
    print("you are searching by astronomical event")


while 1:
    print("Welcome to Antikythera Simulation main menu")
    c = input("Press 1 to view the entire system, 2 to search for an astronomical event and 0 to exit\n")
    # typecast to int of base 10
    choice = int(c, 10)
    if choice == 1:
        view_system()
    elif choice == 2:
        search_event()
    elif choice == 0:
        break
    else:
        print("Invalid input")

