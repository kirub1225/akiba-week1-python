#taking input 
full_name = input("Enter your full name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
university = input("Enter your university: ")
department = input("Enter your department: ")
favorite_language = input("Enter your favorite programming language: ")
programming_goal = input("Enter your programming goal: ")
#displaying the information 
print("\n" + "=" * 40)
print("        STUDENT INTRODUCTION")
print("=" * 40 + "\n")

print(f"My name is {full_name}.")
print(f"I am {age} years old.")
print(f"I live in {city}.")
print(f"I study {department} at {university}.")
print(f"My favorite programming language is {favorite_language}.\n")

print("My programming goal:")
print(f"{programming_goal}\n")

print("=" * 40)