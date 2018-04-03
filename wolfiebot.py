import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import math
import os
from roles import *

try:
    from config import TOKEN
except ModuleNotFoundError:
    TOKEN = os.environ['TOKEN']

Client = discord.Client()
prefix= "w."
client = commands.Bot(command_prefix=prefix)

startup_extensions = ["roledescriptions","gamecommands"]

game_channel = client.get_channel(392995027909083137)
voting_channel = client.get_channel(393470084217176075)
notes_channel = client.get_channel(393476547954212874)
dead_channel = client.get_channel(392995124423950344)

AllRoles = ["Alchemist", "Arsonist", "Backstabber", "Bard", "Bloodhound", "Clockmaker", "Cultist", "Cyberhound", "Dentist", "Direwolf", "Doctor", "Dodomeki", "Drunk", "Fate", "Geneticist",
            "Gladiator", "Glazier", "Hacker", "Hangman", "Heir", "Herald", "Hermit", "Hitman", "Hooligan", "Hunter", "Inevitable", "Inventor", "Jailor", "Jester", "Knight", "Kresnik", "Mage", "Maid", "Medium",
            "Merchant", "Multiple Agent", "Noir", "Page", "Paladin", "Philanthropist", "Pixie", "Politician", "Poltergeist", "Poser", "Priest", "Prince", "Psychic", "Researcher", "Rogue",
            "Rōjinbi", "Romantic", "Santa", "Scarecrow", "Seer", "Sentinel", "Sharpshooter", "Shifter", "Shinigami", "Slasher", "Souleater", "Spider", "Spinster", "Spy", "Survivalist", "Sylph", "Evil TARDIS Engineer",
            "Good TARDIS Engineer", "Thief", "Time Lord", "Understudy", "Vampire", "Warlock", "Werewolf", "Whisperer", "Witch"]

GoodRoles = ["Doctor", "Gladiator", "Glazier", "Hacker", "Hunter", "Jailor", "Knight", "Kresnik", "Mage", "Medium", "Noir", "Paladin", "Pixie", "Poser", "Priest", "Prince", "Researcher",
             "Rogue", "Seer", "Sharpshooter", "Spy", "Sylph", "Good TARDIS Engineer", "Time Lord", "Whisperer"]
EvilRoles = ["Backstabber", "Bloodhound", "Cultist", "Cyberhound", "Dentist", "Direwolf", "Dodomeki", "Heir", "Hooligan", "Jester", "Politician", "Poltergeist", "Psychic", "Shinigami", "Spider",
             "Evil TARDIS Engineer", "Vampire", "Warlock", "Werewolf"]
NeutralRoles = ["Alchemist", "Arsonist", "Bard", "Clockmaker", "Drunk", "Fate", "Geneticist", "Hangman", "Herald", "Hermit", "Hitman", "Inevitable", "Inventor", "Maid", "Merchant", "Multiple Agent", "Page",
                "Philanthropist", "Rōjinbi","Romantic", "Santa", "Scarecrow", "Sentinel", "Shifter", "Slasher", "Souleater", "Spinster", "Survivalist", "Thief", "Understudy", "Witch"]

ChaosRoles = ["Alchemist", "Bard", "Drunk", "Fate", "Geneticist", "Hangman", "Herald", "Inevitable", "Inventor", "Jester", "Mage", "Merchant", "Multiple Agent", "Poltergeist", "Psychic", "Rōjinbi",
              "Scarecrow", "Shifter", "Slasher", "Souleater", "Spinster", "Thief", "Understudy", "Warlock"]
CounteractiveRoles = ["Cultist", "Cyberhound", "Backstabber", "Dentist", "Glazier", "Gladiator", "Hangman", "Heir", "Hermit", "Jailor", "Paladin", "Philanthropist", "Pixie", "Priest",
                      "Rogue", "Shinigami", "Spider", "Survivalist", "Thief"]
InvestigativeRoles = ["Dodomeki", "Hacker", "Hermit", "Kresnik", "Mage", "Noir", "Pixie", "Poltergeist", "Researcher", "Seer", "Sharpshooter", "Spinster", "Spy", "Time Lord", "Whisperer"]
KillingRoles = ["Arsonist", "Backstabber", "Bard", "Bloodhound", "Clockmaker", "Cyberhound", "Direwolf", "Doctor", "Gladiator", "Herald", "Hitman", "Hooligan", "Hunter", "Inevitable", "Inventor",
                "Jester", "Knight", "Kresnik", "Noir", "Politician", "Sharpshooter", "Shinigami", "Slasher", "Souleater", "Warlock", "Werewolf", "Witch"]
ProtectiveRoles = ["Doctor", "Hunter", "Jailor", "Multiple Agent", "Paladin", "Rogue", "Romantic", "Sentinel", "Witch"]
SupportRoles = ["Bloodhound", "Cultist", "Direwolf", "Geneticist", "Hacker", "Hooligan", "Knight", "Maid", "Medium", "Merchant", "Page", "Philanthropist", "Politician", "Poser", "Priest",
                "Prince", "Psychic", "Santa", "Scarecrow", "Spider", "Sylph", "Evil TARDIS Engineer", "Good TARDIS Engineer", "Time Lord", "Understudy", "Vampire", "Whisperer"]

HumanRoles = ["Alchemist", "Arsonist", "Backstabber", "Bard", "Clockmaker", "Cultist", "Dentist", "Doctor", "Drunk", "Geneticist", "Gladiator", "Glazier", "Hacker", "Hangman", "Heir", "Hermit",
              "Hitman", "Hooligan", "Hunter", "Inventor", "Jailor", "Knight", "Kresnik", "Mage", "Maid", "Medium", "Merchant", "Multiple Agent", "Noir", "Page", "Paladin", "Philanthropist", "Politician", "Poser",
              "Priest", "Prince", "Psychic", "Researcher", "Rogue", "Romantic", "Seer", "Sharpshooter", "Spy", "Survivalist", "Evil TARDIS Engineer", "Good TARDIS Engineer", "Thief", "Understudy", "Warlock", "Whisperer"]
NonHumanRoles = ["Dodomeki", "Fate", "Herald", "Inevitable", "Jester", "Pixie", "Poltergeist", "Rōjinbi", "Santa", "Scarecrow", "Sentinel", "Shifter", "Shinigami", "Slasher", "Souleater", "Spider",
                 "Spinster", "Sylph", "Time Lord", "Vampire", "Witch"]
WolfRoles = ["Bloodhound", "Cyberhound", "Direwolf", "Werewolf"]

UniqueRoles = ["Alchemist", "Arsonist", "Backstabber", "Bard", "Bloodhound", "Cultist", "Cyberhound", "Dentist", "Direwolf", "Dodomeki", "Drunk", "Fate", "Geneticist", "Gladiator",
               "Hangman", "Heir", "Hermit", "Inevitable", "Inventor", "Jailor", "Knight", "Kresnik", "Maid", "Merchant", "Noir", "Page", "Paladin", "Philanthropist", "Politician", "Priest", "Prince",
               "Psychic", "Researcher", "Rogue", "Rōjinbi", "Romantic", "Santa", "Scarecrow", "Sharpshooter", "Shinigami", "Slasher", "Spider", "Spinster", "Sylph", "Evil TARDIS Engineer",
               "Good TARDIS Engineer", "Thief", "Understudy", "Vampire", "Warlock", "Whisperer"]

AchievableRoles = ["Bloodhound", "Cyberhound", "Dodomeki", "Hacker", "Herald", "Inevitable", "Paladin", "Souleater", "Spinster", "Evil TARDIS Engineer", "Good TARDIS Engineer", "Warlock"]

