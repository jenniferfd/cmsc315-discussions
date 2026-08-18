"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""

from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    category = "General Person"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    role = "Student"

    def __init__(self, name, age, student_id, courses):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = courses

    def display_info(self):
        return (
            f"Name: {self.name}, Age: {self.age}, "
            f"Student ID: {self.student_id}, Courses: {self.courses}"
        )

    def add_course(self, course_name):
        self.courses.append(course_name)


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    student1 = ChildClass("Jennifer", 25, "S1001", ["CMSC 315"])
    student2 = ChildClass("Alex", 22, "S1002", ["CMSC 215"])

    print("Class variable through class:", ChildClass.role)
    print("Class variable through object:", student1.role)

    student1.favorite_language = "Python"

    print("\nStudent 1 namespace:")
    print(student1.__dict__)

    print("\nStudent 2 namespace:")
    print(student2.__dict__)

    print("\nChildClass namespace:")
    print(ChildClass.__dict__)


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original = ChildClass(
        "Jordan",
        21,
        "S2001",
        [["CMSC 315", "Data Structures"], ["CMSC 215", "Programming"]]
    )

    shallow_copy = copy(original)
    deep_copy = deepcopy(original)

    original.courses[0].append("Python")

    print("Original:")
    print(original.courses)

    print("\nShallow copy:")
    print(shallow_copy.courses)

    print("\nDeep copy:")
    print(deep_copy.courses)

    # A shallow copy creates a new outer object, but nested mutable
    # objects are still shared with the original.
    #
    # A deep copy creates completely separate copies of nested objects,
    # so changes to the original do not affect the deep copy.


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\nParent Object")
    parent = ParentClass("Taylor", 40)
    print(parent.display_info())

    print("\nChild Object")
    child = ChildClass("Jennifer", 25, "S1001", ["CMSC 315"])
    print(child.display_info())

    child.add_course("CMSC 310")
    print(child.display_info())

    print("\nEdge Case: Student With No Courses")
    empty_student = ChildClass("Morgan", 20, "S3001", [])
    print(empty_student.display_info())

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()