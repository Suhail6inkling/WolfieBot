import random
import asyncio
import discord
from wolfiebot import *

role_categories_list = ["Chaos", "Counteractive", "Investigative", "Killing", "Protective", "Support"]
alignments = ["Good", "Evil", "Neutral"]
attack_save_strengths = ["Standard", "Strong", "Powerful", "Unstoppable"]
save_durations = ["Lunar", "Active", "Queued"]
species_list = ["Human", "Adept", "Ethereal", "Unearthly", "Wolf"]

class Role():
    def __init__(self):
        self.ongamestart_abilities = []
        self.ondaystart_abilities = []
        self.onnightstart_abilities = []
        self.ontarget_abilities = []
        self.onattack_abilities = []
        self.ondeath_abilities = []

class Modifier(Role):
    def __init__(self):
        super().__init__()

class Faction():
    pass

class Action():
    def __init__(self, name, function, user, *args):
        self.name = name
        self.function = function
        self.user = user
        self.args = args
        self.fail = False
        self.giveinstead = None
        user.actions[name][0] = user.actions[name][0] - 1

class Save():
    def __init__(self, strength, duration, special=None):
        self.strength = strength
        self.duration = duration
        self.special = special

    async def use(self, user):
        if type(self.special) is list:
            if self.special[0] == "infect":
                user.changerole(Werewolf(self.special[1]))

class Attack():
    def __init__(self, user, target, strength, special=None):
        self.user = user
        self.target = target
        self.strength = strength
        self.special = special
        self.saved = False

    async def use(self, user, target):
        return

class Player():
    def __init__(self, user, chan, role, *modifiers):
        self.user = user
        self.privchannel = chan
        self.role = role
        self.alignment = role.alignment
        self.species = role.species
        self.objectives = role.objectives
        self.modifiers = modifiers
        self.actions = role.actions
        for m in modifiers:
            self.actions.update(m.actions)
        self.isAlive = True
        self.saves = role.saves
        self.tags = role.tags
        if hasattr(self.role,"faction"):
            self.role.faction.addmember(self)

    def changerole(self, role):
        oldrole = self.role
        self.role = role
        self.alignment = role.alignment
        self.species = role.species
        self.objectives = role.objectives
        self.tags = role.tags
        for a in oldroles.actions:
            self.actions[a] = None
        if hasattr(self.role,"faction"):
            self.role.faction.addmember(self)
        if hasattr(oldrole,"faction"):
            oldrole.faction.addmember(self)
    
    async def attacked(self, attack):
        for save in self.saves:
            if save.strength >= attack.strength:
                self.saves.remove(save)
                attack.saved = True
                await save.use(self)
                return "saved"
        await attack.use(attack.user,self)
        self.isAlive = False
        return ["killed",attack.user.role.name]

    async def suicide(self):
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
    species = "Adept"
    categories = ["Investigative"]
    objectives = ["good-standard"]
    saves = []
    tags = {"Good", "Investigative", "Adept"}

    def __init__(self):
        super().__init__()
        self.actions = {"Investigate" : [-1,"night",Seer.investigate], "Publish" : [1,"night",Seer.publish]}
        self.invest_results = []

    async def investigate(self, user, target):
        if hasattr(user.role,"invest_results"):
            if target.alignment == "Evil" and target not in user.role.invest_results and user.role.name == "Seer":
                user.role.invest_results[target] = [target.role.name, target.alignment]
                user.saves.append(Save(1,2))
                return [target.role.name, target.alignment]
        if hasattr(user.role,"invest_targets"):
            user.role.invest_results[target] = [target.role.name, target.alignment]
        return [target.role.name, target.alignment]

    async def publish(self, user, target):
        if not hasattr(user.role,"invest_results"):
            return "fail"
        if target not in user.role.invest_results:
            return "fail"
        return user.role.invest_results[target]