Modifiers = ["Companion", "Conduit", "Feral", "Guide", "Minstrel", "Morty", "Soulless", "Spectre", "Speedster", "Stand User", "Twin"]
AchievableModifiers = ["Companion", "Guide", "Minstrel", "Soulless", "Spectre"]

VoteEmojis = [":regional_indicator_a:", ":regional_indicator_b:", ":regional_indicator_c:", ":regional_indicator_d:", ":regional_indicator_e:", ":regional_indicator_f:",
              ":regional_indicator_g:", ":regional_indicator_h:", ":regional_indicator_i:", ":regional_indicator_j:", ":regional_indicator_k:", ":regional_indicator_l:",
              ":regional_indicator_m:", ":regional_indicator_n:", ":regional_indicator_o:", ":regional_indicator_p:", ":regional_indicator_q:", ":regional_indicator_r:",
              ":regional_indicator_s:", ":regional_indicator_t:", ":regional_indicator_u:", ":regional_indicator_v:", ":regional_indicator_w:", ":regional_indicator_x:",
              ":regional_indicator_y:", ":regional_indicator_z:"]

UVoteEmojis = [b'\xf0\x9f\x87\xa6', b'\xf0\x9f\x87\xa7', b'\xf0\x9f\x87\xa8', b'\xf0\x9f\x87\xa9', b'\xf0\x9f\x87\xaa', b'\xf0\x9f\x87\xab', b'\xf0\x9f\x87\xac', b'\xf0\x9f\x87\xad',
               b'\xf0\x9f\x87\xae', b'\xf0\x9f\x87\xaf', b'\xf0\x9f\x87\xb0', b'\xf0\x9f\x87\xb1', b'\xf0\x9f\x87\xb2', b'\xf0\x9f\x87\xb3', b'\xf0\x9f\x87\xb4', b'\xf0\x9f\x87\xb5',
               b'\xf0\x9f\x87\xb6', b'\xf0\x9f\x87\xb7', b'\xf0\x9f\x87\xb8', b'\xf0\x9f\x87\xb9', b'\xf0\x9f\x87\xba', b'\xf0\x9f\x87\xbb', b'\xf0\x9f\x87\xbc', b'\xf0\x9f\x87\xbd',
               b'\xf0\x9f\x87\xbe', b'\xf0\x9f\x87\xbf']

PLACEHOLDERICON = "https://via.placeholder.com/256x256"

icons = {"alchemist" : "https://i.imgur.com/CkcPTXj.png", "arsonist" : "https://i.imgur.com/eACFT2J.png", "backstabber" : "https://i.imgur.com/IKAq9Xj.png", "bard" : "https://i.imgur.com/4vqgI1l.png",
         "bloodhound" : "https://i.imgur.com/Ln1TEDm.png", "clockmaker" : "https://i.imgur.com/9sRU1wY.png",
         "companion" : "https://i.imgur.com/jdN1QwN.png", "conduit" : "https://i.imgur.com/Qapubfn.png", "cultist" : "https://i.imgur.com/f6b61vM.png", "cyberhound" : "https://i.imgur.com/EzCRujB.png",
         "dentist" : "https://i.imgur.com/HBu6XXy.png",
         "direwolf" : "https://i.imgur.com/1ZLzSrI.png", "doctor" : "https://i.imgur.com/d7nawSg.png", "dodomeki" : "https://i.imgur.com/niarSn0.png", "drunk" : "https://i.imgur.com/fx1zfEP.png",
         "fate" : "https://i.imgur.com/zWwrrc6.png", "feral" : "https://i.imgur.com/vmOUm8A.png", "geneticist" : "https://i.imgur.com/VcOvFfU.png", "gladiator" : "https://i.imgur.com/qSxDXwc.png",
         "glazier" : "https://i.imgur.com/n7N7dOI.png",
         "guide" : "https://i.imgur.com/6C59lhY.png", "hacker" : "https://i.imgur.com/IT4TDsx.png", "hangman" : "https://i.imgur.com/nIlRgYj.png", "heir" : "https://i.imgur.com/xSQdjo7.png",
         "herald" : "https://i.imgur.com/42kAlx1.png",
         "hermit" : "https://i.imgur.com/WaMFV6G.png", "hitman" : PLACEHOLDERICON, "hooligan" : "https://i.imgur.com/RgofblX.png", "hunter" : "https://i.imgur.com/91EYf4h.png",
         "inevitable" : "https://i.imgur.com/PlzPjU7.png",
         "inventor" : "https://i.imgur.com/uyVCtUE.png", "jailor" : "https://i.imgur.com/w1lT9VF.png", "jester" : "https://i.imgur.com/fHcSdG1.png", "knight" : "https://i.imgur.com/80i6sbg.png",
         "kresnik" : "https://i.imgur.com/l5qO6ik.png",
         "mage" : "https://i.imgur.com/Shp4BCk.png", "maid" : "https://i.imgur.com/j3ls0Bq.png", "medium" : "https://i.imgur.com/LyVnqOB.png", "merchant" : "https://i.imgur.com/94e1SoH.png",
         "minstrel" : "https://i.imgur.com/wiUUTKk.png", "morty" : "https://i.imgur.com/KDys0gU.png", "multipleagent" : "https://i.imgur.com/GBbzP40.png", "noir" : "https://i.imgur.com/jK5qG4G.png",
         "page" : "https://i.imgur.com/zbRiee0.png", "paladin" : "https://i.imgur.com/d21IPWL.png", "philanthropist" : "https://i.imgur.com/UMSqiC4.png", "pixie" : "https://i.imgur.com/wK4dnew.png",
         "politician" : "https://i.imgur.com/c96wBhg.png", "poltergeist" : "https://i.imgur.com/Kw00X8Y.png", "poser" : "https://i.imgur.com/hAH4Bpq.png", "priest" : "https://i.imgur.com/hBt3nbH.png",
         "prince" : "https://i.imgur.com/WlHqAWN.png", "psychic" : "https://i.imgur.com/ij227Zp.png", "researcher" : "https://i.imgur.com/EKYuHHB.png", "rogue" : "https://i.imgur.com/Mv4kPmv.png",
         "rojinbi" : "https://i.imgur.com/l5FG3fd.png",
         "romantic" : "https://i.imgur.com/uyGYo8v.png", "santa" : "https://i.imgur.com/4BbwtSM.png", "scarecrow" : "https://i.imgur.com/AussjT7.png", "seer" : "https://i.imgur.com/ZBw7bqy.png",
         "sentinel" : PLACEHOLDERICON, "sharpshooter" : "https://i.imgur.com/Hi8LZXq.png",
         "shifter" : "https://i.imgur.com/srEm6NB.png", "shinigami" : "https://i.imgur.com/g3lHNHK.png", "slasher" : "https://i.imgur.com/V2Z0g2x.png", "souleater" : "https://i.imgur.com/9Yx69aM.png",
         "soulless" : PLACEHOLDERICON, "spectre" : "https://i.imgur.com/CLtiWTl.png", "speedster" : "https://i.imgur.com/2NdRPVX.png",
         "spider" : "https://i.imgur.com/V5Ovqe9.png", "spinster" : "https://i.imgur.com/VKdzrRc.png", "spy" : "https://i.imgur.com/HBr0JPO.png", "standuser" : "https://i.imgur.com/ANrLfnT.png",
         "survivalist" : "https://i.imgur.com/Ua7WMU8.png", "sylph" : "https://i.imgur.com/AaFsJ7j.png",
         "tardisengineer" : "https://i.imgur.com/EdItCwm.png", "thief" : "https://i.imgur.com/CnqKHwS.png", "timelord" : "https://i.imgur.com/msxarpT.png", "twin" : "https://i.imgur.com/jKI4GnP.png",
         "understudy" : "https://i.imgur.com/xtL1C6F.png", "vampire" : "https://i.imgur.com/QvxToyj.png", "warlock" : "https://i.imgur.com/1pWGWgF.png", "werewolf" : "https://i.imgur.com/SeJ1Fv1.png",
         "whisperer" : "https://i.imgur.com/l8c7un3.png", "witch" : "https://i.imgur.com/uzkYewk.png"}

