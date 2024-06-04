import time
import characterGENERATOR.characterGENERATORclasses
import characterGENERATOR.characterGENERATORparameters
from Levenshtein import distance as levenshtein

if __name__ == "__main__":
    def wait_a_moment(times=2):
        for _ in range(times):
            time.sleep(0.25)


    def repeat():
        repeatAsk = input("Repeat?").strip().lower()
        return repeatAsk in ("tak", "t", "yes", "y")


    def show_results(globalInstances):
        if not globalInstances:
            print("No data in current database")
            return False
        else:
            for key, value in globalInstances.items():
                print(dunder_str_for_save(key, value))
                return True


    def dunder_str_for_save(key, value):
        try:
            if language in ("ENG", "Eng", "eng", "en", "e"):
                result = f"""
    Id:{key}
    Name:
        {value[0]}, {value[18]}, {value[1]} 
    Main characteristics:
        ws:{value[2]}, bs:{value[3]}, s:{value[4]}, t:{value[5]}, ag:{value[6]}, int: {value[7]}, wp:{value[8]}, fel:{value[9]}
    Second characteristics:
        a:{value[10]}, w:{value[11]}, sb:{value[12]}, tb:{value[13]}, m:{value[14]}, mag:{value[15]}, ip:{value[16]}, fp:{value[17]}
        """
            else:
                result = f"""
    Id:{key}
    Nazwa Postaci:
        {value[0]}, {value[18]}, {value[1]} 
    Cechy główne:
        ww:{value[2]}, us:{value[3]}, k:{value[4]}, odp:{value[5]}, zr:{value[6]}, int: {value[7]}, sw:{value[8]}, ogd:{value[9]}
    Cechy drugorzędne:
        a:{value[10]}, żyw:{value[11]}, s:{value[12]}, wt:{value[13]}, sz:{value[14]}, mag:{value[15]}, po:{value[16]}, ps:{value[17]}
        """

        except IndexError:
            if language in ("ENG", "Eng", "eng", "en", "e"):
                result = f"""
    Id:{key}
    Name:
        {value[0]}, {value[1]} 
    Main characteristics:
        ws:{value[2]}, bs:{value[3]}, s:{value[4]}, t:{value[5]}, ag:{value[6]}, int: {value[7]}, wp:{value[8]}, fel:{value[9]}
    Second characteristics:
        a:{value[10]}, w:{value[11]}, sb:{value[12]}, tb:{value[13]}, m:{value[14]}, mag:{value[15]}, ip:{value[16]}, fp:{value[17]}
    
        """
            else:
                result = f"""
    Id:{key}
    Nazwa Postaci:
        {value[0]}, {value[1]} 
    Cechy główne:
        ww:{value[2]}, us:{value[3]}, k:{value[4]}, odp:{value[5]}, zr:{value[6]}, int: {value[7]}, sw:{value[8]}, ogd:{value[9]}
    Cechy drugorzędne:
        a:{value[10]}, żyw:{value[11]}, s:{value[12]}, wt:{value[13]}, sz:{value[14]}, mag:{value[15]}, po:{value[16]}, ps:{value[17]}
        """
        return result


    def save_to_file():
        globalInstances = characterGENERATOR.characterGENERATORclasses.RandomHumanoid.instances.copy()
        globalInstances.update(characterGENERATOR.characterGENERATORclasses.StepHumanoid.instances)
        results = show_results(globalInstances)
        wait_a_moment()
        if results:
            print("Chosen character will be saved in *.txt file")
            choice = str(input("Type [id] or save [a]: "))
            if choice.lower() != "a":
                bestMatch = check_id(choice, globalInstances)
                value = globalInstances[bestMatch]
                print("You wrote: " + bestMatch)

                with open("Characters.txt", 'a+', encoding="utf-8") as file:
                    file.write(dunder_str_for_save(bestMatch, value))

            else:
                with open("Characters.txt", 'a+', encoding="utf-8") as file:
                    for key, value in globalInstances.items():
                        file.write(dunder_str_for_save(key, value))


    def check_id(choice, globalInstances):
        levenshteinDict = {}
        for key, value in globalInstances.items():
            levenshteinDict[key] = (levenshtein(key.lower(), choice.lower()))
        bestMatch = min(levenshteinDict, key=levenshteinDict.get)
        return bestMatch


    def random_humanoid():
        while True:
            howmany = int(input("How many characters do you need?"))
            for _ in range(howmany):
                randomHumanoid = characterGENERATOR.characterGENERATORclasses.RandomHumanoid(language)
                print(randomHumanoid)
            if not repeat():
                wait_a_moment()
                break


    def step_humanoid_race():
        chosenRace = int(input(f"""Chose race
        1. {characterGENERATOR.characterGENERATORparameters.humanoidRacesStats["Human"]["race"]}
        2. {characterGENERATOR.characterGENERATORparameters.humanoidRacesStats["Elf"]["race"]}
        3. {characterGENERATOR.characterGENERATORparameters.humanoidRacesStats["Dwarf"]["race"]}
        4. {characterGENERATOR.characterGENERATORparameters.humanoidRacesStats["Halfing"]["race"]}
        5. Random
                """))
        if chosenRace == 1:
            race = characterGENERATOR.characterGENERATORparameters.humanoidRacesStats["Human"]["race"]
        elif chosenRace == 2:
            race = characterGENERATOR.characterGENERATORparameters.humanoidRacesStats["Elf"]["race"]
        elif chosenRace == 3:
            race = characterGENERATOR.characterGENERATORparameters.humanoidRacesStats["Dwarf"]["race"]
        elif chosenRace == 4:
            race = characterGENERATOR.characterGENERATORparameters.humanoidRacesStats["Halfing"]["race"]
        elif chosenRace == 5:
            race = None
        else:
            race = None
        return race


    def step_humanoid_name():
        chosenName = int(input(f"""
    How would you like name your character? 
    1. Random
    2. Myself
    """))
        if (chosenName == 1) or (chosenName in ["random", "Random", "r", "R"]):
            name = None
        else:
            name = str(input("Please type name of your character"))
        return name


    def step_humanoid_class():
        chosenCharacterClass = int(input(f"""Firstly choose one of three classes of your future character.
    
    Three chosen attributes will be higher than other ones.
    
        1. {characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Warrior"]["class"]}
                {characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Warrior"]["description"]}
                {characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Warrior"]["classMainStats"]}
        2. {characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Swordsman"]["class"]}
                {characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Swordsman"]["description"]}
                {characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Swordsman"]["classMainStats"]}
        3. {characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Marksman"]["class"]}
                {characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Marksman"]["description"]}
                {characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Marksman"]["classMainStats"]}
        4. {characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Thief"]["class"]}
                {characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Thief"]["description"]}
                {characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Thief"]["classMainStats"]}
        5. {characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Intellectual"]["class"]}
                {characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Intellectual"]["description"]}
                {characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Intellectual"]["classMainStats"]}
        6. {characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Magician"]["class"]}
                {characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Magician"]["description"]}
                {characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Magician"]["classMainStats"]}
        7. Make it random.
         """))

        if chosenCharacterClass == 1:
            characterClass = characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Warrior"]["class"]
        elif chosenCharacterClass == 2:
            characterClass = characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Swordsman"]["class"]
        elif chosenCharacterClass == 3:
            characterClass = characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Marksman"]["class"]
        elif chosenCharacterClass == 4:
            characterClass = characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Thief"]["class"]
        elif chosenCharacterClass == 5:
            characterClass = characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Intellectual"]["class"]
        elif chosenCharacterClass == 6:
            characterClass = characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Magician"]["class"]
        elif chosenCharacterClass == 7:
            characterClass = None
        else:
            characterClass = None

        return characterClass


    def step_humanoid_classMainStats(characterClass):
        if characterClass == characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Warrior"]["class"]:
            classMainStats = characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Warrior"]["classMainStats"]
        elif characterClass == characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Swordsman"]["class"]:
            classMainStats = characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Swordsman"]["classMainStats"]
        elif characterClass == characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Marksman"]["class"]:
            classMainStats = characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Marksman"]["classMainStats"]
        elif characterClass == characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Thief"]["class"]:
            classMainStats = characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Thief"]["classMainStats"]
        elif characterClass == characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Intellectual"]["class"]:
            classMainStats = characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Intellectual"]["classMainStats"]
        elif characterClass == characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Magician"]["class"]:
            classMainStats = characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Magician"]["classMainStats"]
        elif characterClass is None:
            classMainStats = None
        else:
            classMainStats = None

        return classMainStats


    def step_humanoid(boost):
        while True:
            race = step_humanoid_race()
            name = step_humanoid_name()
            characterClass = step_humanoid_class()
            classMainStats = step_humanoid_classMainStats(characterClass)
            howmany = int(input("How many characters do you need?"))
            for _ in range(howmany):
                stepHumanoid = characterGENERATOR.characterGENERATORclasses.StepHumanoid(race, name, characterClass, classMainStats,
                                                                      boost, language)
                print(stepHumanoid)
            if not repeat():
                wait_a_moment()
                break


    def main_menu():
        while True:
            choiceMainMenu = int(input(f"""What would you do?:
            {characterGENERATOR.characterGENERATORparameters.mainMenu[0]} 
            {characterGENERATOR.characterGENERATORparameters.mainMenu[1]}
            {characterGENERATOR.characterGENERATORparameters.mainMenu[2]}
            {characterGENERATOR.characterGENERATORparameters.mainMenu[3]}
            {characterGENERATOR.characterGENERATORparameters.mainMenu[4]}
            {characterGENERATOR.characterGENERATORparameters.mainMenu[5]}
            {characterGENERATOR.characterGENERATORparameters.mainMenu[6]}
            {characterGENERATOR.characterGENERATORparameters.mainMenu[7]}
            """))

            if choiceMainMenu == 1:
                step_humanoid(boost=0)
            elif choiceMainMenu == 2:
                random_humanoid()
            elif choiceMainMenu == 3:
                step_humanoid(boost=1)
            elif choiceMainMenu == 4:
                step_humanoid(boost=2)
            elif choiceMainMenu == 5:
                step_humanoid(boost=3)
            elif choiceMainMenu == 6:
                global language
                language = "pl"
                continue
            elif choiceMainMenu == 7:
                save_to_file()
            elif choiceMainMenu == 8:
                break
            else:
                print("Please choose 1-6 option")
                wait_a_moment()
                continue


    print(characterGENERATOR.characterGENERATORparameters.welcomeText)
    global language
    language = "eng"
    main_menu()
