spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] >5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level_emoji = "🌶" * food["heat_level"]
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {heat_level_emoji}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
def print_spiciest_foods(spicy_foods):
     spiciest_foods = get_spiciest_foods(spicy_foods) 
     print_spicy_foods(spiciest_foods) 

def get_average_heat_level(spicy_foods):
     total_heat_level = sum(food["heat_level"] for food in spicy_foods)
     return total_heat_level // len(spicy_foods) 

def create_spicy_food(spicy_foods, new_food):
     spicy_foods.append(new_food)
     return spicy_foods

# Testing the functions
if __name__ == "__main__":
    # Testing get_names function
    names = get_names(spicy_foods)
    print("Names of spicy foods:", names)
    
    # Testing get_spiciest_foods function
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print("Spiciest foods:", spiciest_foods)
    
    # Testing print_spicy_foods function
    print("Spicy foods:")
    print_spicy_foods(spicy_foods)
    
    # Testing get_spicy_food_by_cuisine function
    american_food = get_spicy_food_by_cuisine(spicy_foods, "American")
    print("Spicy food by cuisine (American):", american_food)
    
    # Testing print_spiciest_foods function
    print("Spiciest foods printed:")
    print_spiciest_foods(spicy_foods)
    
    # Testing get_average_heat_level function
    average_heat = get_average_heat_level(spicy_foods)
    print("Average heat level:", average_heat)
    
    # Testing create_spicy_food function
    new_food = {"name": "Griot", "cuisine": "Haitian", "heat_level": 10}
    updated_foods = create_spicy_food(spicy_foods, new_food)
    print("Spicy foods after adding new food:", updated_foods)

 
