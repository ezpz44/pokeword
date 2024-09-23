import requests, time, os



# URL for the Pokémon API to get the Pokémon list with limit to 10000. Adjust higher if needed.
POKE_API_URL = "https://pokeapi.co/api/v2/pokemon?limit=10000"

# Fetch the data from the API
response = requests.get(POKE_API_URL)
data = response.json()


# Create file name with timestamp appened for tracking.
t = time.localtime()
timestamp = time.strftime('%b-%d-%Y_%H%M', t)
file_name = ("pokemeon_names_" + timestamp)

# Open a file to write the Pokemon names
with open(file_name + ".txt", "a+") as file:
    # Loop through each Pokemon and write the name to the file
    for pokemon in data['results']:
        # Remove hyphens from Pokémon names
        clean_name = pokemon['name'].replace('-', '')
        file.write(clean_name + "\n")

# Open the file again to count the number of lines (number of Pokémon names)
with open(file_name + ".txt", "r") as file:
    lines = file.readlines()
    num_newlines = len(lines)

# Print out the number of new lines to file created.
print(num_newlines, "Pokemon names have been written to", file_name + ".txt")
