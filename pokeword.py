import requests

# URL for the Pokémon API to get the Pokémon list with limit to 10000. Adjust higher if needed.
POKE_API_URL = "https://pokeapi.co/api/v2/pokemon?limit=10000"

# Function to fetch Pokémon names from the API
def fetch_pokemon_names():
    pokemon_names = []
    try:
        response = requests.get(POKE_API_URL)
        if response.status_code == 200:
            data = response.json()
            pokemon_names = [pokemon['name'] for pokemon in data['results']]
        else:
            print("Failed to fetch data. Status code: {response.status_code}")
    except Exception as e:
        print("An error occurred: {e}")
    
    return pokemon_names

# Function to save wordlist to a file
def save_wordlist_to_file(wordlist, filename="pokemon_wordlist.txt"):
    with open(filename, "w") as file:
        for name in wordlist:
            file.write("{name}\n")
    print("Wordlist saved to {filename} with {len(wordlist)} Pokémon names.")

# Main function to execute the program
def main():
    pokemon_names = fetch_pokemon_names()
    if pokemon_names:
        save_wordlist_to_file(pokemon_names)
    else:
        print("No Pokémon names were fetched.")

# Run the main function
if __name__ == "__main__":
    main()