import random
import os
import datetime

import characterGENERATOR.characterGENERATORparameters
import characterGENERATOR.characterGENERATORclasses
# import characterGENERATOR.characterGENERATORmain
import mainAPPvariables

language = "eng"
working_file = "Characters.txt"  # working file

# userCommand=None is necessary for every def because of advanced defs.

def help_me(userCommand=None):
    help_text = "\nList of usable commands:\n\n"
    for userCommand in commandDictionary:
        help_text += commandDictionary[userCommand][1] + "\n"
    return help_text


def clear(userCommand=None):
    return "clear"


def exit_app(userCommand=None):
    return "exit"


def back_log(userCommand=None):
    return "[sample text] This is back log output"


def read_file(userCommand=None):
    with open(working_file, 'r', encoding="utf-8") as file:
        content = file.read()
    return content


def save_file(userCommand=None):
    current_time = datetime.datetime.now().strftime("%y%m%d%H%M%S")
    next_file = current_time
    file_path_copy = f"Characters{next_file}.txt"

    if os.path.exists(working_file):
        with open(working_file, 'r') as source:
            with open(file_path_copy, 'w') as destination:
                destination.write(source.read())
        os.remove(working_file)
        return (
            f"Working file {working_file} successfully saved as {file_path_copy}."
            f" Working {working_file} file removed. For delete all files type: 'd d' ")

    else:
        return "Working file doesn't exist. For delete all files type 'd d' "


def delete_file_sudo(userCommand=None):
    if userCommand[2] == "d":
        directory = os.getcwd()
        deleted_files = []

        try:
            for filename in os.listdir(directory):
                if filename.endswith(".txt") and filename.startswith("Characters"):
                    path_to_file = os.path.join(directory, filename)
                    os.remove(path_to_file)
                    deleted_files.append(filename)
        except OSError as e:
            return f"Error: {e}"

        return f"Deleted files: {', '.join(deleted_files)}"
    else:
        return "No file deleted"


def advanced(userCommand):
    if userCommand[0] == "s":
        return step_humanoid_execute(userCommand)
    if userCommand[0] == "d":
        return delete_file_sudo(userCommand)
    else:
        return (mainAPPvariables.defaultUnknownCommandLine1 + userCommand
                + mainAPPvariables.defaultUnknownCommandLine2)


def change_language(userCommand=None):
    global language
    language = "pl"
    return "Zmieniono język wyników na polski"


def save_working_file(data):
    with open(working_file, 'a+', encoding="utf-8") as file:
        file.write(str(data))


def step_humanoid_execute(userCommand):
    race = None
    boost = None
    characterClass = None
    classMainStats = None
    name = None
    setInput = userCommand

    if (len(userCommand) == 4) and (int(userCommand[1]) <= 4) and (int(userCommand[2]) <= 4) and (
            int(userCommand[3]) <= 6):

        if int(userCommand[1]) == 0:
            boost = int(0)
        elif int(userCommand[1]) == 1:
            boost = int(1)
        elif int(userCommand[1]) == 2:
            boost = int(2)
        elif int(userCommand[1]) == 3:
            boost = int(3)
        elif int(userCommand[1]) == 4:
            boost = random.randint(0, 3)

        if int(userCommand[2]) == 0:
            race = characterGENERATOR.characterGENERATORparameters.racesTuple[0]
        elif int(userCommand[2]) == 1:
            race = characterGENERATOR.characterGENERATORparameters.racesTuple[1]
        elif int(userCommand[2]) == 2:
            race = characterGENERATOR.characterGENERATORparameters.racesTuple[2]
        elif int(userCommand[2]) == 3:
            race = characterGENERATOR.characterGENERATORparameters.racesTuple[3]
        elif int(userCommand[2]) == 4:
            race = None

        if userCommand[3] == "0":
            characterClass = characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Warrior"][
                "class"]
            classMainStats = characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Warrior"][
                "classMainStats"]
        elif userCommand[3] == "1":
            characterClass = characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Swordsman"][
                "class"]
            classMainStats = characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Swordsman"][
                "classMainStats"]
        elif userCommand[3] == "2":
            characterClass = characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Marksman"][
                "class"]
            classMainStats = characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Marksman"][
                "classMainStats"]
        elif userCommand[3] == "3":
            characterClass = characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Thief"]["class"]
            classMainStats = characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Thief"][
                "classMainStats"]
        elif userCommand[3] == "4":
            characterClass = characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Intellectual"][
                "class"]
            classMainStats = characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Intellectual"][
                "classMainStats"]
        elif userCommand[3] == "5":
            characterClass = characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Magician"][
                "class"]
            classMainStats = characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Magician"][
                "classMainStats"]
        elif userCommand[3] == "6":
            characterClass = None
            classMainStats = None

        stepHumanoid = characterGENERATOR.characterGENERATORclasses.StepHumanoid(race, name, characterClass,
                                                                                 classMainStats, boost, setInput,
                                                                                 language)

        save_working_file(stepHumanoid)

        return stepHumanoid

    else:
        return (mainAPPvariables.defaultUnknownCommandLine1 + userCommand
                + mainAPPvariables.defaultUnknownCommandLine2)


