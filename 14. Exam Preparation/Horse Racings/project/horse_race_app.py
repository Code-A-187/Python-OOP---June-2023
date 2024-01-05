from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_HORSES_TYPES = {"Appaloosa": Appaloosa,
                          "Thoroughbred": Thoroughbred
                          }

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):

        for h in self.horses:
            if h.name == horse_name:
                raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in self.VALID_HORSES_TYPES:
            created_horse = self.VALID_HORSES_TYPES[horse_type](horse_name, horse_speed)
            self.horses.append(created_horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        for j in self.jockeys:
            if j.name == jockey_name:
                raise Exception(f"Jockey {jockey_name} has been already added!")

        created_jockey = Jockey(jockey_name, age)
        self.jockeys.append(created_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        for race in self.horse_races:
            if race.race_type == race_type:
                raise Exception(f"Race {race_type} has been already created!")

        created_horse_race = HorseRace(race_type)
        self.horse_races.append(created_horse_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):

        try:
            jockey_obj = next(filter(lambda jockey: jockey.name == jockey_name, self.jockeys))
        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        for horse in self.horses:
            if not horse.is_taken and horse.__class__.__name__ == horse_type:
                horse_obj = horse
                break
        else:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey_obj.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey_obj.horse = horse_obj
        horse_obj.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse_obj.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        try:
            race_obj = next(filter(lambda race: race.race_type == race_type, self.horse_races))
        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        try:
            jockey_obj = next(filter(lambda jockey: jockey.name == jockey_name, self.jockeys))
        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey_obj.horse:
            return f"Jockey {jockey_name} cannot race without a horse!"

        if jockey_obj in race_obj.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race_obj.jockeys.append(jockey_obj)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        for race in self.horse_races:
            if race.race_type == race_type:
                race_obj = race
                break
        else:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race_obj.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        best_race_speed = 0
        winner_obj = ''

        for jockey in race_obj.jockeys:
            if jockey.horse.speed > best_race_speed:
                winner_obj = jockey
                best_race_speed = winner_obj.horse.speed

        return f"The winner of the {race_type} race, " \
               f"with a speed of {best_race_speed}km/h is {winner_obj.name}! " \
               f"Winner's horse: {winner_obj.horse.name}."
