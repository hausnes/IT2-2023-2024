# Create an empty dictionary to store the data
data = {
    "Norway" : {
        "capital" : "Oslo",
        "population" : 5378857,
        "neighbors" : ["Sweden", "Finland", "Russia"]
    }
}

# Define a function to add a country and its information to the data dictionary
def add_country(name, capital, population, neighbors):
    # Check if the name is a valid string
    if not isinstance(name, str):
        print("Invalid name")
        return
    # Check if the capital is a valid string
    if not isinstance(capital, str):
        print("Invalid capital")
        return
    # Check if the population is a valid integer
    if not isinstance(population, int):
        print("Invalid population")
        return
    # Check if the neighbors is a valid list of strings
    if not isinstance(neighbors, list) or not all(isinstance(n, str) for n in neighbors):
        print("Invalid neighbors")
        return
    # Create a dictionary with the information of the country
    country = {
        "capital": capital,
        "population": population,
        "neighbors": neighbors
    }
    # Add the country to the data dictionary with the name as the key
    data[name] = country

# Examples: Add countries and their information to the data dictionary
# add_country("Norway", "Oslo", 5378857, ["Sweden", "Finland", "Russia"]) # Already added at the start of the program
add_country("India", "New Delhi", 1366417754, ["Pakistan", "China", "Nepal", "Bhutan", "Bangladesh", "Myanmar"])
add_country("Canada", "Ottawa", 39090369, ["United States"])
add_country("Australia", "Canberra", 25834167, ["Indonesia", "Papua New Guinea", "New Zealand"])
add_country("Sweden", "Stockholm", 10338368, ["Norway", "Finland"])
add_country("Morocco", "Rabat", 38044551, ["Algeria", "Western Sahara", "Spain"])
add_country("Peru", "Lima", 33699903, ["Ecuador", "Colombia", "Brazil", "Bolivia", "Chile"])
add_country("Malaysia", "Kuala Lumpur", 33080328, ["Thailand", "Indonesia", "Brunei", "Singapore"])
add_country("Nepal", "Kathmandu", 30451985, ["China", "India"])
add_country("Chile", "Santiago", 19107216, ["Peru", "Bolivia", "Argentina"])

# Define a function to find the country with the largest population
def find_largest_population():
    # Initialize the largest population to 0
    largest_population = 0
    # Initialize the country with the largest population to an empty string
    largest_population_country = ""
    # Iterate through the countries in the data dictionary
    for country in data:
        # Check if the population of the current country is larger than the largest population
        if data[country]["population"] > largest_population:
            # Update the largest population
            largest_population = data[country]["population"]
            # Update the country with the largest population
            largest_population_country = country
    # Return the country with the largest population
    return largest_population_country

print("Largest population:",find_largest_population())

# Define a function to find the country with the most neighbors
def find_most_neighbors():
    # Initialize the most neighbors to 0
    most_neighbors = 0
    # Initialize the country with the most neighbors to an empty string
    most_neighbors_country = ""
    # Iterate through the countries in the data dictionary
    for country in data:
        # Check if the number of neighbors of the current country is larger than the most neighbors
        if len(data[country]["neighbors"]) > most_neighbors:
            # Update the most neighbors
            most_neighbors = len(data[country]["neighbors"])
            # Update the country with the most neighbors
            most_neighbors_country = country
    # Return the country with the most neighbors
    return most_neighbors_country

print("Most neighbors:",find_most_neighbors())

# Import the random module to generate random questions
import random

# Define a function to ask a question and check the answer
def ask_question():
    # Choose a random country from the data dictionary
    country = random.choice(list(data.keys()))
    # Choose a random attribute from the country dictionary
    attribute = random.choice(list(data[country].keys()))
    # Get the correct answer from the data dictionary
    answer = data[country][attribute]
    # Print the question
    print(f"What is the {attribute} of {country}?")
    # Get the user input
    user_answer = input()
    # Check if the user input matches the correct answer
    # Try to convert the user input to an integer
    try:
        user_answer = int(user_answer)
    except ValueError:
        # If the conversion fails, do nothing
        pass
    # Compare the user input with the correct answer
    if user_answer == answer: # To-do: check  'or user_answer in answer'
        # Print a positive feedback
        print("Correct!")
    else:
        # Print a negative feedback and the correct answer
        print(f"Wrong. The correct answer is {answer}.")

ask_question()