descCommands = {"Alchemist" : "roles_alchemist", "Arsonist" : "roles_arsonist", "Backstabber" : "roles_backstabber", "Bard" : "roles_bard", "Bloodhound" : "roles_bloodhound",
                "Clockmaker" : "roles_clockmaker", "Cultist" : "roles_cultist", "Cyberhound" : "roles_cyberhound", "Dentist" : "roles_dentist", "Direwolf" : "roles_direwolf",
                "Doctor" : "roles_doctor", "Dodomeki" : "roles_dodomeki", "Drunk" : "roles_drunk", "Fate" : "roles_fate", "Geneticist" : "roles_geneticist", "Gladiator" : "roles_gladiator",
                "Glazier" : "roles_glazier", "Hacker" : "roles_hacker", "Hangman" : "roles_hangman", "Heir" : "roles_heir", "Herald" : "roles_herald", "Hermit" : "roles_hermit",
                "Hitman" : "roles_hitman",
                "Hooligan" : "roles_hooligan", "Hunter" : "roles_hunter", "Inevitable" : "roles_inevitable", "Inventor" : "roles_inventor", "Jailor" : "roles_jailor",
                "Jester" : "roles_jester", "Knight" : "roles_knight", "Kresnik" : "roles_kresnik", "Mage" : "roles_mage", "Maid" : "roles_maid", "Medium" : "roles_medium", "Merchant" : "roles_merchant",
                "Multiple Agent" : "roles_multipleagent", "Noir" : "roles_noir", "Page" : "roles_page", "Paladin" : "roles_paladin", "Philanthropist" : "roles_philanthropist",
                "Pixie" : "roles_pixie", "Politician" : "roles_politician", "Poltergeist" : "roles_poltergeist", "Poser" : "roles_poser", "Priest" : "roles_priest",
                "Prince" : "roles_prince", "Psychic" : "roles_psychic", "Researcher" : "roles_researcher", "Rogue" : "roles_rogue", "Rōjinbi" : "roles_rojinbi",
                "Romantic" : "roles_romantic", "Santa" : "roles_santa", "Scarecrow" : "roles_scarecrow", "Seer" : "roles_seer", "Sentinel" : "roles_sentinel",
                "Sharpshooter" : "roles_sharpshooter", "Shifter" : "roles_shifter",
                "Shinigami" : "roles_shinigami", "Slasher" : "roles_slasher", "Souleater" : "roles_souleater", "Soulless" : "roles_soulless", "Spider" : "roles_spider",
                "Spinster" : "roles_spinster", "Spy" : "roles_spy",
                "Sylph" : "roles_sylph", "TARDIS Engineer" : "roles_tardisengineer", "Thief" : "roles_thief", "Time Lord" : "roles_timelord", "Understudy" : "roles_understudy", "Vampire" : "roles_vampire",
                "Warlock" : "roles_warlock", "Werewolf" : "roles_werewolf", "Whisperer" : "roles_whisperer", "Witch" : "roles_witch", "Companion" : "roles_companion",
                "Conduit" : "roles_conduit", "Feral" : "roles_feral", "Guide" : "roles_guide", "Minstrel" : "roles_minstrel", "Morty" : "roles_morty", "Spectre" : "roles_spectre",
                "Speedster" : "roles_speedster", "Stand User" : "roles_standuser", "Twin" : "roles_twin"}

global Day, PlayerInfo, Actions, Attacks
Day = False
DayCount = 0
PlayerInfo = []
Actions = []
Attacks = []

@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    await client.change_presence(activity=discord.Game(name="Say w.help"))
    chan = client.get_channel(392995207894925313)
    await chan.send("WolfieBot online!")

client.remove_command("help")

@client.command(pass_context=True)
async def help(ctx):
    await ctx.send("""Hi there! My name is **Wolfie**! I'm the (WIP) bot for the **Werewolf Server**. This is what I can do:
```md
<w.help> - Shows this message.
<w.gm_help> - Shows commands available for GMs only.
<w.gamerules> - Provides a link to the rules for playing the game.

<w.register (name)> - Creates a private channel for command user using name provided.
<w.rolelist> - Provides a list of roles in the game, plus commands to see more information.
<w.listroles (space seperated list of tags as parameters)> - Lists all roles that have all the tags provided.
<w.achieve (role)> - Lists nonstandard ways of gaining given role.
<w.icon (role)> - Displays icon for given role.

<w.generatelist> - Shows commands to generate rolelists.
<w.vote (options to vote between seperated by commas)> - Displays a list of specified options to vote on.
<w.advancedvote (options to vote between seperated by commas; time; needed)> - w.vote, but better.

<w.randomchoice (comma seperated list of options)> - Randomly chooses from given options.
<w.randomrole (space seperated list of tags as parameters)> - Randomly gives a role that has all the tags provided.
<w.flip (number of coins to flip)> - Flips a specified amount of coins.
<w.roll (#d#)> - Rolls specified dice.
<w.magic8ball> - Ask Wolfie a question!

<w.score (wins:loses)> - Displays score for given statistics.```""")

@client.command(pass_context=True)
async def gm_help(ctx):
    await ctx.send("""```md
<w.setplayers (mentions)> - Sets all users mentioned as Player. If any mentioned are already Player, removes role.
<w.giveroles (player: role [(modifier)], etc)> - Gives players listed the applied role.
<w.gamestatus> - Returns all players in the current game with information about them. 

<w.daytimer (n; seconds; announcements)> - Sets a timer for the day, unlocks #game at start, locks #game when it ends. Seperate lines in announcements with /.
<w.playervote ([time])> - Creates a vote in #voting for the players. Time is 900 seconds if not given.
<w.night> - Ends day.

<w.mayor (@player)> - Sets given player as Mayor.
<w.deputy (@player)> - Sets given player as Deputy.
<w.kill (@player)> - Kills the given player.
<w.revive (@player)> - Revives the given player.

<w.wolves (mentions)> - Creates #wolves if it does not exist, and gives mentioned players permissions for it.
<w.twin (@twin1 @twin2)> - Creates #twins channel for specified players.
<w.tardis (@timelord @companion)> - Creates/fetches #tardis channel for timelord, if companion is not companion gives them permissions, otherwise removes permissions.
<w.coven (mentions)> - Creates #coven if it does not exist, and gives mentioned players permissions for it.
<w.seance (@medium @target)> - Creates a seance between medium and target; this is removed at the start of a day.

<w.lockjaw (@player boolean)> - If boolean true, lockjaws player; if false, unlockjaws player.
<w.medium (@player boolean)> - If boolean true, gives player perms to see #dead; if false, removes perms.
<w.sonic (comma-seperated list of all roles in game)> - Returns a Sonic result for roles provided.

<w.endgame> - Ends game, removing all game roles and permissions from all members of guild and deleting all group priv channels.```""")

