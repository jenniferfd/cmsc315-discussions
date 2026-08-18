# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Implementation Documentation

I created a parent class with class and instance variables, a constructor, and a method that displayed object information. I then created a child class that inherited from the parent class and added additional variables, a new method, and an overridden method.

I demonstrated class and instance namespaces by creating multiple child objects, accessing class variables through both the class and an object, adding an attribute to only one instance, and displaying namespace information with `__dict__`.

I also demonstrated shallow and deep copying using nested mutable data. After modifying the original object's nested list, the shallow copy reflected the change while the deep copy remained independent.

For my student-created extension, I added functionality that allowed a student object to add courses to its course list.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.