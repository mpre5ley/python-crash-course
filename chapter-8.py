# Exercises from Python Crash Course Chapter 8

# 8-12 Write a function that accepts a list of items for a sandwich - args practice
def make_a_sandwich(*toppings):
    print("The customer has ordered a sandwich with the following toppings:")
    # Use string literals
    for topping in toppings:
        print(f"{topping}")
    print("Order up!\n")

#8-13 Copy a function from the book and add 3 kwargs
def build_profile(first, last, **user_info):
    #build a dictionary about the user
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

#8-14 Write a function to store information about a car into a dictionary
def make_car(make, model, **kwargs):
    #build dictionary
    car = {}
    car['make']=make
    car['model']=model
    for key, value in kwargs.items():
        car[key]=value
    return car


def main():
    #8-12
    make_a_sandwich('bacon', 'lettuce', 'tomato')
    make_a_sandwich('cheese', 'mustard')
    make_a_sandwich('peanut butter', 'jelly', 'bananas', 'chocolate')

    #8-13
    user_profile = build_profile('Matthew',
                                 'Presley',
                                 profession='software engineer',
                                 city='Berlin',
                                 school='IU'
                                 )
    print(user_profile)

    #8-14
    user_car = make_car('Audi',
                        'A4',
                        color='grey',
                        sunroof='Yes',
                        year='2023')
    print(user_car)
    

if __name__ == "__main__":
    main()