@client.command(pass_context=True)
async def gamerules(ctx):
    embed=discord.Embed(description="""This link details the rules for playing Werewolf.
If you have any questions or suggestions for improvement on the rules, contact Army with them. They'll be happy to help!
(If that doesn't work, here's the link: https://bit.ly/werewolf-gamerules)""")
    embed.set_author(name="Werewolf Party Game Rules", url='https://bit.ly/werewolf-gamerules', icon_url='https://i.imgur.com/soFqp3g.png')
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def rolelist(ctx):
    await ctx.send("""__**Roles**__
```md
[+][Alchemist] - Neutral, Chaos/Support, Human, Unique - <w.roles_alchemist>
[+][Arsonist] - Neutral, Killing, Human, Unique - <w.roles_arsonist>
[+][Backstabber] - Evil, Counteractive/Killing, Human, Unique - <w.roles_backstabber>
[+][Bard] - Neutral, Chaos/Killing, Human, Unique - <w.roles_bard>
[+][Bloodhound] - Evil, Killing/Support, Wolf, Unique, Achievable - <w.roles_bloodhound>
[+][Clockmaker] - Neutral, Killing, Human - <w.roles_clockmaker>
[+][Companion] - Modifier, Achievable - <w.roles_companion>
[+][Conduit] - Modifier - <w.roles_conduit>
[+][Cultist] - Evil, Counteractive/Support, Human, Unique - <w.roles_cultist>
[+][Cyberhound] - Evil, Counteractive/Killing, Wolf, Unique, Achievable - <w.roles_cyberhound>
[+][Dentist] - Evil, Counteractive, Human, Unique - <w.roles_dentist>
[+][Direwolf] - Evil, Killing/Support, Wolf, Unique - <w.roles_direwolf>
[+][Doctor] - Good, Killing/Protective, Human - <w.roles_doctor>
[+][Dodomeki] - Evil, Investigative, Non-Human, Unique, Achievable - <w.roles_dodomeki>
[+][Drunk] - Neutral, Chaos, Human, Unique - <w.roles_drunk>
[+][Fate] - Neutral, Chaos, Non-Human, Unique - <w.roles_fate>
[+][Feral] - Modifier - <w.roles_feral>
[+][Geneticist] - Neutral, Chaos/Support, Human, Unique - <w.roles_geneticist>
[+][Gladiator] - Good, Counteractive/Killing, Human, Unique - <w.roles_gladiator>
[+][Glazier] - Good, Counteractive, Human - <w.roles_glazier>
[+][Guide] - Modifier, Achievable - <w.roles_guide>
```""")
    await ctx.send("""```md
[+][Hacker] - Good, Investigative/Support, Human, Unique, Achievable - <w.roles_hacker>
[+][Hangman] - Neutral, Chaos/Counteractive, Human, Unique - <w.roles_hangman>
[+][Heir] - Evil, Counteractive, Human, Unique - <w.roles_heir>
[+][Herald] - Neutral, Chaos/Killing, Non-Human, Unique, Achievable - <w.roles_herald>
[+][Hermit] - Neutral, Investigative/Counteractive, Human, Unique - <w.roles_hermit>
[+][Hitman] - Neutral, Killing, Human - <w.roles_hitman>
[+][Hooligan] - Evil, Killing/Support, Human - <w.roles_hooligan>
[+][Hunter] - Good, Killing/Protective, Human - <w.roles_hunter>
[+][Inevitable] - Neutral, Chaos/Killing, Non-Human, Unique, Achievable - <w.roles_inevitable>
[+][Inventor] - Neutral, Chaos/Killing, Human, Unique - <w.roles_inventor>
[+][Jailor] - Good, Counteractive/Protective, Human, Unique - <w.roles_jailor>
[+][Jester] - Evil, Chaos/Killing, Non-Human - <w.roles_jester>
[+][Knight] - Good, Killing/Support, Human, Unique - <w.roles_knight>
[+][Kresnik] - Good, Investigative/Killing, Human, Unique - <w.roles_kresnik>
[+][Mage] - Good, Chaos/Investigative, Human - <w.roles_mage>
[+][Maid] - Neutral, Support, Human, Unique - <w.roles_maid>
[+][Medium] - Good, Support, Human - <w.roles_medium>
[+][Merchant] - Neutral, Chaos/Support, Human, Unique - <w.roles_merchant>
[+][Minstrel] - Modifier, Achievable - <w.roles_minstrel>
[+][Morty] - Modifier - <w.roles_morty>
[+][Multiple Agent] - Neutral, Chaos/Protective, Human - <w.roles_multipleagent>
[+][Noir] - Good, Investigative/Killing, Human, Unique - <w.roles_noir>
```""")
    await ctx.send("""```md
[+][Page] - Neutral, Support, Human, Unique - <w.roles_page>
[+][Paladin] - Good, Human, Counteractive/Protective, Unique, Achievable - <w.roles_paladin>
[+][Philanthropist] - Neutral, Counteractive/Support, Human, Unique - <w.roles_philanthropist>
[+][Pixie] - Good, Counteractive/Investigative, Non-Human - <w.roles_pixie>
[+][Politician] - Evil, Killing/Support, Human, Unique - <w.roles_politician>
[+][Poltergeist] - Evil, Chaos/Investigative, Non-Human - <w.roles_poltergeist>
[+][Poser] - Good, Support, Human - <w.roles_poser>
[+][Priest] - Good, Counteractive/Support, Human, Unique - <w.roles_priest>
[+][Prince] - Good, Support, Human, Unique - <w.roles_prince>
[+][Psychic] - Evil, Chaos/Support, Human, Unique - <w.roles_psychic>
[+][Researcher] - Good, Investigative, Human, Unique - <w.roles_researcher>
[+][Rogue] - Good, Counteractive/Protective, Human, Unique - <w.roles_rogue>
[+][Rōjinbi] - Neutral, Chaos, Non-Human, Unique - <w.roles_rojinbi>
[+][Romantic] - Neutral, Protective, Human, Unique - <w.roles_romantic>
[+][Santa] - Neutral, Support, Non-Human, Unique - <w.roles_santa>
[+][Scarecrow] - Neutral, Chaos/Support, Non-Human, Unique - <w.roles_scarecrow>
[+][Seer] - Good, Investigative, Human - <w.roles_seer>
[+][Sentinel] - Neutral, Protective, Non-Human - <w.roles_sentinel>
[+][Shifter] - Neutral, Chaos, Non-Human - <w.roles_shifter>
[+][Shinigami] - Evil, Counteractive/Killing, Non-Human, Unique - <w.roles_shinigami>
[+][Slasher] - Neutral, Chaos/Killing, Non-Human, Unique - <w.roles_slasher>
[+][Souleater] - Neutral, Chaos/Killing, Non-Human, Achievable - <w.roles_souleater>
```""")
    await ctx.send("""```md
[+][Soulless] - Modifier, Achievable - <w.roles_soulless>
[+][Spectre] - Modifier, Achievable - <w.roles_spectre>
[+][Speedster] - Modifier - <w.roles_speedster>
[+][Spider] - Evil, Counteractive/Support, Non-Human, Unique - <w.roles_spider>
[+][Spinster] - Neutral, Chaos/Investigative, Non-Human, Unique, Achievable - <w.roles_spinster>
[+][Spy] - Good, Investigative, Human - <w.roles_spy>
[+][Stand User] - Modifier - <w.roles_standuser>
[+][Survivalist] - Neutral, Counteractive, Human - <w.roles_survivalist>
[+][Sylph] - Good, Support, Non-Human, Unique - <w.roles_sylph>
[+][TARDIS Engineer] - Good/Evil, Support, Human, Unique, Achievable - <w.roles_tardisengineer>
[+][Thief] - Neutral, Chaos/Counteractive, Human, Unique - <w.roles_thief>
[+][Time Lord] - Good, Investigative/Support, Non-Human - <w.roles_timelord>
[+][Twin] - Modifier - <w.roles_twin>
[+][Understudy] - Neutral, Chaos/Support, Human, Unique - <w.roles_understudy>
[+][Vampire] - Evil, Support, Non-Human, Unique - <w.roles_vampire>
[+][Warlock] - Evil, Chaos/Killing, Human, Unique, Achievable - <w.roles_warlock>
[+][Werewolf] - Evil, Killing, Wolf - <w.roles_werewolf>
[+][Whisperer] - Good, Investigative/Support, Human, Unique - <w.roles_whisperer>
[+][Witch] - Neutral, Killing/Protective, Non-Human - <w.roles_witch>
```""")

