# Exercises from Python Crash Course Chapter 8

# 8-12 Write a function that accepts a list of items for a sandwich - args practice

def make_a_sandwich(*toppings):
    print("The customer has ordered a sandwich with the following toppings:")
    # Use string literals
    for topping in toppings:
        print(f"{topping}")
    print("Order up!\n")

def build_profile(first, last, **user_info):
    #build a dictionary about the user
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


def main():
    #8-12
    make_a_sandwich('bacon', 'lettuce', 'tomato')
    make_a_sandwich('cheese', 'mustard')
    make_a_sandwich('peanut butter', 'jelly', 'bananas', 'chocolate')

    user_profile = build_profile

if __name__ == "__main__":
    main()