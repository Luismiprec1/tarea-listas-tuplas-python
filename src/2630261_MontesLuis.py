# Python Collections Practice: Lists and Tuples
# Student: Luis Angel Montes Hernandez
# Student ID: 2630261
# Group: IM3
# File: 2630261_MontesLuis.py
#
# Executive Summary
# A list is an ordered collection that can be changed after it is created.
# A tuple is an ordered collection whose positions cannot be reassigned.
# Lists can hold related values that may need to be added, removed, or sorted.
# Tuples can keep fixed values together, like the coordinates of a point.
# This file has six programs that practice lists and tuples in simple examples.
# The programs cover shopping items, points, products, grades, words, and contacts.
# Each problem includes inputs, outputs, validations, and three test cases.
# The examples also show how to search, update, count, and summarize information.
#
# Good Practices
# - Use lists when items need to be added, removed, or reordered.
# - Use tuples for grouped values that should stay fixed.
# - Avoid changing a list while looping through it unless the logic is clear.
# - Keep related lists in the same order when their indexes match.
# - Validate data before using it in calculations or searches.
# - Use clear variable names and messages that explain input errors.
#
# Note: Choose one problem from the menu at the end of this file.
# The sample records in problems 3, 4, and 6 are stored in lists and tuples.
#
import math

# ------------------------------------------------------------
# Problem 1: Shopping list basics
# Description:
# This program creates a list from comma-separated product names.
# It adds one item and checks whether another item is already in the list.
#
# Inputs:
# - initial_items_text: products separated by commas.
# - new_item: one product to add.
# - search_item: one product to look for.
#
# Outputs:
# - Items list, total item count, and whether the searched item was found.
#
# Validations:
# - The initial text, new item, and search item cannot be empty.
# - Empty entries between commas are removed.
# - At least one valid starting item must remain.
#
# Test cases:
# 1) Normal: "apple, banana, orange", "pear", "BANANA" -> found is true.
# 2) Border: "kiwi", "plum", "pear" -> two items after adding and found is false.
# 3) Error: "   " -> print an error because the starting text is empty.
# ------------------------------------------------------------
def run_problem_1():
    initial_items_text = input("Enter items separated by commas: ").strip()
    if not initial_items_text:
        print("Error: invalid input")
        return

    items_list = [
        item.strip()
        for item in initial_items_text.split(",")
        if item.strip()
    ]
    if not items_list:
        print("Error: invalid input")
        return

    new_item = input("Enter a new item: ").strip()
    search_item = input("Enter an item to search: ").strip()
    if not new_item or not search_item:
        print("Error: invalid input")
        return

    items_list.append(new_item)
    normalized_items = [item.lower() for item in items_list]
    found_item = search_item.lower() in normalized_items

    print("Items list:", items_list)
    print("Total items:", len(items_list))
    print("Found item:", str(found_item).lower())


# ------------------------------------------------------------
# Problem 2: Points and distances with tuples
# Description:
# This program stores two points as tuples and calculates their distance.
# It also creates a new tuple with the midpoint between the two points.
#
# Inputs:
# - x1, y1, x2, and y2 as finite numeric values.
#
# Outputs:
# - Point A, Point B, the Euclidean distance, and the midpoint.
#
# Validations:
# - Each coordinate must convert to a finite float.
# - Invalid numeric text is rejected before calculations.
#
# Test cases:
# 1) Normal: (0, 0) and (3, 4) -> distance 5.0 and midpoint (1.5, 2.0).
# 2) Border: (2.5, -1) and (2.5, -1) -> distance 0.0.
# 3) Error: x1 is "north" -> print an error and stop this problem.
# ------------------------------------------------------------
def run_problem_2():
    coordinate_names = ("x1", "y1", "x2", "y2")
    coordinate_values = []

    for coordinate_name in coordinate_names:
        coordinate_text = input(f"Enter {coordinate_name}: ").strip()
        try:
            coordinate_value = float(coordinate_text)
        except ValueError:
            print("Error: invalid input")
            return

        if not math.isfinite(coordinate_value):
            print("Error: invalid input")
            return

        coordinate_values.append(coordinate_value)

    x1, y1, x2, y2 = coordinate_values
    point_a = (x1, y1)
    point_b = (x2, y2)
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", round(distance, 2))
    print("Midpoint:", midpoint)


