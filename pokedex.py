### To do list:
# 1 - Correct option 3 with wrong type name
# 2 - Correct option 6 name
# 3 - Create a main page where user can't see the code


import locale
import platform
import pandas as pd

from pokemondraw import bulbasaur, caterpie, dragonite, charizard, __pokemon_draw, charmeleon, wartortle, venosaur, squirtle, blastoise, ivysaur, charmander, ash, caterpie
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
def __list_pokemon_by_type (pokedex):

    #Draw Squirtle Pokemon
    squirtle()

    # List all types of pokemon
    __type_list(pokedex)

    pokemon_type = input(f"\nDigit the pokemon type: (ex.: Fire, Water, Steel): ")
                            
    result_pokemon_by_type = pokedex[(pokedex["type1"] == pokemon_type.lower()) | (pokedex["type2"] == pokemon_type.lower())][["pokedex_number", "name", "type1", "type2"]].reset_index(drop=True)

    print(result_pokemon_by_type)

    input("Press enter to continue...")

    pass

def __list_of_games():

    main_games = ["Generation I: Red, Blue, Green & Yellow ", 
                     "Generation II: Gold, Silver & Crystal", 
                     "Generation III: Ruby, Sapphire & Emerald", 
                     "Generation IV: Diamond, Pearl & Platinum", 
                     "Generation V: Black & White", 
                     "Generation VI: X & Y", 
                     "Generation VII: Sun & Moon"]

    
    side_games = ["Pokemon Stadium", 
                  "Pokemon Snap", 
                  "Pokemon Mystery Dungeon", 
                  "Pokemon Ranger", 
                  "Pokemon Go"] 

    # Draw Bulbasaur Pokemon
    bulbasaur()

    print(f"\nList of all games in the series:\n")

    print(f"\nMain games of each generation:\n")

    for i in main_games:
        print(i)

    print(f"\nSide games of the Pokemon universe:\n")

    for i in side_games:
        print(i)

    input("Press enter to continue...\n")

    pass
    
# List of all pokemon throughout all generations with their respective attributes
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

    input("Press enter to continue...\n")

    pass

# List all pokemon throughout all generations with their respective attributes
def __pokemon_list(pokedex):

    #Draw Charmeleon Pokemon
    charmeleon()

    print(f"\nList of all Pokemon throughout all generations:\n")

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

    print(pokemon_list)

    input("Press enter to continue...\n")

    pass

# Search for a specific pokemon by its original pokedex number and return its attributes
def __search_pokemon(pokedex):

    # search for a specific pokemon by its original pokedex number
    def __search_by_number(pokedex):
        
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

        input("\nPress enter to continue...\n")

    pass   
    
    # Search for a specific pokemon by its name and return its attributes
    def __search_by_name(pokedex):

        while True:
            try:
                pokemon_name = input(f"Enter the pokemon name: ")
                
                if pokemon_name.lower() not in pokedex["name"].str.lower().values:

                    print(f"Invalid input. Please enter a valid pokemon name.")

                    continue

                else:

                    break

            except ValueError:

                print(f"Invalid input. Please enter a valid pokemon name.")

                continue


        pokemon = pokedex[pokedex["name"].str.lower() == pokemon_name.lower()][[
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

        input("Press enter to continue...\n")

        pass

    while True:
        try:    

            #Draw Charmander Pokemon
            charmander()

            # Second Menu - Search Pokemon by pokedex number or name
            print(f"\nSearch Pokemon by:\n")
            print ("1 - Search by pokedex number\n" +
                   "2 - Search by name\n" +
                   "0 - Back to menu\n")
            
            search_option = int(input(f"Choose option number: "))   
            options = [1,2,0]

            if search_option not in options:

                print("Invalid option. Please choose a valid option number.")

                continue

            else:
                
                break

        except ValueError:

            print(f"Invalid input.\nPlease choose a valid option number.\n")

            continue

    match search_option:        
        case 1:
            __search_by_number(pokedex)
            return

        case 2:
            __search_by_name(pokedex)
            return
        case 0:
            return

# Search for all pokemon from a specific generation, in this case, "Generation 1"
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
        
        # Draw Ivysaur Pokemon
        ivysaur()

        print(pokemon_list)

        print(f"Total number of Pokemon in Generation {generation}: " + str(pokemon_list["pokedex_number"].count()))

        input("Press enter to continue...\n")

        pass

    while True:
        try:
            
            # Draw Caterpie Pokemon
            caterpie() 

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
def __menu(pokedex):

    option = -1

    __pokemon_draw()

    menu = f"""POKEDEX --- Version {version}

    1 - List all pokemon throughout all generations
    2 - Search Pokemon (by pokedex number or name)
    3 - List all pokemon of a specific type
    4 - Search all pokemon from a specific generation
    5 - List all games in the series
    6 - List of all pokemon throughout all generations with their respective attributes
    0 - Exit

    """

    while option != 0:        

        try:

            print(menu)

            option = int(input(f"Choose option number: "))
            
            options = [1,2,3,4,5,6,0]

            if option not in options:

                print(f"Invalid option!")
                print("\nPlease, insert a valid option.\n")

                continue

            match option:

                # 1 - List all pokemon throughout all generations
                case 1: 
                    __pokemon_list(pokedex)
                
                # 2 - Search Pokemon (by pokedex number or name)
                case 2: 
                    __search_pokemon(pokedex)
                
                # 3 - List all pokemon of a specific type
                case 3: 
                    __list_pokemon_by_type(pokedex)
                
                #4 - Search all pokemon from a specific generation
                case 4: 
                    __search_pokemon_by_generation(pokedex)
                
                # 5 - List of all games in the series
                case 5: 
                    __list_of_games()
                
                # 6 - List of all pokemon throughout all generations with their respective attributes
                case 6:
                    __list_of_generations(pokedex)

                # 0 - Exit
                case 0: 

                    # Draw Ash (Satoshi) trainer
                    ash()

                    break
            

        except ValueError:
            print(f"Invalid option!")
            print("\nPlease, insert a valid option.\n")

            continue





### Sessão de testes

def main_page():

    __initialyze()

    pokedex = seek_pokemon_file()

    return pokedex
 


#__menu(pokedex)


# List all pokemons
#print("Teste - Cheguei")


#__pokemon_list(pokedex) # List all pokemon throughout all generations with their respective attributes
#__search_pokemon(pokedex) # Search for a specific pokemon by its pokedex number and return its attributes
#__list_of_generations(pokedex) # Resume of each generation with the number of pokemon in each one and the main games of each generation
#__list_of_games() # List all main games of each generation
#__search_pokemon_by_type(pokedex) # Function to show types, then, search for all pokemon of a specific type, in this case, "fire"
#__search_pokemon_by_generation(pokedex) # Search for all pokemon from a specific generation, in this case, "Generation 1"
#__type_list(pokedex) # List all types of pokemon
#__search_pokemon(pokedex) # Search for a specific pokemon by its pokedex number and return its attributes
#__menu(pokedex) # Create a menu with system options

#print("Teste - Terminei")



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