@client.command(pass_context=True)
async def register(ctx, *, name: str):
    try:
        name.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        await ctx.send("Please only use ascii characters.")
        return
    channame = "{}-priv".format(name)
    channame = channame.replace(" ","-")
    channame = channame.lower()
    guild = ctx.message.guild
    user = ctx.message.author
    gm_role = discord.utils.get(guild.roles, name="Game Master")
    bot_role = discord.utils.get(guild.roles, name="Bots")
    if gm_role in user.roles:
        await ctx.send("You're a GM! You can't have a priv channel.")
        return
    for c in guild.channels:
        if c.name == channame:
            await ctx.send("Somebody already has that channel name, sorry!")
            return
        if "-priv" in c.name:
            x = [u for u in guild.members if c.permissions_for(u).read_messages == True]
            if user in x:
                await ctx.send("You already have a priv channel!")
                return
    perms = discord.PermissionOverwrite(read_messages=True)
    everyone_perms = discord.PermissionOverwrite(read_messages=False)
    overwrites = {guild.default_role : everyone_perms, user : perms, gm_role : perms}
    category = discord.utils.get(guild.categories, name="priv channels")
    priv_channel = await guild.create_text_channel(channame, overwrites=overwrites, category=category)
    if channame in [c.name for c in guild.channels]:
        await ctx.send("Channel {} created successfully.".format(priv_channel.mention))
    else:
        await ctx.send("There was an error creating the channel.")

@client.command(pass_context=True)
async def randomchoice(ctx, *, message=""):
    if message == "":
        await ctx.send("""Usage of command <w.randomchoice>:
```md
<w.randomchoice (comma seperated list of options)>

Example: <w.randomchoice A, B, C>
Output: 'C'```""")
    else:
        options = message.split(", ")
        result = random.choice(options)
        await ctx.send("**{}**".format(result))
        return result

@client.command(pass_context=True)
async def randomrole(ctx, *, message=""):
    if message == "":
        await ctx.send("""Usage of command <w.randomrole>:
```md
<w.randomrole (space seperated list of tags as parameters)>

Tags:
> Good
> Evil
> Neutral
> Human
> Non-Human
> Wolf
> Chaos
> Counteractive
> Investigative
> Killing
> Protective
> Support
> Unique
> Achievable

Include 'all' in parameters to discard parameters and allow all roles.
Include 'modifier' in parameters to include and limit selection to modifiers.
Precede tags with 'x-' to exclude roles with them.

Example: <w.randomrole good>
Output: 'Jailor'```""")
    else:
        conditions = message.split(" ")
        for c in conditions:
            c = c.lower()
        if "modifier" in conditions:
            All = list(Modifiers)
            Valid = list(All)
            for r in All:
                if "achievable" in conditions:
                    if r not in AchievableModifiers:
                        Valid.remove(r)
                    continue
                if "x-achievable" in conditions:
                    if r in AchievableModifiers:
                        Valid.remove(r)
                    continue
        else:
            All = list(AllRoles)
            Valid = list(All)
            ref = {"good" : GoodRoles, "evil" : EvilRoles, "neutral" : NeutralRoles, "chaos" : ChaosRoles, "counteractive" : CounteractiveRoles, "investigative" : InvestigativeRoles,
                   "killing" : KillingRoles, "protective" : ProtectiveRoles, "support" : SupportRoles, "human" : HumanRoles, "nonhuman" : NonHumanRoles, "non-human" : NonHumanRoles,
                   "wolf" : WolfRoles, "unique" : UniqueRoles, "achievable" : AchievableRoles}
            xref = {"x-good" : GoodRoles, "x-evil" : EvilRoles, "x-neutral" : NeutralRoles, "x-chaos" : ChaosRoles, "x-counteractive" : CounteractiveRoles,
                    "x-investigative" : InvestigativeRoles, "x-killing" : KillingRoles, "x-protective" : ProtectiveRoles, "x-support" : SupportRoles, "x-human" : HumanRoles,
                    "x-nonhuman" : NonHumanRoles, "x-non-human" : NonHumanRoles, "x-wolf" : WolfRoles, "x-unique" : UniqueRoles, "x-achievable" : AchievableRoles}
            if message.lower() != "all":
                for r in All:
                    for c in conditions:
                        if c in ref:
                            if r not in ref[c]:
                                Valid.remove(r)
                                break
                        elif c in xref:
                            if r in xref[c]:
                                Valid.remove(r)
                                break
        if Valid == []:
            await ctx.send("No roles exist that fit all parameters, sorry. :(")
        else:
            while True:
                role = random.choice(Valid)
                if role == "Good TARDIS Engineer" or role == "Evil TARDIS Engineer":
                    if "Good TARDIS Engineer" in Valid and "Evil TARDIS Engineer" in Valid:
                        x = random.randint(0,1)
                        if x == 0:
                            continue
                break
            await ctx.send("**{}**".format(role))
            return role

@client.command(pass_context=True)
async def listroles(ctx, *, message=""):
    if message == "":
        await ctx.send("""Usage of command <w.listroles>:
```md
<w.listroles (space seperated list of tags as parameters)>

Tags:
> Good
> Evil
> Neutral
> Human
> Non-Human
> Wolf
> Chaos
> Counteractive
> Investigative
> Killing
> Protective
> Support
> Unique
> Achievable

Include 'all' in parameters to discard parameters and allow all roles.
Include 'modifier' in parameters to include and limit selection to modifiers.
Precede tags with 'x-' to exclude roles with them.

Example: <w.listroles wolf>
Output: '3 roles found:
 - Cyberhound
 - Direwolf
 - Werewolf'```""")
    else:
        conditions = message.split(" ")
        for c in conditions:
            c = c.lower()
        if "modifier" in conditions:
            All = list(Modifiers)
            Valid = list(All)
            for r in All:
                if "achievable" in conditions:
                    if r not in AchievableModifiers:
                        Valid.remove(r)
                    continue
                if "x-achievable" in conditions:
                    if r in AchievableModifiers:
                        Valid.remove(r)
                    continue
        else:
            All = list(AllRoles)
            Valid = list(All)
            ref = {"good" : GoodRoles, "evil" : EvilRoles, "neutral" : NeutralRoles, "chaos" : ChaosRoles, "counteractive" : CounteractiveRoles, "investigative" : InvestigativeRoles,
                   "killing" : KillingRoles, "protective" : ProtectiveRoles, "support" : SupportRoles, "human" : HumanRoles, "nonhuman" : NonHumanRoles, "non-human" : NonHumanRoles,
                   "wolf" : WolfRoles, "unique" : UniqueRoles, "achievable" : AchievableRoles}
            xref = {"x-good" : GoodRoles, "x-evil" : EvilRoles, "x-neutral" : NeutralRoles, "x-chaos" : ChaosRoles, "x-counteractive" : CounteractiveRoles,
                    "x-investigative" : InvestigativeRoles, "x-killing" : KillingRoles, "x-protective" : ProtectiveRoles, "x-support" : SupportRoles, "x-human" : HumanRoles,
                    "x-nonhuman" : NonHumanRoles, "x-non-human" : NonHumanRoles, "x-wolf" : WolfRoles, "x-unique" : UniqueRoles, "x-achievable" : AchievableRoles}
            if message.lower() != "all":
                for r in All:
                    for c in conditions:
                        if c in ref:
                            if r not in ref[c]:
                                Valid.remove(r)
                                break
                        elif c in xref:
                            if r in xref[c]:
                                Valid.remove(r)
                                break
        if Valid == []:
            await ctx.send("No roles exist that fit all parameters, sorry. :(")
        else:
            display = "{} roles found:\n```".format(len(Valid))
            for r in Valid:
                display = "{} - {}\n".format(display, r)
            display = "{}```".format(display)
            await ctx.send(display)

