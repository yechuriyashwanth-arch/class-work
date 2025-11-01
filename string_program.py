# Python program to create a string, access its elements, and demonstrate built-in methods

# Step 1: Create a string
my_string = "Hello, World!"

# Step 2: Access elements of the string
print("Original string:", my_string)
print("First character:", my_string[0])  # Accessing the first element (index 0)
print("Last character:", my_string[-1])  # Accessing the last element (negative indexing)
print("Substring from index 7 to 11:", my_string[7:12])  # Slicing to access a range of elements

# Step 3: Demonstrate built-in methods on strings
print("\nBuilt-in methods demonstration:")
print("Length of string:", len(my_string))  # len() - returns the length
print("Uppercase:", my_string.upper())  # upper() - converts to uppercase
print("Lowercase:", my_string.lower())  # lower() - converts to lowercase
print("Capitalized:", my_string.capitalize())  # capitalize() - capitalizes the first letter
print("Title case:", my_string.title())  # title() - capitalizes the first letter of each word
print("Replaced 'World' with 'Python':", my_string.replace("World", "Python"))  # replace() - replaces a substring
print("Split into words:", my_string.split())  # split() - splits the string into a list
print("Joined back:", " ".join(my_string.split()))  # join() - joins elements of a list into a string
print("Starts with 'Hello':", my_string.startswith("Hello"))  # startswith() - checks if starts with a substring
print("Ends with 'World!':", my_string.endswith("World!"))  # endswith() - checks if ends with a substring
print("Find 'World':", my_string.find("World"))  # find() - returns the index of the first occurrence
print("Count of 'l':", my_string.count("l"))  # count() - counts occurrences of a substring
print("Is alphanumeric:", my_string.isalnum())  # isalnum() - checks if all characters are alphanumeric
print("Is alphabetic:", my_string.isalpha())  # isalpha() - checks if all characters are alphabetic
print("Is digit:", my_string.isdigit())  # isdigit() - checks if all characters are digits
print("Is lowercase:", my_string.islower())  # islower() - checks if all characters are lowercase
print("Is uppercase:", my_string.isupper())  # isupper() - checks if all characters are uppercase
print("Stripped whitespace:", "  Hello, World!  ".strip())  # strip() - removes leading/trailing whitespace
