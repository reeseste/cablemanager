from box import Box
from cabletype import CableType
from cable import Cable
from typing import List


class Storage:
    def __init__(self, inventory: List[Box] = None) -> None:
        self.inventory: List[Box] = inventory if inventory is not None else []

    def __str__(self) -> str:
        return str([str(box) for box in self.inventory])

    def get_inventory(self) -> list:
        return self.inventory

    def add_box(self):
        name = input("Please enter box name: ")
        location = input("Please enter box location: ")
        box = Box(name, location)
        self.inventory.append(box)


    def add_cable(self):
        cable_type = int(input(f"What type of cable would you like to add (input the number)? \n Options: {CableType._member_map_} "))
        cable_color = input(f"What is the color of this cable? ")
        cable_length = float(input("What is the cable's length (in ft)?: "))
        cable_location = input(f"What the box name for this cable? ")

        new_cable = Cable(type=cable_type, color=cable_color, length=cable_length, location=cable_location)

        print(f"{cable_location = }, {type(cable_location)}")
        self.put_cable_in_box(desired_box=cable_location, cable=new_cable)

        print(self)


    def put_cable_in_box(self, desired_box: str, cable: Cable):
        for box in self.inventory:
            if box.name.lower() == desired_box.lower():
                print(str(box))
                box.contents.append(cable)
                print(f"{cable = } has been placed into box {box.name}")
                return
        else:
            print("Couldn't find the box you dummy, try again")