@client.command(pass_context=True)
async def roles(ctx, *, role: str):
    role = role.title()
    te = False
    if role == "Tardis Engineer":
        role = "TARDIS Engineer"
        te = True
    if role == "Rojinbi":
        role = "Rōjinbi"
    if role in AllRoles or role in Modifiers or te:
        await ctx.invoke(client.get_command(descCommands[role]))

@client.command(pass_context=True)
async def achieve(ctx, *, role=""):
    if role == "":
        await ctx.send("""Usage of command <w.achieve>:
```md
<w.achieve (role)>

Example: <w.score hacker>
Output: 'Hacker:
- Be targeted with Investigate as an Inventor.
- Target a player with Do Research and have every living player other than yourself and the target player appear in the results.
- (Random) Be a Drunk.'```""")
    else:
        role = role.title()
        te = False
        if role == "Tardis Engineer":
            role = "TARDIS Engineer"
            te = True
        if role == "Rojinbi":
            role = "Rōjinbi"
        if role in AllRoles or role in Modifiers or te:
            methods = {"Bloodhound" : "- Be targeted with *Fangs* as a Wolf or a player with the Feral modifier.\n- Be targeted with both *Fangs* and *Infect*.\n- (Random) Be a Drunk.",
                       "Cultist" : "- Become Evil as a Priest.\n- Have any Priest become a Cultist as a Priest.",
                       "Cyberhound" : "- Be targeted with *Infect* as an Inventor.\n- Successfully predit *Infect* as a Psychic.\n- (Random) Be a Drunk.",
                       "Dodomeki" : "- Become Evil as a Thief or a Rogue.\n- (Random) Be a Drunk.",
                       "Hacker" : "- Be targeted with *Investigate* as an Inventor.\n- Target a player with *Research* and have every living player other than yourself and the target player appear in the results.\n- (Random) Be a Drunk.",
                       "Herald" : "- Be targeted with *Create Herald*.",
                       "Inevitable" : "- Be targeted with *Create Inevitable* as an Evil player.",
                       "Inventor" : "- Lose the Companion modifer as a TARDIS Engineer.",
                       "Jester" : "- Be targeted with *Laughing Gas* if targeted with *Lockjaw* the previous night.",
                       "Paladin" : "- Live until NIGHT 5 as a Priest.\n- (Random) Be a Drunk.",
                       "Priest" : "- Become Good as a Cultist.\n- Have any Cultist become a Priest as a Cultist.",
                       "Psychic" : "- Target Evil players with *Loyalty* for three nights in a row as a Multiple Agent.",
                       "Shifter" : "- Be targeted with *Shift*.",
                       "Slasher" : "- Have the Slasher die after being targeted with *Legacy*.",
                       "Souleater" : "- Spend three nights as a Shifter. These nights do not need to be consecutive.\n- (Random) Be a Drunk.",
                       "Spy" : "- Target Good players with *Loyalty* for three nights in a row as a Multiple Agent.",
                       "Spinster" : "- Be targeted with *Create Spinster* as a Good player.",
                       "TARDIS Engineer" : "- Be targeted with *Invite* as an Inventor or a Companion.\n- Be targeted with *Invite* by two Time Lords of the same alignment.",
                       "Vampire" : "- Be targeted with *Fangs* while being without any saves.",
                       "Warlock" : "- Have any Priest become a Paladin as a Cultist.\n- (Random) Be a Drunk.",
                       "Companion" : "- Be targeted with *Invite*.",
                       "Conduit" : "- Have your Twin gain the Conduit modifier as a Twin.\n- Have your Companion gain the Conduit modifier as a Time Lord.",
                       "Guide" : "- (Random) Be in a game with a Page as a Unique role.",
                       "Minstrel" : "- (Random) Be in a game with a Bard.",
                       "Spectre" : "- Die as an Arsonist.\n- Die as a Sylph.\n- Be killed by Wolves as a Spider.\n- Be killed by a Soulless player as a Souleater.\n- Die before NIGHT 3 as a Drunk.\n- Die during the same night or the day after being targeted with *Curse*.\n- Redirect a Poltergeist who is redirecting you as a Poltergeist.\n- Have your Twin gain the Spectre modifier as a Twin.\n- Die by any means other than Suicide or Lynching as a Whisperer.",
                       "Stand User" : "- Be targeted with *Stand Arrow*.",
                       "Werewolf" : "- Use a save gained through *Infect*.",
                       "Witch" : "- Be targeted with *Poison* and *Heal* on the same night by different players."}
            try:
                await ctx.send("{}:\n{}".format(role,methods[role]))
            except KeyError:
                await ctx.send("There are no alternate ways of gaining that role or modifier.")
        else:
            await ctx.send("That is not a role or modifier.")

@client.command(pass_context=True)
async def score(ctx, *, message=""):
    if message == "":
        await ctx.send("""Usage of command <w.score>:
```md
<w.score (wins:loses)>

Example: <w.score 10:6>
Output: '870'```""")
    else:
        message = message.split(":")
        W = int(message[0])
        L = int(message[1])
        score = round((100+(W+L)*2)*(W-L)*(1+(W+1)/(W+L+1)))
        await ctx.send(score)

@client.command(pass_context=True)
async def flip(ctx, *, message=""):
    if message == "":
        await ctx.send("""Usage of command <w.flip>:
```md
<w.flip (number of coins to flip)>

Example: <w.flip 3>
Output: 'T, H, H'```""")
    else:
        message = int(message)
        send=""
        tcount=0
        hcount=0
        for c in range(0,message):
            if c != 0:
                send="{}, ".format(send)
            i = random.randint(0,1)
            if i == 0:
                send=send+"T"
                tcount=tcount+1
            else:
                send=send+"H"
                hcount=hcount+1
        embed=discord.Embed(title=send)
        await ctx.send(embed=embed)
        return [hcount,tcount]

@client.command(pass_context=True)
async def roll(ctx, *, message=""):
    if message == "":
        await ctx.send("""Usage of command <w.roll>:
```md
<w.roll (#d#)>

Example: <w.roll 3d20>
Output: '19, 8, 14'```""")
    else:
        message = message.split("d")
        times = int(message[0])
        sides = int(message[1])
        send = ""
        for c in range(0,times):
            if c != 0:
                send="{}, ".format(send)
            i = str(random.randint(1,sides))
            send = send+i
        embed=discord.Embed(title=send)
        await ctx.send(embed=embed)

@client.command(pass_context=True)
async def magic8ball(ctx):
    results = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes, definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yep.",
               "Signs point to yes.", "Reply hazy. Try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
               "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
    await ctx.send(random.choice(results))

