import requests, time, os



# URL for the Pokémon API to get the Pokémon list with limit to 10000. Adjust higher if needed.
POKE_API_URL = "https://pokeapi.co/api/v2/pokemon?limit=10000"

# Fetch the data from the API
response = requests.get(POKE_API_URL)
data = response.json()


# Create file name with timestamp appened for tracking.
t = time.localtime()
timestamp = time.strftime('%b-%d-%Y_%H%M', t)
file_name = ("pokemeon_names" + timestamp)

# Open a file to write the Pokemon names
with open(file_name + ".txt", "a+") as file:
    # Loop through each Pokemon and write the name to the file
    for pokemon in data['results']:
        file.write(pokemon['name'] + "\n")
        # Count new lines to know the total amount of names added.
        lines = file.readlines()
        num_newlines = len(lines)

# Print out the number of new lines to file created.
print(num_newlines, "Pokemon names have been written to", file_name + ".txt")