# ------------------------------------------------------------
# Problem 3: Product catalog with parallel lists
# Description:
# This program stores product names and prices in two lists.
# The same index connects each product name with its price.
#
# Inputs:
# - product_name: a product name.
# - quantity_text: a positive whole number.
#
# Outputs:
# - Unit price, quantity, and total price, or an error message.
#
# Validations:
# - The product name cannot be empty and must exist in the product list.
# - Quantity must be an integer greater than zero.
# - The product and price lists use the same order.
#
# Test cases:
# 1) Normal: "bread", quantity 2 -> unit price 28.50 and total 57.00.
# 2) Border: "milk", quantity 1 -> total 24.00.
# 3) Error: "pear", quantity 2 -> print "Error: product not found".
# ------------------------------------------------------------
def run_problem_3():
    product_names = ["apple", "bread", "milk"]
    unit_prices = [10.0, 28.5, 24.0]

    product_name = input("Enter a product name: ").strip().lower()
    if not product_name:
        print("Error: invalid input")
        return

    quantity_text = input("Enter quantity: ").strip()
    try:
        quantity = int(quantity_text)
    except ValueError:
        print("Error: invalid input")
        return

    if quantity <= 0:
        print("Error: quantity must be greater than zero")
        return

    if product_name not in product_names:
        print("Error: product not found")
        return

    product_index = product_names.index(product_name)
    unit_price = unit_prices[product_index]
    total_price = unit_price * quantity

    print("Unit price:", f"{unit_price:.2f}")
    print("Quantity:", quantity)
    print("Total:", f"{total_price:.2f}")


# ------------------------------------------------------------
# Problem 4: Student grades with lists and tuples
# Description:
# This program stores student names and grade tuples inside a list.
# It finds one student's grades, calculates the average, and checks passing.
#
# Inputs:
# - student_name: the name of a student in the sample records.
#
# Outputs:
# - The grades tuple, average, and whether the student passed.
#
# Validations:
# - The student name cannot be empty and must match a sample record.
# - The selected tuple must contain at least one grade.
#
# Test cases:
# 1) Normal: "Alice" -> grades (90, 85), average 87.50, passed true.
# 2) Border: "Bruno" -> average 67.50, passed false.
# 3) Error: "Maya" -> print "Error: student not found".
# ------------------------------------------------------------
def run_problem_4():
    student_records = [
        ("Alice", (90.0, 85.0)),
        ("Bruno", (65.0, 70.0)),
        ("Carla", (100.0, 95.0)),
    ]
    PASSING_GRADE = 70.0

    student_name = input("Enter a student name: ").strip()
    if not student_name:
        print("Error: invalid input")
        return

    selected_grades = None
    for record_name, grades_tuple in student_records:
        if record_name.lower() == student_name.lower():
            selected_grades = grades_tuple
            break

    if selected_grades is None:
        print("Error: student not found")
        return

    if not selected_grades:
        print("Error: no grades available")
        return

    average_grade = sum(selected_grades) / len(selected_grades)
    is_passed = average_grade >= PASSING_GRADE

    print("Grades:", selected_grades)
    print("Average:", f"{average_grade:.2f}")
    print("Passed:", str(is_passed).lower())


# ------------------------------------------------------------
# Problem 5: Word frequency counter with lists
# Description:
# This program separates a sentence into words and counts each word.
# It uses two lists to store unique words and their matching counts.
#
# Inputs:
# - sentence: a non-empty sentence.
#
# Outputs:
# - The words list, a list of (word, count) pairs, and the most common word.
#
# Validations:
# - The sentence cannot be empty.
# - The cleaned sentence must contain at least one word.
# - Simple punctuation is replaced with spaces before counting.
#
# Test cases:
# 1) Normal: "Red fish, blue fish!" -> fish appears 2 times.
# 2) Border: "Hello..." -> one word remains after cleaning.
# 3) Error: "!!!" -> print an error because no words remain.
# ------------------------------------------------------------
def run_problem_5():
    sentence = input("Enter a sentence: ").strip()
    if not sentence:
        print("Error: invalid input")
        return

    cleaned_sentence = sentence.lower()
    PUNCTUATION_MARKS = ".,!?;:"
    for punctuation_mark in PUNCTUATION_MARKS:
        cleaned_sentence = cleaned_sentence.replace(punctuation_mark, " ")

    words_list = cleaned_sentence.split()
    if not words_list:
        print("Error: invalid input")
        return

    unique_words = []
    word_counts = []
    for word in words_list:
        if word in unique_words:
            word_index = unique_words.index(word)
            word_counts[word_index] += 1
        else:
            unique_words.append(word)
            word_counts.append(1)

    most_common_index = 0
    for word_index in range(1, len(word_counts)):
        if word_counts[word_index] > word_counts[most_common_index]:
            most_common_index = word_index

    frequency_pairs = list(zip(unique_words, word_counts))
    most_common_word = unique_words[most_common_index]

    print("Words list:", words_list)
    print("Frequencies (word, count):", frequency_pairs)
    print("Most common word:", most_common_word)


