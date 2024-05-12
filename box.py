from dataclasses import dataclass
from typing import List

from cable import Cable

class Box:

    def __init__(self, name: str, location: str, contents: List[Cable] = None):
        self.name = name
        self.location = location
        self.contents = contents if contents is not None else []

    def __str__(self) -> str:
        return f"Name: {self.name}, Location: {self.location} \
          Contents: {self.contents}"

    
    def show_box(self):
        print(self.contents)
