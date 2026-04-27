# ======================================
# Enums Exercise
# ======================================

from dataclasses import dataclass
from enum import Enum
from typing import List
import sys


class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"


@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: OperatingSystem


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem


# Predefined laptops
laptops: List[Laptop] = [
    Laptop(1, "Dell", "XPS", 13, OperatingSystem.ARCH),
    Laptop(2, "Dell", "XPS", 15, OperatingSystem.UBUNTU),
    Laptop(3, "Dell", "XPS", 15, OperatingSystem.UBUNTU),
    Laptop(4, "Apple", "MacBook", 13, OperatingSystem.MACOS),
]


# Helper: convert string → enum safely
def parse_operating_system(os_str: str) -> OperatingSystem:
    for os in OperatingSystem:
        if os.value.lower() == os_str.lower():
            return os
    print(f"Error: Invalid operating system '{os_str}'", file=sys.stderr)
    sys.exit(1)


# Read user input
name = input("Enter name: ")

try:
    age = int(input("Enter age: "))
except ValueError:
    print("Error: Age must be an integer", file=sys.stderr)
    sys.exit(1)

os_input = input("Enter preferred operating system (macOS, Ubuntu, Arch Linux): ")
preferred_os = parse_operating_system(os_input)


person = Person(name=name, age=age, preferred_operating_system=preferred_os)


# Count matching laptops
matching = [l for l in laptops if l.operating_system == person.preferred_operating_system]

print(f"\nThere are {len(matching)} laptops available for {person.preferred_operating_system.value}.")


# Find most available OS
os_counts = {}
for laptop in laptops:
    os_counts[laptop.operating_system] = os_counts.get(laptop.operating_system, 0) + 1

best_os = max(os_counts, key=os_counts.get)

if best_os != person.preferred_operating_system:
    print(
        f"If you're flexible, choosing {best_os.value} increases your chances "
        f"({os_counts[best_os]} laptops available)."
    )