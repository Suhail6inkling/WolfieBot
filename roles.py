from wolfiebot import *
from config import *

role_categories_list = ["Chaos", "Counteractive", "Investigative", "Killing", "Protective", "Support"]
alignments = ["Good", "Evil", "Neutral"]
attack_save_strengths = ["Standard", "Strong", "Powerful", "Unstoppable"]
save_durations = ["Active", "Lunar", "Queued"]
species_list = ["Human", "Wolf", "Non-Human"]

class Role():
    name = None
    isUnique = False
    isAchievable = False
    alignment = "Neutral"
    species = "Human"

class Save():
    def __init__(self, strength, duration, special=None):
        self.strength = strength
        self.duration = duration
        self.special = special

    def use(self, user):
        if self.special == "infect":
            user.role = Werewolf()
            user.alignment = "Evil"

class Attack():
    def __init__(self, user, strength, special=None):
        self.user = user
        self.strength = strength
        self.special = special

    def use(self, user, target):
        return

class Player():
    def __init__(self, user, chan, role, *modifiers):
        self.user = user
        self.privchannel = chan
        self.role = role
        self.alignment = role.alignment
        self.objectives = role.objectives
        self.modifiers = list(modifiers)
        self.isAlive = True
        self.saves = role.saves
        self.tags = role.tags

    def attacked(self, attack):
        for save in self.saves:
            if save.strength >= attack.strength:
                self.saves.remove(save)
                save.use(self)
                return "saved"
        attack.use(attack.user,self)
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
    alignment = "Good"
    categories = ["Investigative"]
    objectives = ["good-standard"]
    saves = []
    tags = {"Good", "Investigative", "Human"}

    def __init__(self):
        self.actions = {"Investigate" : -1, "Publish" : 1}
        self.invest_targets = []

    def investigate(self, user, target):
        if hasattr(user.role,"invest_targets"):
            if target.alignment == "Evil" and target not in user.role.invest_targets and user.role.name == "Seer":
                user.role.invest_targets.append(target)
                user.saves.append(Save(1,2))
                return target.role.name, target.alignment
        if hasattr(user.role,"invest_targets"):
            user.role.invest_targets.append(target)
        return target.role.name, target.alignment

    ongamestart_abilities = []
    ondaystart_abilities = []
    onnightstart_abilities = []
    ontarget_abilities = []

class Werewolf(Role):
    name = "Werewolf"
    alignment = "Evil"
    species = "Wolf"
    categories = ["Killing"]
    objectives = ["evil-standard"]
    saves = []
    tags = {"Evil", "Killing", "Wolf"}

    def __init__(self):
        self.actions = {"Maul" : -1, "Pack Offensive" : 1}

    def maul(self, user, target):
        result = target.attacked(Attack(user,1))

    ongamestart_abilities = []
    ondaystart_abilities = []
    onnightstart_abilities = []
    ontarget_abilities = []