@client.command(pass_context=True)
async def vote(ctx, *, message="", where="", needed=0, time=0):
    if message == "":
        await ctx.send("""Usage of command <w.vote>:
```md
<w.vote (options to vote between seperated by commas)>

Example: <w.vote 1, 2, 3>
Output: 'React with appropriate emoji to vote:
:A: --> 1
:B: --> 2
:C: --> 3'```""")
    else:
        if where == "":
                where = ctx.message.channel
        global VoteEmojis
        options = message.split(", ")
        if len(options) > 20:
            await ctx.send("Too many!")
        else:
            options = sorted(options)
            display=""
            for i in range(0,len(options)):
                display = display+("\n{} --> {}".format(VoteEmojis[i],options[i]))
            vote_message = await where.send(embed=discord.Embed(title="React with appropriate emoji to vote:",description=display))
            if needed != 0 and time != 0:
                wintimer = 0
                for i in range(0,time):                
                    vote_message = await where.get_message(vote_message.id)
                    await vote_message.edit(embed=discord.Embed(title="React with appropriate emoji to vote: [{}]".format(time-i),description=display))
                    await asyncio.sleep(1)
                    if i % 5 == 0:
                        votes = {VoteEmojis[i] : [0, options[i]] for i in range(0,len(options))}
                        reacts = vote_message.reactions
                        for r in reacts:
                            for i in range(0,len(options)):
                                if r.emoji.encode('utf-8') == UVoteEmojis[i]:
                                    votes[VoteEmojis[i]][0] = r.count
                        top = []
                        for v in votes:
                            if votes[v][0] == max([votes[i][0] for i in votes]) and votes[v][0] >= needed:
                                top.append(votes[v])
                        if top != []:
                            if wintimer == 6:
                                await vote_message.edit(embed=discord.Embed(title="React with appropriate emoji to vote:",description=display))
                                if len(top) == 1:
                                    await where.send("**{}** has been voted!".format(top[0][1]))
                                    return top[0]
                                else:
                                    for w in top:
                                        if w == top[0]:
                                            l = "**{}**".format(w[1])
                                        elif w != top[len(top)-1]:
                                            l = "{}, **{}**".format(l,w[1])
                                        else:
                                            l = "{} and **{}** have been voted!".format(l,w[1])
                                    await where.send(l)
                                    # solve tie
                                    return
                            else:
                                wintimer = wintimer + 1
                        else:
                            wintimer = 0
                vote_message = await where.get_message(vote_message.id)
                await vote_message.edit(embed=discord.Embed(title="React with appropriate emoji to vote:",description=display))
                votes = {VoteEmojis[i] : [0, options[i]] for i in range(0,len(options))}
                reacts = vote_message.reactions
                for r in reacts:
                    for i in range(0,len(options)):
                        if r.emoji.encode('utf-8') == UVoteEmojis[i]:
                            votes[VoteEmojis[i]][0] = r.count
                top = []
                for v in votes:
                    if votes[v][0] == max([votes[i][0] for i in votes]):
                        top.append(votes[v])
                if len(top) == 1:
                    await where.send("**{}** has been voted!".format(top[0][1]))
                    return top[0]
                else:
                    for w in top:
                        if w == top[0]:
                            l = "**{}**".format(w[1])
                        elif w != top[len(top)-1]:
                            l = "{}, **{}**".format(l,w[1])
                        else:
                            l = "{} and **{}** have been voted!".format(l,w[1])
                    await where.send(l)
                    # solve tie
                    return

@client.command(pass_context=True)
async def advancedvote(ctx, *, message="", where=""):
    if message == "":
        await ctx.send("""Usage of command <w.advancedvote>:
```md
<w.advancedvote (options to vote between seperated by commas; time; needed)>

Example: <w.vote 1, 2, 3; 60; 3>
Output: 'React with appropriate emoji to vote:
:A: --> 1
:B: --> 2
:C: --> 3'
The vote will last 60 seconds (or until any option gets 3 votes) and will then return the result.```""")
    else:
        if where == "":
            where = ctx.message.channel
        message = message.split("; ")
        time = int(message[1])
        needed = int(message[2])
        message = message[0]
        await ctx.invoke(client.get_command("vote"),message=message,time=time,needed=needed)

@client.command(pass_context=True)
async def icon(ctx, *, role=""):
    if role == "":
        await ctx.send("""Usage of command <w.icon>:
```md
<w.icon (role)>

Example: <w.icon seer>
Output: 'https://i.imgur.com/Ih7WkoX.png'```""")
    else:
        role = role.lower()
        role = role.replace(" ","")
        try:
            icon = icons[role]
            await ctx.send(icon)
        except KeyError:
            await ctx.send("That is not a role.")

