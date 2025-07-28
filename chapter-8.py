# Exercises from Python Crash Course Chapter 8

# 8-12 Write a function that accepts a list of items for a sandwich

def make_a_sandwich(*toppings):
    print("The customer has ordered a sandwich with the following toppings:")
    # Use string literals
    for topping in toppings:
        print(f"{topping}")
    print("Order up!\n")

def main():
    make_a_sandwich('bacon', 'lettuce', 'tomato')
    make_a_sandwich('cheese', 'mustard')
    make_a_sandwich('peanut butter', 'jelly', 'bananas', 'chocolate')

if __name__ == "__main__":
    main()