# =========================
# Why We Use Types Exercise
# =========================

# Part 1 — Predictions

# Predict: double("22")
# I think it will return "2222" because multiplying a string repeats it.


# Part 2 — Code

def half(value):
    return value / 2 

def double(value):
    return value * 2 

def second(value):
    return value[1]


# Running examples

print("half(22):", half(22))

# These may cause errors, so you can comment/uncomment when testing
# print("half('hello'):", half("hello"))
# print("half('22'):", half("22"))

print("double(22):", double(22))
print("double('hello'):", double("hello"))
print("double('22'):", double("22"))

# print("second(22):", second(22))  # will error
# print("second(0x16):", second(0x16))  # will error
print("second('hello'):", second("hello"))
print("second('22'):", second("22"))


# Part 3 — Explanation

# double("22") returns "2222"
# because Python allows multiplying strings, which repeats them.


# Part 4 — Bug Explanation (JavaScript example)

# The bug is that response.body is a Promise, not a string.
# So calling .toLowerCase() on it crashes.
# Types would help catch this before running the code.


# Part 5 — Types Example

def double_typed(value: int) -> int:
    return value * 2

# With types, tools can warn if we do:
# double_typed("22")  # ❌ wrong type


# Part 6 — Bug in code

def double_bug(number):
    return number * 3

# Bug:
# The function is named "double" but multiplies by 3.
# Fix:

def double_fixed(number):
    return number * 2


# Final Reflection

# 1. Missing types can lead to bugs because we might pass wrong kinds of data.
# 2. Types can catch wrong inputs (e.g., string instead of number).
# 3. Types cannot catch logic errors (like multiplying by 3 instead of 2).