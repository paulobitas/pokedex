### To do list:
# - Create a menu with system options
# - List all pokemon of specific type (list types, then, ask desired type and show results)


import locale
import platform
import pandas as pd

from pokemondraw import bulbasaur, dragonite, charizard, __pokemon_draw, charmeleon, wartortle, venosaur, squirtle, blastoise, ivysaur, charmander, ash
from pathlib import Path

if platform.system() == "Windows":
    locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil')
else:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

version = "0.1v"




# Seek Pokemon csv file and load to a Pandas dataframe
def seek_pokemon_file():

    while True:
        try:

            archive = Path(f"pokemon.csv")

            # Verify if the file exists in the current directory
            if not Path(archive).is_file():
                print(f"File '{archive}' not found. Please try again.")

                input("Check file and press enter to continue")
                continue

            # Read the spreadsheet using Pandas
            df_base = pd.read_csv(archive, encoding = "UTF-8", sep = "," )
            print(f"File {archive} loaded successfully!")

            df_base["number"] = range(1, len(df_base) + 1)

            return df_base
        
        # Return error message if the file cannot be read
        except Exception as e:
            print(f"An error occurred while trying to read the file: {e}. Please try again.")

# Program boot message
def __initialyze():

    __pokemon_draw() # Print Pokemon Logo

    print(f"""--------------- Pokemon Data Analysis ------------------

        Analysis of data from the Pokemon universe (Gen I to VII)
        Author - Paulo Izidoro
        Data -  {pd.Timestamp.now()}\n\n""")
    

# Return a list of dictionaries with the unique pokemon types and their respective index in a array
def __type_list(pokedex):
    
    # Create a list with all unique pokemon types
    list = pokedex["type1"].sort_values().unique().tolist()

    ind = 0 
    type_list = []

    while ind < len(list):
        type_list.append({"number" : ind,
                          "type" : list[ind]})
        ind += 1

    for i in type_list:
        print(f"{i['number']} - {i['type']}")

    pass

# Search for all pokemon of a specific type, in this case, "fire"
def __search_pokemon_by_type (pokedex):

     # List all types of pokemon
    __type_list(pokedex)

    pokemon_type = input(f"Digit the pokemon type: ")
                            
    result_pokemon_by_type = pokedex[(pokedex["type1"] == pokemon_type.lower()) | (pokedex["type2"] == pokemon_type.lower())][["pokedex_number", "name", "type1", "type2"]].reset_index(drop=True)

    return print(result_pokemon_by_type)

def __list_of_games():

    games = ["Generation I: Red, Blue, Green & Yellow ", 
                     "Generation II: Gold, Silver & Crystal", 
                     "Generation III: Ruby, Sapphire & Emerald", 
                     "Generation IV: Diamond, Pearl & Platinum", 
                     "Generation V: Black & White", 
                     "Generation VI: X & Y", 
                     "Generation VII: Sun & Moon"]
    
    for i in games:
        print(i)

def __list_of_generations(pokedex):

    generation = []
    i = 0
    while i < len(pokedex["generation"].unique()):

        games = ["Red, Blue, Green & Yellow ", 
                     "Gold, Silver & Crystal", 
                     "Ruby, Sapphire & Emerald", 
                     "Diamond, Pearl & Platinum", 
                     "Black & White", 
                     "X & Y", 
                     "Sun & Moon"]
        
        generation.append({
                        "Generation" : i + 1,
                        "Games" : games[i],
                        "count" : pokedex[pokedex["generation"] == i + 1]["pokedex_number"].count()
                      })
        
        i += 1

    for ill in generation:
        print(f"Generation " + str(ill['Generation']) + "\n" +
                "Games: " + ill['Games'] + "\n" +
                "Number of Pokemon: " + str(ill['count'])+ "\n")

    print("Total number of Pokemon: " + str(pokedex["pokedex_number"].count())) 

    pass

# List all pokemon throughout all generations with their respective attributes

def __pokemon_list(pokedex):

    charmeleon()

    print(f"List of all Pokemon throughout all generations:\n")

    pokemon_list = pokedex[[
                            "pokedex_number", 
                            "name",
                            "japanese_name",
                            "classfication",
                            "type1", 
                            "type2",
                            "generation",
                            "height_m",
                            "weight_kg",
                            "attack",
                            "defense",
                            "speed",
                            "hp",
                            "sp_attack",
                            "sp_defense"
                            ]].reset_index(drop = True)
    
    print(f"Total number of Pokemon: " + str(pokedex["pokedex_number"].count()) + "\n")

    return pokemon_list

