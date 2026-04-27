# ==============================
# Dataclasses Exercise
# ==============================

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Person:
    name: str
    date_of_birth: date
    preferred_operating_system: str

    def is_adult(self) -> bool:
        today = date.today()

        age = today.year - self.date_of_birth.year

        # Adjust if birthday hasn't happened yet this year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1

        return age >= 18


# Create instances
imran = Person("Imran", date(2002, 5, 10), "Ubuntu")
eliza = Person("Eliza", date(1990, 3, 22), "Arch Linux")

# Test dataclass features
print(imran)
print(eliza)

# Equality check (should be True)
imran2 = Person("Imran", date(2002, 5, 10), "Ubuntu")
print("imran == imran2:", imran == imran2)

# Test method
print(imran.name, "is adult:", imran.is_adult())
print(eliza.name, "is adult:", eliza.is_adult())