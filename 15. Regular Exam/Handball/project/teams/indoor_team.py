from typing import List

from project.teams.base_team import BaseTeam
from project.equipment.base_equipment import BaseEquipment


class IndoorTeam(BaseTeam):
    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, budget=500.0)
        self.equipment: List[BaseEquipment] = []

    def win(self):
        self.advantage += 145
        self.wins += 1