@client.group(pass_context=True)
async def generatelist(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send("Available Gamemodes to generate lists for: \n(Give Players and Roles as comma seperated lists)\n```md\nStandard - <w.generatelist standard [players]>\n\
Anonymous Register - <w.generatelist anons [players] : [roles]>\nDuality - <w.generatelist duality [players]>\nMoral Feud - <w.generatelist morals [players]>\n\
Truth & Claw - <w.generatelist tac [players]>```")

@generatelist.command(pass_context=True)
async def standard(ctx, *, message: str):
    Evil=list(EvilRoles)
    for r in Evil:
        if r in AchievableRoles:
            Evil.remove(r)
    Evil.remove("Direwolf")
    Evil.remove("Werewolf")
    Good=list(GoodRoles)
    for r in Good:
        if r in AchievableRoles:
            Good.remove(r)
    Good.remove("Priest")
    Neutral=list(NeutralRoles)
    for r in Neutral:
        if r in AchievableRoles:
            Neutral.remove(r)
    Mod=list(Modifiers)
    for r in Mod:
        if r in AchievableModifiers:
            Mod.remove(r)
    PlayerList = message.split(", ")
    PlayerList = sorted(PlayerList)
    if len(PlayerList) < 8:
        await ctx.send("Not enough players, sorry.")
        return
    else:
        GCount = 4
        ECount = 3
        NCount = 1
        PlayerCount = len(PlayerList) - 8
        skip = False
        loopcount = 0
        while True:
            loopcount = loopcount + 1
            for i in range(0,PlayerCount):
                if skip == True:
                    skip = False
                    continue
                x = random.randint(0,2)
                if x != 0 and i < (PlayerCount - 2):
                    GCount = GCount + 1
                    y = random.randint(0,2)
                    if y != 0:
                        ECount = ECount + 1
                        skip = True
                else:
                    NCount = NCount + 1
            if ECount >= round(GCount*2/3) and NCount <= round((GCount+ECount)/2):
                break
            elif loopcount == 75:
                await ctx.send("Error, please try again.")
                return
        while True:
            RoleList = ["Seer", "Direwolf"]
            w = round(len(PlayerList)/8)
            for i in range(0,w):
                RoleList.append("Werewolf")
            CP = False
            Minstrels = 0
            for i in range((1+w),ECount):
                r = random.choice(Evil)
                RoleList.append(r)
                if r in UniqueRoles:
                    Evil.remove(r)
                if r == "Cultist":
                    CP = True
            for i in range(1,GCount):
                if "Vampire" in RoleList:
                    Good.append("Kresnik")
                if CP == True:
                    r = "Priest"
                    CP = False
                else:
                    r = random.choice(Good)
                RoleList.append(r)
                if r in UniqueRoles and r != "Priest":
                    Good.remove(r)
                    if r == "Kresnik" and "Vampire" in RoleList:
                        Good.remove(r)
            for i in range(0,NCount):
                r = random.choice(Neutral)
                RoleList.append(r)
                if r in UniqueRoles:
                    Neutral.remove(r)
                if r == "Bard":
                    Minstrels = 2
                    Mod.append("Minstrel")
                    Mod.append("Minstrel")
            ModifierList = []
            Twins = False
            TwinCount = 1
            StandUsers = False
            SUPresent = False
            for i in range(0,len(PlayerList)):
                if Minstrels > 0:
                    m = "Minstrel"
                    Minstrels = Minstrels - 1
                elif Twins:
                    m = "Twin {}".format(TwinCount)
                    TwinCount = TwinCount+1
                    Twins = False
                elif StandUsers:
                    m = "Stand User"
                    Mod.append("Stand User")
                    StandUsers = False
                else:
                    z = random.randint(1,4)
                    if z == 4:
                        m = random.choice(Mod)
                    else:
                        m = ""
                if m == "Twin":
                    m = "Twin {}".format(TwinCount)
                    Twins = True
                elif m == "Stand User" and not SUPresent:
                    StandUsers = True
                    SUPresent = True
                ModifierList.append(m)
            random.shuffle(RoleList)
            random.shuffle(ModifierList)
            combined = "```md\n"
            for i in range(0,len(PlayerList)):
                string = "[+][{}] - {} {}\n" .format(PlayerList[i],RoleList[i],ModifierList[i])
                combined = combined+string
            finish = "```\n"
            combined = combined+finish
            if "Bard Minstrel" in combined:
                continue
            elif combined.count("Minstrel") == 1:
                continue
            elif combined.count("Stand User") == 1:
                continue
            elif combined.count("Twin") % 2 != 0:
                continue
            elif [i for i in ["Backstabber {}".format(m) for m in Modifiers] if i in combined] != []:
                continue
            elif [i for i in ["{} Conduit".format(a) for a in AllRoles if a not in [r for r in AllRoles if r in HumanRoles and r in KillingRoles]] if i in combined] != []:
                continue
            else:
                break
        giveroles = "w.giveroles "
        for p in range(0,len(PlayerList)):
            if p == len(PlayerList)-1:
                end = ""
            else:
                end = ", "
            if ModifierList[p] != "":
                if "Twin" in ModifierList[p]:
                    ModifierList[p] = "Twin"
                giveroles = "{}{}: {} ({}){}".format(giveroles,PlayerList[p].lower(),RoleList[p],ModifierList[p],end)
            else:
                giveroles = "{}{}: {}{}".format(giveroles,PlayerList[p].lower(),RoleList[p],end)
        combined = "{}`{}`".format(combined,giveroles)
        await ctx.send(combined)

@generatelist.command(pass_context=True)
async def anons(ctx, *, message: str):
    message = message.split(" : ")
    PlayerList = message[0]
    RoleList = message[1]
    if len(PlayerList) != len(RoleList):
        await ctx.send("Needs to have equal amount of players and roles!")
    elif len(PlayerList) < 8:
        await ctx.send("Not enough players, sorry.")
    else:
        PlayerList = PlayerList.split(", ")
        RoleList = RoleList.split(", ")
        PlayerList = sorted(PlayerList)
        random.shuffle(RoleList)
        combined = "```md\n"
        for i in range(0,len(PlayerList)):
            string = "[+][{}] - {}\n" .format(PlayerList[i],RoleList[i])
            combined = combined+string
        finish = "```"
        combined = combined+finish
        await ctx.send(combined)

@generatelist.command(pass_context=True)
async def duality(ctx, *, message: str):
    PlayerList = message.split(", ")
    PlayerList = sorted(PlayerList)
    if len(PlayerList) % 2 != 0:
        await ctx.send("Needs to be an even number of players!")
    elif len(PlayerList) < 8:
        await ctx.send("Not enough players, sorry.")
    else:
        Invest = list(InvestigativeRoles)
        Kill = list(KillingRoles)
        i = ["Time Lord", "Whisperer", "Mage", "Hacker", "Noir"]
        for r in i:
            Invest.remove(r)
        k = ["Jester", "Werewolf", "Direwolf", "Bard", "Inventor", "Gladiator", "Hooligan", "Politician", "Shinigami", "Hunter", "Backstabber", "Arsonist"]
        for r in k:
            Kill.remove(r)
        for r in AchievableRoles:
            if r in Invest:
                Invest.remove(r)
            if r in Kill:
                Kill.remove(r)
        t = int(len(PlayerList)/2)
        RoleList = []
        for sets in range(0,t):
            iRole = random.choice(Invest)
            kRole = random.choice(Kill)
            iRole = "{} Twin {}".format(iRole,(sets+1))
            kRole = "{} Twin {}".format(kRole,(sets+1))
            RoleList.append(iRole)
            RoleList.append(kRole)
        random.shuffle(RoleList)
        combined = "```md\n"
        for i in range(0,len(PlayerList)):
            string = "[+][{}] - {}\n" .format(PlayerList[i],RoleList[i])
            combined = combined+string
        finish = "```"
        combined = combined+finish
        await ctx.send(combined)

@generatelist.command(pass_context=True)
async def morals(ctx, *, message: str):
    PlayerList = message.split(", ")
    PlayerList = sorted(PlayerList)
    if len(PlayerList) < 8:
        await ctx.send("Not enough players, sorry.")
    else:
        EvilCount = 1
        GoodCount = 1
        NeutralCount = 0
        x = round(len(PlayerList)/8)
        for i in range(0, x):
            EvilCount = EvilCount+1
        y = random.randint((round(len(PlayerList)/3)), (round(len(PlayerList)/1.5)))
        for i in range(0, y):
            GoodCount = GoodCount+1
        for i in range(0, round((GoodCount-EvilCount)/2)):
            EvilCount = EvilCount+1
        for i in range(0,(len(PlayerList)-GoodCount-EvilCount)):
            NeutralCount = NeutralCount+1
        Alignments = []
        for c in range(0, EvilCount):
            Alignments.append("Evil")
        for c in range(0, GoodCount):
            Alignments.append("Good")
        for c in range(0, NeutralCount):
            Alignments.append("Neutral")
        random.shuffle(Alignments)
        combined = "```md\n"
        for i in range(0,len(PlayerList)):
            string = "[+][{}] - {}\n" .format(PlayerList[i],Alignments[i])
            combined = combined+string
        finish = "```"
        combined = combined+finish
        await ctx.send(combined)

@generatelist.command(pass_context=True)
async def tac(ctx, *, message: str):
    PlayerList = message.split(", ")
    PlayerList = sorted(PlayerList)
    if len(PlayerList) < 6:
        await ctx.send("Not enough players, sorry.")
    else:
        RoleList = []
        for i in range(0,round(len(PlayerList)/10+0.49999)):
            RoleList.append("Good Knight")
            RoleList.append("Evil Werewolf")
        for i in range(0,round(3*len(PlayerList)/5-0.49999)):
            RoleList.append("Good Time Lord")
        for i in range(0,(len(PlayerList)-len(RoleList))):
            RoleList.append("Evil Time Lord")
        random.shuffle(RoleList)
        combined = "```md\n"
        for i in range(0,len(PlayerList)):
            string = "[+][{}] - {}\n" .format(PlayerList[i],RoleList[i])
            combined = combined+string
        finish = "```"
        combined = combined+finish
        await ctx.send(combined)

async def KeepAwake():
    await asyncio.sleep(1500)
    print("Still awake.")

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    client.loop.create_task(KeepAwake())
    client.run(TOKEN)
