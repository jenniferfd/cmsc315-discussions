# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Implementation Documentation

I created a Python dictionary to represent a hash table and used product SKUs as keys with inventory quantities as values. I added multiple key-value pairs to demonstrate how data could be inserted into the dictionary and displayed the dictionary after the insert operations.

I demonstrated lookup operations by retrieving quantities for existing SKU keys. I also updated the quantity of an existing SKU and showed the dictionary before and after the change. When an existing key was assigned a new value, the old value was replaced instead of creating a duplicate key.

For the delete operation, I removed an existing SKU and displayed the dictionary before and after the deletion. I also tested edge cases by looking up a missing SKU using `get()`, which safely returned `None`, and by checking for a missing key before attempting to delete it.

The program demonstrated how Python dictionaries behave like hash tables by using keys to quickly locate associated values. This type of structure is useful for inventory systems because product information can be accessed, updated, or removed efficiently.

## Real-World Scenario

A real-world example of using a hash table is an inventory management system. Each product SKU can be used as a unique key, while the quantity in stock can be stored as its value. This allows the system to quickly check inventory levels, update quantities after a sale or shipment, and remove products that are no longer carried.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.