def random_humanoid_execute(userCommand):
    randomHumanoid = characterGENERATOR.characterGENERATORclasses.RandomHumanoid(language)

    save_working_file(randomHumanoid)

    return randomHumanoid


def step_humanoid_info(userCommand=None):
    return f"""
Please choose below options:

Boost : 
    {characterGENERATOR.characterGENERATORparameters.guiBoosters[0]} [0]
    {characterGENERATOR.characterGENERATORparameters.guiBoosters[1]} [1]
    {characterGENERATOR.characterGENERATORparameters.guiBoosters[2]} [2]
    {characterGENERATOR.characterGENERATORparameters.guiBoosters[3]} [3]
    Random [4]
                
Race :  
    {characterGENERATOR.characterGENERATORparameters.racesTuple[0]} [0]
    {characterGENERATOR.characterGENERATORparameters.racesTuple[1]} [1]
    {characterGENERATOR.characterGENERATORparameters.racesTuple[2]} [2]
    {characterGENERATOR.characterGENERATORparameters.racesTuple[3]} [3]
    Random [4]
    
Character class :
    {characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Warrior"]["class"]} [0]
    {characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Swordsman"]["class"]} [1]
    {characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Marksman"]["class"]} [2]
    {characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Thief"]["class"]} [3]
    {characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Intellectual"]["class"]} [4]
    {characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Magician"]["class"]} [5]
    Random [6]
    
Example :
Create step by step humanoid, with no boost, Dwarf, Swordsman: s021
    
Or ask for more information about Character classes [7] or boosters [8]
        
"""


def character_classes_info(userCommand=None):
    return f"""
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
"""


def boosters_info(userCommand=None):
    return f"""
Boosters, in order:

    for main stats : {characterGENERATOR.characterGENERATORparameters.boosters["boostersMainStats"]}
    for other stats : {characterGENERATOR.characterGENERATORparameters.boosters["boostersOtherStats"]}
    for attack points : {characterGENERATOR.characterGENERATORparameters.boosters["boosterAttack"]}
    for wound points : {characterGENERATOR.characterGENERATORparameters.boosters["boosterWounds"]}

"""


commandDictionary = {
    "h": [help_me, "[h]elp - display list of usable commands"],
    "c": [clear, "[c]lear - clean output data box"],
    "e": [exit_app, "[e]xit the application"],
    "r": [read_file, "[r]ead working file"],
    "sa": [save_file, "[sa]ve working file"],

    "l": [change_language, "[l] results language change / zmiana języka wyników"],

    "1": [step_humanoid_info, "[1] - Create humanoid - step by step. Auto save."],
    "2": [random_humanoid_execute, "[2] - Create humanoid fully random, no boost. Auto save"],

    "7": [character_classes_info, "[7] - More information about character classes"],
    "8": [boosters_info, "[8] - More information about boosters"],

}

commandListAdvanced = [
    "s",  # step_humanoid_execute
    "d",  # delete all characters files, sudo mode

]
