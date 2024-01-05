from typing import List
from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms: List[Room] = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        room_total_price = sum([room.room_cost for room in self.rooms])
        room_total_expenses = sum([room.expenses for room in self.rooms])
        return f"Monthly consumption: {room_total_expenses + room_total_price:.2f}$."

    def pay(self):
        return_result = []
        for room in self.rooms:
            total_cost = room.expenses + room.room_cost

            # Apparently room is family for this loop
            if room.budget >= total_cost:
                room.budget -= total_cost
                return_result.append(f"{room.family_name} paid {total_cost:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                self.rooms.remove(room)
                return_result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
        return '\n'.join(return_result)

    def status(self):
        all_people = sum([room.members_count for room in self.rooms])
        result = [f"Total population: {all_people}"]
        for room in self.rooms:
            result.append(
                f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$")
            children_cost = 0
            if room.children:
                n = 1
                for child in room.children:
                    children_cost += child.get_monthly_expense()
                    result.append(f"--- Child {n} monthly cost: {child.get_monthly_expense():.2f}$")
                    n += 1
            result.append(f"--- Appliances monthly cost: {room.expenses - children_cost:.2f}$")

        return "\n".join(result)