class Jailor(Role):
    name = "Jailor"
    alignment = "Good"
    species = "Human"
    categories = ["Counteractive","Protective"]
    objectives = ["good-standard"]
    saves = []
    tags = {"Good", "Counteractive", "Protective", "Human", "Unique"}

    def __init__(self):
        super().__init__()
        self.actions = {"Jail" : [-1,"night",Jailor.jail]}

    async def jail(self, user, target):
        global Actions, Attacks
        for a in [a for a in Actions if a.user == target]:
            a.fail = True
        for a in [a for a in Attacks if a.target == target]:
            if a.strength < 2:
                a.saved = True
            else:
                a.target = user

class Hunter(Role):
    name = "Hunter"
    alignment = "Good"
    species = "Human"
    categories = ["Killing","Protective"]
    objectives = ["good-standard"]
    saves = [Save(1,2)]
    tags = {"Good", "Killing", "Protective", "Human"}

    def __init__(self):
        super().__init__()
        self.actions = {"Shoot" : [-1,"attack",Hunter.shoot], "Martyr" : [1,"night",Hunter.martyr]}

    async def shoot(self, user, target):
        if target.species in ["Non-Human", "Wolf"]:
            target.attacked(Attack(user,2))
        else:
            target.attacked(Attack(user,0))
        return None

    async def martyr(self, user):
        global Attacks
        for a in Attacks:
            a.target = user

class Wolves(Faction):
    name = "Wolves"

    class role():
        name = "Wolves"
        alignment = "Evil"
        species = "Wolf"
        categories = ["Killing"]

    def __init__(self, chan):
        self.privchannel = chan
        self.actions = {"Maul" : [-1,"night",Wolves.maul], "Pack Offensive" : [0,"night",Wolves.packoffensive]}
        self.members = []

    async def addmember(self, player):
        if player not in self.members:
            self.members.append(player)

    async def removemember(self, player):
        if player in self.members:
            self.members.remove(player)

    async def maul(self, user, target):
        target.attacked(Attack(user,1))
        return None

    async def packoffensive(self, *targets):
        if len(self.members) != len(targets):
            return "tryagain"
        random.shuffle(targets)
        for i in range(0,len(self.members)):
            wolf = self.members[i]
            wolf.role.packoffensive(wolf,targets[i])
        return None

    async def n3_gain_use(self):
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
        super().__init__()
        self.actions = dict(wolves.actions)
        self.actions["Infect"] = [-1,"night",Direwolf.infect]
        self.faction = wolves
        self.ondaystart_abilities = [self.refresh_actions]
        self.onnightstart_abilities = [self.po_gain_use]

    async def packoffensive(self, user, target):
        target.attacked(Attack(user,0))

    async def infect(self, user, target):
        if target in self.faction.members:
            return "Fail"
        target.saves.append(Save(3,1,["infect",self.faction]))
        return None

    async def po_gain_use(self, user):
        if DayCount == 3 and Day == False:
            self.faction.n3_gain_use()

    async def refresh_actions(self, user):
        user.actions["Maul"] = self.faction.actions["Maul"]
        user.actions["Pack Offensive"] = self.faction.actions["Pack Offensive"]

class Werewolf(Role):
    name = "Werewolf"
    alignment = "Evil"
    species = "Wolf"
    categories = ["Killing"]
    objectives = ["evil-standard"]
    saves = []
    tags = {"Evil", "Killing", "Wolf"}

    def __init__(self, wolves):
        super().__init__()
        self.actions = dict(wolves.actions)
        self.faction = wolves
        self.ondaystart_abilities = [self.refresh_actions]
        self.onnightstart_abilities = [self.po_gain_use]

    async def packoffensive(self, user, target):
        target.attacked(Attack(user,0))

    async def po_gain_use(self, user):
        if DayCount == 3 and Day == False:
            self.faction.n3_gain_use()

    async def refresh_actions(self, user):
        user.actions["Maul"] = self.faction.actions["Maul"]
        user.actions["Pack Offensive"] = self.faction.actions["Pack Offensive"]
