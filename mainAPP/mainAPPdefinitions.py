import characterGENERATOR.characterGENERATORparameters


def help_me():
    help_text = "\nList of usable commands:\n\n"
    for userCommand in commandDictionary:
        help_text += commandDictionary[userCommand][1] + "\n"
    return help_text


def clear():
    return "clear"


def exit_app():
    return "exit"


def back_log():
    return "[sample text] This is back log output"


def step_humanoid():
    return f"""
    
Please choose below options:

Boost : 
    {characterGENERATOR.characterGENERATORparameters.guiBoosters[0]} [0]
    {characterGENERATOR.characterGENERATORparameters.guiBoosters[1]} [1]
    {characterGENERATOR.characterGENERATORparameters.guiBoosters[2]} [2]
    {characterGENERATOR.characterGENERATORparameters.guiBoosters[3]} [3]
                
Race :  
    {characterGENERATOR.characterGENERATORparameters.racesTuple[0]} [0]
    {characterGENERATOR.characterGENERATORparameters.racesTuple[1]} [1]
    {characterGENERATOR.characterGENERATORparameters.racesTuple[2]} [2]
    {characterGENERATOR.characterGENERATORparameters.racesTuple[3]} [3]
    
Character class :
    {characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Warrior"]["class"]} [0]
    {characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Swordsman"]["class"]} [1]
    {characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Marksman"]["class"]} [2]
    {characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Thief"]["class"]} [3]
    {characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Intellectual"]["class"]} [4]
    {characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Magician"]["class"]} [5]

Example :
    Create step by step humanoid, with no boost, Dwarf, Swordsman: 021
    
Or ask for more information about Character classes [7] or boosters [8]
        
"""


def character_classes_info():
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


def boosters_info():
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

    # sample functions:

    "1": [step_humanoid, "[1] - Create humanoid - step by step"],

    "7": [character_classes_info, "[7] - More information about character classes"],
    "8": [boosters_info, "[8] - More information about boosters"],

}
