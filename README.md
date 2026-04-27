# Python Types & OOP

This repository contains a series of exercises focused on improving Python code quality using:

* Type annotations
* Static type checking with `mypy`
* Object-Oriented Programming (OOP)
* Dataclasses, Generics, Enums, and Inheritance

---

##  Learning Goals

Throughout these exercises, I learned to:

* Use type annotations to make code clearer and safer
* Detect bugs early using `mypy`
* Understand and apply classes and objects
* Refactor code safely using types
* Replace fragile string-based logic with enums
* Use generics for more precise type checking
* Understand inheritance and its trade-offs

---

## 📂 Project Structure

```
.
├── types_exercise.py
├── mypy_exercise.py
├── classes_exercise.py
├── methods_exercise.py
├── dataclasses_exercise.py
├── generics_exercise.py
├── type_guided_refactoring.py
├── enums_exercise.py
└── inheritance_exercise.py
```

---

##  Key Concepts Covered

### 1. Why Types Matter

* Prevent invalid operations (e.g. dividing a string)
* Make function expectations explicit
* Reduce runtime errors

---

### 2. Type Checking with `mypy`

* Detects incorrect argument types
* Finds missing attributes and wrong function calls
* Helps during refactoring by pointing to broken code

Run:

```bash
mypy <filename>.py
```

---

### 3. Classes & Objects

* Classes define structure and expected properties
* Instances represent real data
* Type checkers can validate attribute access

---

### 4. Methods vs Functions

* Methods belong to objects (`person.is_adult()`)
* Improve readability and encapsulation

---

### 5. Dataclasses

* Reduce boilerplate code
* Automatically provide:

  * constructor
  * equality comparison
  * readable string output

---

### 6. Generics

* Allow precise typing for collections
* Example:

  ```python
  List[Person]
  ```
* Prevents mixing incompatible types

---

### 7. Type-Guided Refactoring

* Changing types (e.g. `str → List[str]`)
* `mypy` highlights all required updates
* Makes large changes safer and faster

---

### 8. Enums

* Replace unreliable strings with fixed values
* Prevent bugs from typos and inconsistencies
* Centralize validation of input data

---

### 9. Inheritance

* Enables code reuse between classes
* Subclasses extend or override behavior
* Demonstrates method resolution order

---

##  Key Takeaways

* Types catch many bugs early, but not all
* `mypy` is a powerful tool for maintaining code quality
* Clear structure (classes, enums) reduces ambiguity
* Refactoring becomes safer with strong typing

---

##  How to Run

Example:

```bash
python enums_exercise.py
```

---

## How to Check Types

```bash
pip install mypy
mypy .
```

---

## 📌 Notes

* Some files include intentionally incorrect code (commented out) to demonstrate type errors
* Exercises focus on understanding concepts rather than building a single application

---
