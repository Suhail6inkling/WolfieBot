import random
from wolfiebot import *

role_categories_list = ["Chaos", "Counteractive", "Investigative", "Killing", "Protective", "Support"]
alignments = ["Good", "Evil", "Neutral"]
attack_save_strengths = ["Standard", "Strong", "Powerful", "Unstoppable"]
save_durations = ["Lunar", "Active", "Queued"]
species_list = ["Human", "Wolf", "Non-Human"]

class Role():
    pass

class Save():
    def __init__(self, strength, duration, special=None):
        self.strength = strength
        self.duration = duration
        self.special = special

    def use(self, user):
        if type(self.special) is list:
            if self.special[0] == "infect":
                user.changerole(Werewolf(self.special[1]))

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
        self.species = role.species
        self.objectives = role.objectives
        self.modifiers = list(modifiers)
        self.isAlive = True
        self.saves = role.saves
        self.tags = role.tags
        if self.species == "Wolf":
            role.wolves.addmember(self)

    def changerole(self, role):
        oldrole = self.role
        self.role = role
        self.alignment = role.alignment
        self.species = role.species
        self.objectives = role.objectives
        self.tags = role.tags
        if self.species == "Wolf":
            role.wolves.addmember(self)
        elif oldrole.species == "Wolf":
            oldrole.wolves.removemember(self)
    
    def attacked(self, attack):
        for save in self.saves:
            if save.strength >= attack.strength:
                self.saves.remove(save)
                save.use(self)
                return "saved"
        attack.use(attack.user,self)
        self.isAlive = False
        return ["killed",attack.user.role.name]

    def suicide(self):
        self.isAlive = False
        return "suicided"

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
        self.actions = {"Investigate" : [-1,"night",self.investigate], "Publish" : [1,"night",self.publish]}
        self.invest_results = []

    def investigate(self, user, target):
        if self.actions["Investigate"][0] == 0:
            return "expended"
        self.actions["Investigate"][0] = self.actions["Investigate"][0] - 1
        if hasattr(user.role,"invest_results"):
            if target.alignment == "Evil" and target not in user.role.invest_results and user.role.name == "Seer":
                user.role.invest_results[target] = [target.role.name, target.alignment]
                user.saves.append(Save(1,2))
                return [target.role.name, target.alignment]
        if hasattr(user.role,"invest_targets"):
            user.role.invest_results[target] = [target.role.name, target.alignment]
        return [target.role.name, target.alignment]

    def publish(self, user, target):
        if self.actions["Publish"] == 0:
            return "expended"
        self.actions["Publish"] = self.actions["Publish"] - 1
        if not hasattr(user.role,"invest_results"):
            return "fail"
        if target not in user.role.invest_results:
            return "fail"
        return user.role.invest_results[target]

    ongamestart_abilities = []
    ondaystart_abilities = []
    onnightstart_abilities = []
    ontarget_abilities = []
    ondeath_abilities = []

class Wolves():
    name = "Wolves"

    class role():
        name = "Wolves"
        alignment = "Evil"
        species = "Wolf"
        categories = ["Killing"]

    def __init__(self, chan):
        self.channel = chan
        self.actions = {"Maul" : [-1,"night",self.maul], "Pack Offensive" : [0,"night",self.packoffensive]}
        self.members = []

    def addmember(self, player):
        if player not in self.members:
            self.members.append(player)

    def removemember(self, player):
        if player in self.members:
            self.members.remove(player)

    def maul(self, user, target):
        if self.actions["Maul"][0] == 0:
            return "expended"
        self.actions["Maul"][0] = self.actions["Maul"][0] - 1
        target.attacked(Attack(user,1))
        return "success"

    def packoffensive(self, *targets):
        if self.actions["Pack Offensive"][0] == 0:
            return "expended"
        if len(self.members) != len(targets):
            return "tryagain"
        self.actions["Pack Offensive"][0] = self.actions["Pack Offensive"][0] - 1
        random.shuffle(targets)
        for i in range(0,len(self.members)):
            wolf = self.members[i]
            wolf.role.packoffensive(wolf,targets[i])
        return "success"

    def n3_gain_use(self):
        self.actions["Pack Offensive"][0] = 1

class Direwolf(Role):
    name = "Direwolf"
    alignment = "Evil"
    species = "Wolf"
    categories = ["Killing","Support"]
    objectives = ["evil-standard"]
    saves = []
    tags = {"Evil", "Killing", "Support", "Wolf", "Unique"}

    def __init__(self, wolves):
        self.actions = dict(wolves.actions)
        self.actions["Infect"] = [-1,"night",self.infect]
        self.wolves = wolves

    def packoffensive(self, user, target):
        target.attacked(Attack(user,0))

    def infect(self, user, target):
        if self.actions["Infect"][0] == 0:
            return "expended"
        if target in self.wolves.members:
            return "fail"
        self.actions["Infect"][0] = self.actions["Infect"][0] - 1
        target.saves.append(Save(3,1,["infect",self.wolves]))
        return "success"

    def po_gain_use(self, user):
        if DayCount == 3 and Day == False:
            self.wolves.n3_gain_use()

    def refresh_actions(self, user):
        self.actions["Maul"] = self.wolves.actions["Maul"]
        self.actions["Pack Offensive"] = self.wolves.actions["Pack Offensive"]

    ongamestart_abilities = []
    ondaystart_abilities = [refresh_actions]
    onnightstart_abilities = [po_gain_use]
    ontarget_abilities = []
    ondeath_abilities = []

class Werewolf(Role):
    name = "Werewolf"
    alignment = "Evil"
    species = "Wolf"
    categories = ["Killing"]
    objectives = ["evil-standard"]
    saves = []
    tags = {"Evil", "Killing", "Wolf"}

    def __init__(self, wolves):
        self.actions = dict(wolves.actions)
        self.wolves = wolves

    def packoffensive(self, user, target):
        target.attacked(Attack(user,0))

    def po_gain_use(self, user):
        if DayCount == 3 and Day == False:
            self.wolves.n3_gain_use()

    def refresh_actions(self, user):
        self.actions["Maul"] = self.wolves.actions["Maul"]
        self.actions["Pack Offensive"] = self.wolves.actions["Pack Offensive"]

    ongamestart_abilities = []
    ondaystart_abilities = [refresh_actions]
    onnightstart_abilities = [po_gain_use]
    ontarget_abilities = []
    ondeath_abilities = []