# Search for a specific pokemon by its pokedex number and return its attributes
def __search_pokemon(pokedex):

    while True:
        try:
            pokemon_number = int(input(f"Digit the pokemon number (1-{pokedex['pokedex_number'].max()}): "))
            
            if pokemon_number < 1 or pokemon_number > pokedex["pokedex_number"].max():

                print(f"Invalid input. Please enter a number between 1 and {pokedex['pokedex_number'].max()}.")

                continue

            else:

                break

        except ValueError:

            print(f"Invalid input. Please enter a number between 1 and {pokedex['pokedex_number'].max()}.")

            continue


    pokemon = pokedex[pokedex["pokedex_number"] == pokemon_number][[
                            "pokedex_number", 
                            "name",
                            "japanese_name",
                            "classfication",
                            "type1", 
                            "type2",
                            "generation",
                            "height_m",
                            "weight_kg",
                            "attack",
                            "defense",
                            "speed",
                            "hp",
                            "sp_attack",
                            "sp_defense"
                            ]].reset_index(drop = True)
    
    print(pokemon)

    pass


def __search_pokemon_by_generation(pokedex):

    def search(generation):

        

        pokemon_list =  pokedex[pokedex["generation"] == generation][[
            "pokedex_number", 
            "name",
            "japanese_name",
            "classfication",
            "type1", 
            "type2",
            "generation",
            "height_m",
            "weight_kg",
            "attack",
            "defense",
            "speed",
            "hp",
            "sp_attack",
            "sp_defense"

            ]].reset_index(drop=True)   
        
        print(pokemon_list)

        print(f"Total number of Pokemon in Generation {generation}: " + str(pokemon_list["pokedex_number"].count()))

        pass

    while True:
        try:

            __list_of_generations(pokedex)

            generation_input = int(input(f"Enter the generation number (1 to {pokedex['generation'].max()}): "))
            
            if generation_input < 1 or generation_input > pokedex["generation"].max():
                print(f"Invalid input. Please enter a number between 1 and {pokedex['generation'].max()}.")
                continue
            else:
                search(generation_input)
                break

        except ValueError:
            print(f"Invalid input. Please enter a number between 1 and {pokedex['generation'].max()}.")
            continue

    pass


# Create a menu with system options
def __menu():

    option = -1

    print(__pokemon_draw())

    menu = f"""POKEDEX --- Version {version}

    1 - List all pokemon throughout all generations
    2 - List all generations main games
    3 - Search all pokemon of a specific type
    4 - Search all pokemon from a specific generation
    5 - List all pokemon types
    0 - Exit

    """

    while option != 0:        

        try:

            print(menu)

            option = int(input(f"Choose option number: "))
            
            options = [1,2,3,4,5,6,0]

            if option not in options:
                continue

            match option:

                # 1 - List all pokemon throughout all generations
                case 1: 
                    print(__pokemon_list(pokedex))
                
                # 2 - List all generations main games
                case 2: 
                    __list_of_generations(pokedex)
                
                # 3 - Search all pokemon of a specific type
                case 3: 

                    continue
                
                #4 - Search all pokemon from a specific generation
                case 4: 
                    continue
                
                # 5 - List all pokemon types
                case 5: 
                    continue
                
                # 0 - Exit
                case 0: 
                    break
            

        except ValueError:
            print(f"Invalid option!")

            continue





### Sessão de testes
 
pokedex = seek_pokemon_file()

__initialyze()

#__menu()


# List all pokemons
print("Cheguei")


#__pokemon_list(pokedex) # List all pokemon throughout all generations with their respective attributes
#__search_pokemon(pokedex) # Search for a specific pokemon by its pokedex number and return its attributes
#__list_of_generations(pokedex) # Resume of each generation with the number of pokemon in each one and the main games of each generation
#__list_of_games() # List all main games of each generation
#__search_pokemon_by_type(pokedex) # Function to show types, then, search for all pokemon of a specific type, in this case, "fire"
#__search_pokemon_by_generation(pokedex) # Search for all pokemon from a specific generation, in this case, "Generation 1"
#__type_list(pokedex) # List all types of pokemon
#__search_pokemon(pokedex) # Search for a specific pokemon by its pokedex number and return its attributes
__menu() # Create a menu with system options

print("Terminei")

#wartortle()
#bulbasaur()
#dragonite()
#charizard()
#venosaur()
#squirtle()
#blastoise()
#ivysaur()
#charmander()
ash()

#__list_of_games()


# List all types of pokemon
#__type_list(pokedex)

# Resume of each generation
#__list_of_generations(pokedex)

# Search for all pokemon of a specific type, in this case, "fire"
#print(__search_pokemon_by_type(pokedex, "fire"))

# Search for all pokemon of a specific generation, in this case, "Generation 1"
#__search_pokemon_by_generation(pokedex)



### Fim da sessão de testes