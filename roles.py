from wolfiebot import *
from config import *

role_categories_list = ["chaos", "counteractive", "investigative", "killing", "protective", "support"]
alignments = ["Good", "Evil", "Neutral"]
attack_save_strengths = ["Standard", "Strong", "Powerful", "Unstoppable"]
save_durations = ["active", "lunar", "queued"]
species_list = ["Human", "Wolf", "Non-Human"]

class Role():
    isUnique = False
    isAchievable = False
    alignment = "Neutral"
    species = "Human"

    def __init__(self):
        self.tags = []
        self.role_categories = []
        self.saves = []
        if self.isUnique:
            self.tags.append("Unique")
        if self.isAchievable:
            self.tags.append("Achievable")
        self.tags.append(self.alignment)
        self.tags.append(self.species)
        for category in self.role_categories:
            self.tags.append(category)

class Save():
    def __init__(self, strength, duration):
        self.strength = strength
        self.duration = duration

class Attack():
    def __init__(self, strength, duration):
        self.strength = strength

class Player():
    def __init__(self, role):
        self.role = role
        self.alignment = role.alignment
        self.objectives = role.objectives
        self.isAlive = True
        self.saves = role.saves
        self.action_targets = {a : [] for a in role.actions}

    def attacked(self, attack):
        for save in self.saves:
            if save.strength >= attack.strength:
                self.saves.remove(save)
                return "saved"
        self.isAlive = False
        return "killed"

    def suicide(self):
        self.isAlive = False
        return "Suicided"

    def isWinner(self, game_objectives):
        for objective in game_objectives:
            if objective in self.objectives:
                return True
        return False

class Seer(Role):
    name = "Seer"
    actions = {"Investigate" : -1, "Publish" : 1}
    objectives = ["good-standard"]
    alignment = "Good"

    def __init__(self):
        super().__init__()
        role_categories = ["investigative"]

    def investigate(self, target):
        if target.alignment == "Evil" and target not in self.investigated_list:
            self.action_targets["Investigate"].append(target)
            return target.role.__name__, target.alignment, Save(1, 2)
        self.action_targets["Investigate"].append(target)
        return target.role.name, target.alignment

class Werewolf(Role):
    name = "Werewolf"
    actions = {"Maul" : -1, "Pack Offensive" : 1}
    objectives = ["evil-standard"]
    alignment = "Evil"

    def __init__(self):
        super().__init__()
        role_categories = ["killing"]

    def maul(self, target):
        result = target.attacked(Attack(1))
