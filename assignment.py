# 1. Input/Output
# Get user's name and age
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# 2. Basic Arithmetic Operations
# Calculate the year when the user will turn 100
current_year = 2024
year_when_100 = current_year + (100 - age)

# 3. Conditional Statements
# Provide a message based on the age
if age < 18:
    age_group = "a minor"
elif 18 <= age < 65:
    age_group = "an adult"
else:
    age_group = "a senior citizen"

# 4. Looping
# Print a message a certain number of times
print("\nMessages:")
for i in range(5):
    print(f"Hello {name}! You are {age} years old, which makes you {age_group}.")

# 5. Functions
# Define a function to display when the user will turn 100
def year_to_turn_100(name, year_when_100):
    return f"{name}, you will turn 100 years old in the year {year_when_100}."

# Call the function and display the result
message = year_to_turn_100(name, year_when_100)
print("\n" + message)
