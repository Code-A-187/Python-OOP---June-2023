from typing import List

from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT_TYPES = {"KneePad": KneePad,
                             "ElbowPad": ElbowPad
                             }
    VALID_TEAMS_TYPES = {"OutdoorTeam": OutdoorTeam,
                         "IndoorTeam": IndoorTeam
                         }

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[KneePad, ElbowPad] = []
        self.teams: List[IndoorTeam, OutdoorTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")

        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.VALID_EQUIPMENT_TYPES:
            raise Exception("Invalid equipment type!")
        created_equipment = self.VALID_EQUIPMENT_TYPES[equipment_type]()
        self.equipment.append(created_equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAMS_TYPES:
            raise Exception("Invalid team type!")
        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."
        created_team = self.VALID_TEAMS_TYPES[team_type](team_name, country, advantage)
        self.teams.append(created_team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        team_obj = object
        for team in self.teams:
            if team.name == team_name:
                team_obj = team
                break
        obj_index = 0
        equipment_obj = object
        for equipment in self.equipment[::-1]:
            if equipment.__class__.__name__ == equipment_type:
                equipment_obj = equipment
                break

        if team_obj.budget < equipment_obj.price:
            raise Exception("Budget is not enough!")

        team_obj.equipment.append(self.equipment.pop(obj_index))
        team_obj.budget -= equipment_obj.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        try:
            team_obj = next(filter(lambda team: team.name == team_name, self.teams))
        except StopIteration:
            raise Exception("No such team!")

        if team_obj.wins > 0:
            raise Exception(f"The team has {team_obj.wins} wins! Removal is impossible!")

        self.teams.remove(team_obj)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        number_of_changed_equipment = 0

        for equipment in self.equipment:
            if equipment.__class__.__name__ == equipment_type:
                number_of_changed_equipment += 1
                equipment.increase_price()

        return f"Successfully changed {number_of_changed_equipment}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team_1_obj = [t for t in self.teams if t.name == team_name1][0]
        team_2_obj = [t for t in self.teams if t.name == team_name2][0]

        if team_1_obj.__class__.__name__ != team_2_obj.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        team_1_score = team_1_obj.advantage + sum([e.protection for e in team_1_obj.equipment])
        team_2_score = team_2_obj.advantage + sum([e.protection for e in team_2_obj.equipment])

        if team_1_score == team_2_score:
            return "No winner in this game."

        elif team_1_score > team_2_score:
            team_1_obj.win()
            return f"The winner is {team_1_obj.name}."

        elif team_1_score < team_2_score:
            team_2_obj.win()
            return f"The winner is {team_2_obj.name}."

    def get_statistics(self):
        result = [f"Tournament: {self.name}",
                  f"Number of Teams: {len(self.teams)}",
                  f"Teams:",
                  ]

        for team in sorted(self.teams, key=lambda x: -x.wins):
            result.append(str(team.get_statistics()))

        return "\n".join(result)
