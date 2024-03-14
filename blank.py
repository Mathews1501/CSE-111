# this function performs a task

def greet(first_name, last_name):

    print(f"Hi there {first_name.capitalize()} {last_name.capitalize()}")
    print("welcome to the studio")


greet("Buck", "Marley")
print()
greet("mark", "peter")
print()
# this function returns a value
# Use the astrix to have multiple parameters

def get_id(* name, age=30, sex="male"):
    return f"My name is {name} i am {age} and my gender is {sex}"

identity = get_id('matty')
print(identity)
print()

#Dictionary use double astrix for arguements remember the sqaure brackets to get specific arguement

def user_id(**user):
    print(user["name"])
    print(user["age"])
    print(user["type_of_user"])


user_id(name="Matt", age=30, type_of_user="super sudo " )
print()

#iterate through each number and multiply

def multiply_numbers(*numbers):
    total = 1 
    for number in numbers:
        total *= number
    return total
    
#print the function with arguements
print(multiply_numbers(5, 6, 7, 5, 8))
print()

def fizz_buzz(input):

    if input >= 5:
        print("Fizz")
    if input <= 5:
        print("Buzz")
    else:
        print("Fizz buzz")

fizz_buzz(3)
