from storage import Storage


def main():
    print("Welcome to CableManager")

    store1 = Storage()
    while True:
        item = input("\nWhat item would you like to add? \n Options: box, cable: ")
        match item.lower():
            case "box":
                store1.add_box()
                print("You have added your box to storage.")
                print(f"Your current storage is: {store1}")
            case "cable":
                store1.add_cable()

main()


    

# add cable hdmi green box1
    # lookup box1, if it does exist then good
    # else create box1? or prompt user that they need to create the box first
# search hdmi
    # Show all boxes with hdmi cables
    

# when they start the program, they should have the option to create a new db, or load a database (this should be a file Path)


def add_location():
    pass
def remove_item():
    pass
def give_info():
    pass
