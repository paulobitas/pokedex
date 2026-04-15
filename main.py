from pokedex import __menu, __initialyze, main_page



def main():

    __initialyze()

    print("Cheguei2")
    pokedex = main_page()
    print("Cheguei3")
    __menu(pokedex)
    print("Saí1")

if __name__ == "__main__":
    main()