# ------------------------------------------------------------
# Problem 6: Simple contact book with a list of tuples
# Description:
# This program stores contacts as (name, phone) tuples inside a list.
# It can add or update a contact, search for a phone number, or delete one.
#
# Inputs:
# - action_text: ADD, SEARCH, or DELETE.
# - name: the contact name.
# - phone: a phone number required only for ADD.
#
# Outputs:
# - A saved contact, a phone number, a deletion message, or an error.
#
# Validations:
# - The action must be ADD, SEARCH, or DELETE.
# - The name cannot be empty.
# - ADD requires a non-empty phone number.
# - SEARCH and DELETE check that the name exists before using its index.
#
# Test cases:
# 1) Normal: ADD, "Diana", "5550101" -> contact is saved.
# 2) Border: SEARCH, "Alice" -> returns the existing phone number.
# 3) Error: DELETE, "Maya" -> print "Error: contact not found".
# ------------------------------------------------------------
def run_problem_6():
    contacts = [
        ("Alice", "5551234567"),
        ("Bruno", "5557654321"),
        ("Carla", "5559876543"),
    ]

    action_text = input("Enter action (ADD, SEARCH, DELETE): ").strip().upper()
    valid_actions = ("ADD", "SEARCH", "DELETE")
    if action_text not in valid_actions:
        print("Error: invalid action")
        return

    name = input("Enter contact name: ").strip()
    if not name:
        print("Error: invalid input")
        return

    contact_name = name.title()
    contact_index = -1
    for index, contact in enumerate(contacts):
        if contact[0].lower() == contact_name.lower():
            contact_index = index
            break

    if action_text == "ADD":
        phone = input("Enter phone number: ").strip()
        if not phone:
            print("Error: invalid input")
            return

        if contact_index >= 0:
            contacts[contact_index] = (contact_name, phone)
        else:
            contacts.append((contact_name, phone))
        print("Contact saved:", contact_name, phone)

    elif action_text == "SEARCH":
        if contact_index < 0:
            print("Error: contact not found")
        else:
            print("Phone:", contacts[contact_index][1])

    else:
        if contact_index < 0:
            print("Error: contact not found")
        else:
            contacts.pop(contact_index)
            print("Contact deleted:", contact_name)


# ------------------------------------------------------------
# Main Menu
# Choose one problem number to run. Each problem is independent.
# ------------------------------------------------------------
def main():
    print("Python lists and tuples practice")
    print("1. Shopping list")
    print("2. Points and distances")
    print("3. Product catalog")
    print("4. Student grades")
    print("5. Word frequency")
    print("6. Contact book")
    problem_choice = input("Choose a problem (1-6): ").strip()

    if problem_choice == "1":
        run_problem_1()
    elif problem_choice == "2":
        run_problem_2()
    elif problem_choice == "3":
        run_problem_3()
    elif problem_choice == "4":
        run_problem_4()
    elif problem_choice == "5":
        run_problem_5()
    elif problem_choice == "6":
        run_problem_6()
    else:
        print("Error: invalid input")


if __name__ == "__main__":
    main()

# ------------------------------------------------------------
# Conclusions
# Lists work well when a program needs to add, remove, or reorder items.
# Tuples are useful for fixed groups of values, like the coordinates of a point.
# I practiced using lists of tuples to keep related information together.
# Parallel lists can also work, as long as their positions stay matched.
# Choosing a collection that fits the problem makes the code easier to follow.
# Validating input first helps avoid errors during calculations and searches.
#
# References
# 1) Python Documentation - Tutorial: More on Lists
#    https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
# 2) Python Documentation - Tutorial: Tuples and Sequences
#    https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
# 3) Python Documentation - Built-in Types: Sequence Types
#    https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
# 4) Python Documentation - Built-in Functions: len, sum, min, max, sorted
#    https://docs.python.org/3/library/functions.html#len
# 5) Python Documentation - Tutorial: Errors and Exceptions
#    https://docs.python.org/3/tutorial/errors.html

