# ==============================
# Classes and Objects Exercise
# ==============================

class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system


imran = Person("Imran", 22, "Ubuntu")
eliza = Person("Eliza", 34, "Arch Linux")


# Access valid properties
print(imran.name)
print(eliza.name)


# This line is intentionally wrong (mypy should catch it)
# print(imran.address)


def is_adult(person: Person) -> bool:
    return person.age >= 18


print(is_adult(imran))
print(is_adult(eliza))


# Function with an error (for mypy to detect)
def get_address(person: Person) -> str:
    return person.address   # This property does NOT exist