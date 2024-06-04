import characterGENERATOR.characterGENERATORparameters
import random
import faker
import copy


class RandomHumanoid:
    instances = {}

    def __init__(self, language="eng"):
        self.language = language
        self.race = random.choice(
            [characterGENERATOR.characterGENERATORparameters.humanoidRacesStats["Human"]["race"],
             characterGENERATOR.characterGENERATORparameters.humanoidRacesStats["Elf"]["race"],
             characterGENERATOR.characterGENERATORparameters.humanoidRacesStats["Dwarf"]["race"],
             characterGENERATOR.characterGENERATORparameters.humanoidRacesStats["Halfing"]["race"]])
        self.self_name()
        self.simpleId = self.simple_id()
        for stat in ["ws", "bs", "s", "t", "ag", "int", "wp", "fel"]:
            setattr(self, stat, characterGENERATOR.characterGENERATORparameters.humanoidRacesStats[self.race][stat]
                    + self.generate_main_stat_random())
        self.a = characterGENERATOR.characterGENERATORparameters.humanoidRacesStats[self.race]["a"]
        self.w = random.choices(characterGENERATOR.characterGENERATORparameters.humanoidRacesStats[self.race]["wValues"],
                                characterGENERATOR.characterGENERATORparameters.humanoidRacesStats[self.race]["wWeights"])[0]
        self.sb = (self.s // 10)
        self.tb = (self.t // 10)
        self.m = characterGENERATOR.characterGENERATORparameters.humanoidRacesStats[self.race]["m"]
        self.mag = characterGENERATOR.characterGENERATORparameters.humanoidRacesStats[self.race]["mag"]
        self.ip = characterGENERATOR.characterGENERATORparameters.humanoidRacesStats[self.race]["ip"]
        self.fp = random.choices(characterGENERATOR.characterGENERATORparameters.humanoidRacesStats[self.race]["fpValues"],
                                 characterGENERATOR.characterGENERATORparameters.humanoidRacesStats[self.race]["fpWeights"])[0]

        RandomHumanoid.instances[self.simpleId] = [self.race, self.name, self.ws, self.bs,
                                                   self.s, self.t, self.ag, self.int, self.wp, self.fel,
                                                   self.a, self.w, self.sb, self.tb, self.m, self.mag,
                                                   self.ip, self.fp]

    @staticmethod
    def generate_main_stat_random():
        MainStatRandomRandrange = 0
        while MainStatRandomRandrange <= 6:
            MainStatRandomRandrange = random.randrange(10) + random.randrange(10)
        return MainStatRandomRandrange

    def self_name(self):

        fakeName = faker.Faker(use_weighting=False)

        if self.race == "Human":
            fakeName.locale = "de_DE"
        elif self.race == "Elf":
            fakeName.locale = "fr_FR"
        elif self.race == "Dwarf":
            fakeName.locale = "no_NO"
        elif self.race == "Halfing":
            fakeName.locale = "nl_NL"

        self.firstName = fakeName.first_name()
        self.lastName = fakeName.last_name()
        self.name = self.firstName + " " + self.lastName

        return self.name

    def __str__(self):
        if self.language in ("ENG", "Eng", "eng", "en", "e"):
            return (f"""
Your random humanoid is: 
    {self.race}, {self.firstName} {self.lastName}
Main characteristics:
    ws:{self.ws}, bs:{self.bs}, s:{self.s}, t:{self.t}, ag:{self.ag}, int:{self.int}, wp:{self.wp}, fel:{self.fel}
Second characteristics:
    a:{self.a}, w:{self.w}, sb:{self.sb}, tb:{self.tb}, m:{self.m}, mag:{self.mag}, ip:{self.ip}, fp:{self.fp}
id:{self.simpleId}
""")
        else:
            return (f"""
Twój losowy humanoid to:
    {self.race}, {self.firstName} {self.lastName}
Cechy główne: 
    ww:{self.ws}, us:{self.bs}, k:{self.s}, odp:{self.t}, zr:{self.ag}, int:{self.int}, sw:{self.wp}, ogd:{self.fel}
Cechy drugorzędne: 
    a:{self.a}, zyw:{self.w}, s:{self.sb}, wt:{self.tb}, sz:{self.m}, mag:{self.mag}, po:{self.ip}, ps:{self.fp}
id:{self.simpleId}
""")

    def simple_id(self):
        simpleId = ''.join([self.firstName[:characterGENERATOR.characterGENERATORparameters.simpleIdRules["lenName"]],
                            self.race[:characterGENERATOR.characterGENERATORparameters.simpleIdRules["lenRace"]],
                            str(random.randint(111, 999))])
        while simpleId in RandomHumanoid.instances:
            simpleId += str(random.randint(1, 9))
        return simpleId


class StepHumanoid:
    instances = {}

    def __init__(self, race, name, characterClass, classMainStats, boost, language="eng"):
        self.boost = boost
        self.characterClass = self.characterClassChoice(characterClass)
        self.booster()
        self.language = language
        self.race = self.raceChoice(race)
        self.name = self.nameChoice(name, self.race)
        self.simpleId = self.simple_id()
        self.randomStats = self.generate_main_stats_random()
        self.stats = characterGENERATOR.characterGENERATORparameters.stats
        self.classStatsChoice(classMainStats)
        self.baseRandomStats = copy.copy(self.randomStats)

        for stat in self.classMainStats:
            setattr(self, stat, max(self.randomStats) + characterGENERATOR.characterGENERATORparameters.humanoidRacesStats[self.race][stat]
                    + self.boostMainStats)
            self.randomStats.pop()

        for stat in self.classOtherStats:
            setattr(self, stat, max(self.randomStats) + characterGENERATOR.characterGENERATORparameters.humanoidRacesStats[self.race][stat]
                    + self.boostOtherStats)
            self.randomStats.pop()

        self.a = characterGENERATOR.characterGENERATORparameters.humanoidRacesStats[self.race]["a"] + self.boostAtack
        self.w = (random.choices(characterGENERATOR.characterGENERATORparameters.humanoidRacesStats[self.race]["wValues"],
                                 characterGENERATOR.characterGENERATORparameters.humanoidRacesStats[self.race]["wWeights"])[0]
                  + self.boostWounds)
        self.sb = (self.s // 10)
        self.tb = (self.t // 10)
        self.m = characterGENERATOR.characterGENERATORparameters.humanoidRacesStats[self.race]["m"]
        self.mag = characterGENERATOR.characterGENERATORparameters.humanoidRacesStats[self.race]["mag"]
        self.ip = characterGENERATOR.characterGENERATORparameters.humanoidRacesStats[self.race]["ip"]
        self.fp = random.choices(characterGENERATOR.characterGENERATORparameters.humanoidRacesStats[self.race]["fpValues"],
                                 characterGENERATOR.characterGENERATORparameters.humanoidRacesStats[self.race]["fpWeights"])[0]

        StepHumanoid.instances[self.simpleId] = [self.race, self.name, self.ws, self.bs,
                                                 self.s, self.t, self.ag, self.int, self.wp, self.fel,
                                                 self.a, self.w, self.sb, self.tb, self.m, self.mag,
                                                 self.ip, self.fp, self.characterClass, ]

    def raceChoice(self, race):
        if race is not None:
            return race
        else:
            return random.choice(
                [characterGENERATOR.characterGENERATORparameters.humanoidRacesStats["Human"]["race"],
                 characterGENERATOR.characterGENERATORparameters.humanoidRacesStats["Elf"]["race"],
                 characterGENERATOR.characterGENERATORparameters.humanoidRacesStats["Dwarf"]["race"],
                 characterGENERATOR.characterGENERATORparameters.humanoidRacesStats["Halfing"]["race"]])

    def nameChoice(self, name, race):
        if name is not None:
            return name
        else:
            fakeName = faker.Faker(use_weighting=False)
            if race == "Human":
                fakeName.locale = "de_DE"
            elif race == "Elf":
                fakeName.locale = "fr_FR"
            elif race == "Dwarf":
                fakeName.locale = "no_NO"
            elif race == "Halfing":
                fakeName.locale = "nl_NL"

            name = f"{fakeName.first_name()} {fakeName.last_name()}"

        return name

    def characterClassChoice(self, characterClass):
        if characterClass is not None:
            return characterClass
        else:
            return random.choice(
                [characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Warrior"]["class"],
                 characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Swordsman"]["class"],
                 characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Marksman"]["class"],
                 characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Thief"]["class"],
                 characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Intellectual"]["class"],
                 characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Magician"]["class"]])

    def classStatsChoice(self, classMainStats):
        if classMainStats is not None:
            self.classMainStats = classMainStats
            self.classOtherStats = [stat for stat in characterGENERATOR.characterGENERATORparameters.stats if
                                    stat not in self.classMainStats]
        else:
            self.classMainStats = characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses[self.characterClass][
                "classMainStats"]
            self.classOtherStats = [stat for stat in characterGENERATOR.characterGENERATORparameters.stats if
                                    stat not in self.classMainStats]

    def booster(self):
        self.boostMainStats = 0
        self.boostOtherStats = 0
        self.boostAtack = 0
        self.boostWounds = 0
        if self.boost == 1:
            self.boostMainStats = characterGENERATOR.characterGENERATORparameters.boosters["boostersMainStats"][0]
            self.boostOtherStats = characterGENERATOR.characterGENERATORparameters.boosters["boostersOtherStats"][0]
            if self.characterClass in [characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Warrior"]["class"],
                                       characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Swordsman"]["class"],
                                       characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Marksman"]["class"]]:
                self.boostAtack = characterGENERATOR.characterGENERATORparameters.boosters["boosterAttack"][0]
                self.boostWounds = characterGENERATOR.characterGENERATORparameters.boosters["boosterWounds"][0]
            else:
                self.boostAtack = 0
                self.boostWounds = 0
        elif self.boost == 2:
            self.boostMainStats = characterGENERATOR.characterGENERATORparameters.boosters["boostersMainStats"][1]
            self.boostOtherStats = characterGENERATOR.characterGENERATORparameters.boosters["boostersOtherStats"][1]
            if self.characterClass in [characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Warrior"]["class"],
                                       characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Swordsman"]["class"],
                                       characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Marksman"]["class"]]:
                self.boostAtack = characterGENERATOR.characterGENERATORparameters.boosters["boosterAttack"][1]
                self.boostWounds = characterGENERATOR.characterGENERATORparameters.boosters["boosterWounds"][1]
            else:
                self.boostAtack = 0
                self.boostWounds = characterGENERATOR.characterGENERATORparameters.boosters["boosterWounds"][0]
        elif self.boost == 3:
            self.boostMainStats = characterGENERATOR.characterGENERATORparameters.boosters["boostersMainStats"][2]
            self.boostOtherStats = characterGENERATOR.characterGENERATORparameters.boosters["boostersOtherStats"][2]
            if self.characterClass in [characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Warrior"]["class"],
                                       characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Swordsman"]["class"],
                                       characterGENERATOR.characterGENERATORparameters.humanoidCharacterClasses["Marksman"]["class"]]:
                self.boostAtack = characterGENERATOR.characterGENERATORparameters.boosters["boosterAttack"][2]
                self.boostWounds = characterGENERATOR.characterGENERATORparameters.boosters["boosterWounds"][2]
            else:
                self.boostAtack = 0
                self.boostWounds = characterGENERATOR.characterGENERATORparameters.boosters["boosterWounds"][1]

    def __str__(self):
        if self.language in ("ENG", "Eng", "eng", "en", "e"):
            return (f"""
Your humanoid is: 
    {self.race}, {self.characterClass}, {self.name} 
Your 8 x 2k10 rolls(after under 6 result rejected):
    {self.baseRandomStats}
Main characteristics:
    ws:{self.ws}, bs:{self.bs}, s:{self.s}, t:{self.t}, ag:{self.ag}, int:{self.int}, wp:{self.wp}, fel:{self.fel}
Second characteristics: 
    a:{self.a}, w:{self.w}, sb:{self.sb}, tb:{self.tb}, m:{self.m}, mag:{self.mag}, ip:{self.ip}, fp:{self.fp}
id:{self.simpleId}
""")
        else:
            return (f"""
Twój humanoid to:
    {self.race}, {self.characterClass}, {self.name} 
Twoje rzuty 8 x 2k10 ( po odrzuceniu wyników poniżej 6)
    {self.baseRandomStats}
Cechy główne: 
    ww:{self.ws}, us:{self.bs}, k:{self.s}, odp:{self.t}, zr:{self.ag}, int:{self.int}, sw:{self.wp}, ogd:{self.fel}
Cechy drugorzędne: 
    a:{self.a}, zyw:{self.w}, s:{self.sb}, wt:{self.tb}, sz:{self.m}, mag:{self.mag}, po:{self.ip}, ps:{self.fp}
id:{self.simpleId}
""")

    @staticmethod
    def generate_main_stat_random():
        MainStatRandomRandrange = 0
        while MainStatRandomRandrange <= 6:
            MainStatRandomRandrange = random.randrange(10) + random.randrange(10)
        return MainStatRandomRandrange

    @staticmethod
    def generate_main_stats_random():
        randomStats = []
        for stat in range(8):
            stat = StepHumanoid.generate_main_stat_random()
            randomStats.append(stat)
        randomStats.sort()
        return randomStats

    def simple_id(self):
        simpleId = ''.join([self.name[:characterGENERATOR.characterGENERATORparameters.simpleIdRules["lenName"]],
                            self.race[:characterGENERATOR.characterGENERATORparameters.simpleIdRules["lenRace"]],
                            str(random.randint(111, 999))])
        while simpleId in StepHumanoid.instances:
            simpleId += str(random.randint(1, 9))
        return simpleId
