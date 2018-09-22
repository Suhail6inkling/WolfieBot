import discord
from discord.ext import commands
import random


class Other():
    
    def __init__(self,client):
        self.client = client
    
    @commands.command(pass_context=True)
    async def rolelist(ctx):
        await ctx.send("""__**Roles**__
```md
[+][Alchemist] - Neutral, Chaos/Support, Arcane, Unique - <w.roles_alchemist>
[+][Arsonist] - Neutral, Killing, Human, Unique - <w.roles_arsonist>
[+][Backstabber] - Evil, Counteractive/Killing, Human, Unique - <w.roles_backstabber>
[+][Bard] - Neutral, Chaos/Killing, Human, Unique - <w.roles_bard>
[+][Baykok] - Evil, Counteractive/Killing, Ethereal, Unique - <w.roles_baykok>
[+][Bloodhound] - Evil, Killing/Support, Wolf, Unique, Achievable - <w.roles_bloodhound>
[+][Clockmaker] - Neutral, Killing, Human - <w.roles_clockmaker>
[+][Companion] - Modifier, Achievable - <w.roles_companion>
[+][Conduit] - Modifier - <w.roles_conduit>
[+][Cultist] - Evil, Counteractive/Support, Human, Unique - <w.roles_cultist>
[+][Cyberhound] - Evil, Counteractive/Killing, Wolf, Unique, Achievable - <w.roles_cyberhound>
[+][Dentist] - Evil, Counteractive, Human, Unique - <w.roles_dentist>
[+][Direwolf] - Evil, Killing/Support, Wolf, Unique - <w.roles_direwolf>
[+][Doctor] - Good, Killing/Protective, Human - <w.roles_doctor>
[+][Dodomeki] - Evil, Investigative, Unearthly, Unique, Achievable - <w.roles_dodomeki>
[+][Emissary] - Neutral, Protective/Support, Human, Achievable - <w.roles_emissary>
[+][Drunk] - Neutral, Chaos, Human, Unique - <w.roles_drunk>
[+][Fate] - Neutral, Chaos/Support, Unearthly, Unique - <w.roles_fate>
[+][Feral] - Modifier - <w.roles_feral>
[+][Geneticist] - Neutral, Chaos/Support, Human, Unique - <w.roles_geneticist>
[+][Gladiator] - Good, Counteractive/Killing, Human, Unique - <w.roles_gladiator>
[+][Glazier] - Good, Counteractive, Human - <w.roles_glazier>
[+][Glitch] - Neutral, Chaos, Ethereal, Unique - <w.roles_glitch>
[+][Guide] - Modifier, Achievable - <w.roles_guide>
```""")
        await ctx.send("""```md
[+][Hacker] - Good, Investigative/Support, Human, Unique, Achievable - <w.roles_hacker>
[+][Hangman] - Neutral, Chaos/Counteractive, Human, Unique - <w.roles_hangman>
[+][Harbinger] - Neutral, Chaos/Killing, Unearthly, Unique - <w.roles_harbinger>
[+][Heir] - Evil, Killing, Human, Unique - <w.roles_heir>
[+][Herald] - Neutral, Chaos/Killing, Arcane, Unique, Achievable - <w.roles_herald>
[+][Hermit] - Neutral, Investigative/Counteractive, Human, Unique - <w.roles_hermit>
[+][Hitman] - Neutral, Killing, Human - <w.roles_hitman>
[+][Hooligan] - Evil, Killing/Support, Human - <w.roles_hooligan>
[+][Hunter] - Good, Killing/Protective, Human - <w.roles_hunter>
[+][Inevitable] - Neutral, Killing, Unearthly, Unique, Achievable - <w.roles_inevitable>
[+][Inventor] - Neutral, Chaos/Killing, Human, Unique - <w.roles_inventor>
[+][Jailor] - Good, Counteractive/Protective, Human, Unique - <w.roles_jailor>
[+][Jester] - Evil, Chaos/Killing, Ethereal - <w.roles_jester>
[+][Knight] - Good, Killing/Support, Human, Unique - <w.roles_knight>
[+][Kresnik] - Good, Investigative/Killing, Arcane, Unique - <w.roles_kresnik>
[+][Mage] - Good, Chaos/Investigative, Arcane - <w.roles_mage>
[+][Maid] - Neutral, Chaos/Killing, Human, Unique - <w.roles_maid>
[+][Medium] - Good, Support, Arcane - <w.roles_medium>
[+][Merchant] - Neutral, Chaos/Support, Human, Unique - <w.roles_merchant>
[+][Minstrel] - Modifier, Achievable - <w.roles_minstrel>
[+][Morty] - Modifier - <w.roles_morty>
[+][Multiple Agent] - Neutral, Chaos/Protective, Human - <w.roles_multipleagent>
[+][Noir] - Good, Investigative/Killing, Human, Unique - <w.roles_noir>
```""")
        await ctx.send("""```md
[+][Page] - Neutral, Support, Human, Unique - <w.roles_page>
[+][Paladin] - Good, Counteractive/Protective, Arcane, Unique, Achievable - <w.roles_paladin>
[+][Philanthropist] - Neutral, Counteractive/Support, Human, Unique - <w.roles_philanthropist>
[+][Pixie] - Good, Counteractive/Investigative, Unearthly - <w.roles_pixie>
[+][Politician] - Evil, Killing/Support, Human, Unique - <w.roles_politician>
[+][Poltergeist] - Evil, Chaos/Investigative, Ethereal - <w.roles_poltergeist>
[+][Poser] - Good, Support, Human - <w.roles_poser>
[+][Priest] - Good, Counteractive/Support, Human, Unique - <w.roles_priest>
[+][Prince] - Good, Support, Human, Unique - <w.roles_prince>
[+][Psychic] - Evil, Chaos/Support, Arcane, Unique - <w.roles_psychic>
[+][Researcher] - Good, Investigative, Human, Unique - <w.roles_researcher>
[+][Rogue] - Good, Counteractive/Protective, Human, Unique - <w.roles_rogue>
[+][Rōjinbi] - Neutral, Chaos, Ethereal, Unique - <w.roles_rojinbi>
[+][Romantic] - Neutral, Protective, Human, Unique - <w.roles_romantic>
[+][Santa] - Neutral, Support, Unearthly, Unique - <w.roles_santa>
[+][Scarecrow] - Neutral, Chaos/Support, Ethereal, Unique - <w.roles_scarecrow>
[+][Seer] - Good, Investigative, Arcane - <w.roles_seer>
[+][Sentinel] - Neutral, Protective, Unearthly - <w.roles_sentinel>
[+][Sharpshooter] - Good, Investigative/Killing, Human, Unique - <w.roles_sharpshooter>
[+][Shifter] - Neutral, Chaos, Ethereal - <w.roles_shifter>
[+][Shinigami] - Evil, Counteractive/Killing, Unearthly, Unique - <w.roles_shinigami>
[+][Slasher] - Neutral, Chaos/Killing, Unearthly, Unique - <w.roles_slasher>
[+][Souleater] - Neutral, Chaos/Killing, Ethereal, Achievable - <w.roles_souleater>
```""")
        await ctx.send("""```md
[+][Soulless] - Modifier, Achievable - <w.roles_soulless>
[+][Spectre] - Modifier, Achievable - <w.roles_spectre>
[+][Speedster] - Modifier - <w.roles_speedster>
[+][Spider] - Evil, Counteractive/Support, Unearthly, Unique - <w.roles_spider>
[+][Spinster] - Neutral, Support, Unearthly, Unique, Achievable - <w.roles_spinster>
[+][Spy] - Good, Investigative, Human - <w.roles_spy>
[+][Stand User] - Modifier - <w.roles_standuser>
[+][Survivalist] - Neutral, Counteractive, Human - <w.roles_survivalist>
[+][Sylph] - Good, Support, Ethereal, Unique - <w.roles_sylph>
[+][TARDIS Engineer] - Good, Protective/Support, Human, Unique, Achievable - <w.roles_tardisengineer>
[+][Thief] - Neutral, Chaos/Counteractive, Human, Unique - <w.roles_thief>
[+][Time Lord] - Good, Investigative/Support, Unearthly - <w.roles_timelord>
[+][Twin] - Modifier - <w.roles_twin>
[+][Understudy] - Neutral, Chaos/Support, Human, Unique - <w.roles_understudy>
[+][Vampire] - Evil, Support, Unearthly, Unique - <w.roles_vampire>
[+][Warlock] - Evil, Chaos/Killing, Arcane, Unique, Achievable - <w.roles_warlock>
[+][Werewolf] - Evil, Killing, Wolf - <w.roles_werewolf>
[+][Whisperer] - Good, Investigative/Support, Arcane, Unique - <w.roles_whisperer>
[+][Witch] - Neutral, Killing/Protective, Unearthly - <w.roles_witch>
```""")

    @commands.command(pass_context=True)
    async def factionlist(ctx):
        await ctx.send("""__**Factions**__
```md
[+][Coven] - <w.listroles coven>
[+][Prophets] - <w.listroles prophets>
[+][School] - <w.listroles school>
[+][Tardis] - <w.listroles tardis>
[+][Troupe] - <w.listroles troupe>
[+][Vampiric] - <w.listroles vampiric>
[+][Witches] - <w.listroles witches>
[+][Wolves] - <w.listroles wolves>
```""")

    @commands.command(pass_context=True)
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

    @commands.command(pass_context=True)
    async def stats(ctx, user: discord.Member=None):
        if user == None:
            user = ctx.message.author
        await ctx.trigger_typing()
        info = await GetStats(user.id)
        if info == "Error":
            await ctx.send("There is no information for that user!")
        else:
            if info["ACHIEVEMENTS"] == "":
                info["ACHIEVEMENTS"] = "None :("
            colour = user.colour
            if colour == discord.Colour.default():
                colour = discord.Embed.Empty
            embed=discord.Embed(description=""":white_small_square: __**All Time**__
        - Wins: **{}**     - Losses: **{}**
        - Score: **{}**    - Rank: **{}**
        
:white_small_square: __**Monthly**__
        - Wins: **{}**     - Losses: **{}**
        - Score: **{}**    - Rank: **{}**

:white_small_square: __**Games Played**__
        - Overall: **{}**  - Rank: **{}**

:white_small_square: __**Achievements**__
        {}

:white_small_square: __**Miscellaneous**__
        - Winstreak (Best): **{}**
        - Lossstreak (Worst): **{}**
        - Kills: **{}**""".format(info["WINS"],info["LOSSES"],info["SCORE"],info["AT RANK"],info["M WINS"],info["M LOSSES"],info["M SCORE"],info["M RANK"],info["GAMES PLAYED"],info["GP RANK"],
                     info["ACHIEVEMENTS"],info["WIN STREAK"],info["LOSS STREAK"],info["KILLS"]),colour=colour)
            embed.set_thumbnail(url=user.avatar_url)
            name = user.nick
            if name == None:
                name = user.name
            await ctx.send("Stats for **{}**:".format(name),embed=embed)

    @commands.command(pass_context=True)
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

    @commands.command(pass_context=True)
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
> Arcane
> Ethereal
> Unearthly
> Wolf
> Chaos
> Counteractive
> Investigative
> Killing
> Protective
> Support
> Unique
> Achievable
> [Factions]*

*Factions can be viewed with <w.factionlist>.
Include 'all' in parameters to discard parameters and allow all roles and modifiers.
Include 'modifier' in parameters to limit selection to modifiers.
Include 'x-modifier' in parameters to exclude modifiers.
Precede tags with 'x-' to exclude roles with them.
Precede categories with 'o-' to exclude roles with two categories.

Example: <w.randomrole good>
Output: 'Jailor'```""")
        else:
            conditions = message.split(" ")
            for c in conditions:
                c = c.lower()
            All = list(AllRoles + Modifiers)
            Valid = list(All)
            ref = {"good" : [r for r in AllRoles if Alignments[r] == "G"], "evil" : [r for r in AllRoles if Alignments[r] == "E"],
                "neutral" : [r for r in AllRoles if Alignments[r] == "N"],
                "chaos" : [r for r in AllRoles if "Ch" in Categories[r]], "counteractive" : [r for r in AllRoles if "Co" in Categories[r]],
                "investigative" : [r for r in AllRoles if "I" in Categories[r]], "killing" : [r for r in AllRoles if "K" in Categories[r]],
                "protective" : [r for r in AllRoles if "P" in Categories[r]], "support" : [r for r in AllRoles if "S" in Categories[r]],
                "human" : [r for r in AllRoles if "Human" == Species[r]], "arcane" : [r for r in AllRoles if "Arcane" == Species[r]],
                "ethereal" : [r for r in AllRoles if "Ethereal" == Species[r]], "unearthly" : [r for r in AllRoles if "Unearthly" == Species[r]],
                "wolf" : [r for r in AllRoles if "Wolf" == Species[r]],
                "unique" : [r for r in AllRoles if r in UniqueRoles], "achievable" : [r for r in All if r in AchievableRoles + AchievableModifiers],
                "modifier" : Modifiers, "x-modifier" : AllRoles,
                "coven" : [r for r in All if "Coven" in Factions[r]], "prophets" : [r for r in All if "Prophets" in Factions[r]],
                "school" : [r for r in All if "School" in Factions[r]], "troupe" : [r for r in All if "Troupe" in Factions[r]],
                "vampiric" : [r for r in All if "Vampiric" in Factions[r]], "witches" : [r for r in All if "Witches" in Factions[r]],
                "wolves" : [r for r in All if "Wolves" in Factions[r]], "tardis" : [r for r in All if "Tardis" in Factions[r]],
                "x-good" : [r for r in AllRoles if Alignments[r] != "G"], "x-evil" : [r for r in AllRoles if Alignments[r] != "E"],
                "x-neutral" : [r for r in AllRoles if Alignments[r] != "N"],
                "x-chaos" : [r for r in AllRoles if "Ch" not in Categories[r]], "x-counteractive" : [r for r in AllRoles if "Co" not in Categories[r]],
                "x-investigative" : [r for r in AllRoles if "I" not in Categories[r]], "x-killing" : [r for r in AllRoles if "K" not in Categories[r]],
                "x-protective" : [r for r in AllRoles if "P" not in Categories[r]], "x-support" : [r for r in AllRoles if "S" not in Categories[r]],
                "x-human" : [r for r in AllRoles if "Human" != Species[r]], "x-arcane" : [r for r in AllRoles if "Arcane" != Species[r]],
                "x-ethereal" : [r for r in AllRoles if "Ethereal" != Species[r]], "x-unearthly" : [r for r in AllRoles if "Unearthly" != Species[r]],
                "x-wolf" : [r for r in AllRoles if "Wolf" != Species[r]],
                "x-unique" : [r for r in AllRoles if r not in UniqueRoles], "x-achievable" : [r for r in All if r not in AchievableRoles + AchievableModifiers],
                "x-coven" : [r for r in All if "Coven" not in Factions[r]], "x-prophets" : [r for r in All if "Prophets" not in Factions[r]],
                "x-school" : [r for r in All if "School" not in Factions[r]], "x-troupe" : [r for r in All if "Troupe" not in Factions[r]],
                "x-vampiric" : [r for r in All if "Vampiric" not in Factions[r]], "x-witches" : [r for r in All if "Witches" not in Factions[r]],
                "x-wolves" : [r for r in All if "Wolves" not in Factions[r]], "x-tardis" : [r for r in All if "Tardis" not in Factions[r]],
                "o-chaos" : [r for r in AllRoles if ["Ch"] == Categories[r]], "o-counteractive" : [r for r in AllRoles if ["Co"] == Categories[r]],
                "o-investigative" : [r for r in AllRoles if ["I"] == Categories[r]], "o-killing" : [r for r in AllRoles if ["K"] == Categories[r]],
                "o-protective" : [r for r in AllRoles if ["P"] == Categories[r]], "o-support" : [r for r in AllRoles if ["S"] == Categories[r]],
                "o-coven" : [r for r in All if ["Coven"] == Factions[r]], "o-prophets" : [r for r in All if ["Prophets"] == Factions[r]],
                "o-school" : [r for r in All if ["School"] == Factions[r]], "o-troupe" : [r for r in All if ["Troupe"] == Factions[r]],
                "o-vampiric" : [r for r in All if ["Vampiric"] == Factions[r]], "o-witches" : [r for r in All if ["Witches"] == Factions[r]],
                "o-wolves" : [r for r in All if ["Wolves"] == Factions[r]], "o-tardis" : [r for r in All if ["Tardis"] == Factions[r]]}
            if message.lower() != "all":
                for r in All:
                    for c in conditions:
                        if c in ref:
                            if r not in ref[c]:
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

    @commands.command(pass_context=True)
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
> Arcane
> Ethereal
> Unearthly
> Wolf
> Chaos
> Counteractive
> Investigative
> Killing
> Protective
> Support
> Unique
> Achievable
> [Factions]*

*Factions can be viewed with <w.factionlist>.
Include 'all' in parameters to discard parameters and allow all roles and modifiers.
Include 'modifier' in parameters to limit selection to modifiers.
Include 'x-modifier' in parameters to exclude modifiers.
Precede tags with 'x-' to exclude roles with them.
Precede categories with 'o-' to exclude roles with two categories.

Example: <w.listroles wolf>
Output: '4 roles found:
 - Cyberhound
 - Direwolf
 - Werewolf
 - Bloodhound'```""")
        else:
            conditions = message.split(" ")
            for c in conditions:
                c = c.lower()
            All = list(AllRoles + Modifiers)
            Valid = list(All)
            ref = {"good" : [r for r in AllRoles if Alignments[r] == "G"], "evil" : [r for r in AllRoles if Alignments[r] == "E"],
                "neutral" : [r for r in AllRoles if Alignments[r] == "N"],
                "chaos" : [r for r in AllRoles if "Ch" in Categories[r]], "counteractive" : [r for r in AllRoles if "Co" in Categories[r]],
                "investigative" : [r for r in AllRoles if "I" in Categories[r]], "killing" : [r for r in AllRoles if "K" in Categories[r]],
                "protective" : [r for r in AllRoles if "P" in Categories[r]], "support" : [r for r in AllRoles if "S" in Categories[r]],
                "human" : [r for r in AllRoles if "Human" == Species[r]], "arcane" : [r for r in AllRoles if "Arcane" == Species[r]],
                "ethereal" : [r for r in AllRoles if "Ethereal" == Species[r]], "unearthly" : [r for r in AllRoles if "Unearthly" == Species[r]],
                "wolf" : [r for r in AllRoles if "Wolf" == Species[r]],
                "unique" : [r for r in AllRoles if r in UniqueRoles], "achievable" : [r for r in All if r in AchievableRoles + AchievableModifiers],
                "modifier" : Modifiers, "x-modifier" : AllRoles,
                "coven" : [r for r in All if "Coven" in Factions[r]], "prophets" : [r for r in All if "Prophets" in Factions[r]],
                "school" : [r for r in All if "School" in Factions[r]], "troupe" : [r for r in All if "Troupe" in Factions[r]],
                "vampiric" : [r for r in All if "Vampiric" in Factions[r]], "witches" : [r for r in All if "Witches" in Factions[r]],
                "wolves" : [r for r in All if "Wolves" in Factions[r]],
                "x-good" : [r for r in AllRoles if Alignments[r] != "G"], "x-evil" : [r for r in AllRoles if Alignments[r] != "E"],
                "x-neutral" : [r for r in AllRoles if Alignments[r] != "N"],
                "x-chaos" : [r for r in AllRoles if "Ch" not in Categories[r]], "x-counteractive" : [r for r in AllRoles if "Co" not in Categories[r]],
                "x-investigative" : [r for r in AllRoles if "I" not in Categories[r]], "x-killing" : [r for r in AllRoles if "K" not in Categories[r]],
                "x-protective" : [r for r in AllRoles if "P" not in Categories[r]], "x-support" : [r for r in AllRoles if "S" not in Categories[r]],
                "x-human" : [r for r in AllRoles if "Human" != Species[r]], "x-arcane" : [r for r in AllRoles if "Arcane" != Species[r]],
                "x-ethereal" : [r for r in AllRoles if "Ethereal" != Species[r]], "x-unearthly" : [r for r in AllRoles if "Unearthly" != Species[r]],
                "x-wolf" : [r for r in AllRoles if "Wolf" != Species[r]],
                "x-unique" : [r for r in AllRoles if r not in UniqueRoles], "x-achievable" : [r for r in All if r not in AchievableRoles + AchievableModifiers],
                "x-coven" : [r for r in All if "Coven" not in Factions[r]], "x-prophets" : [r for r in All if "Prophets" not in Factions[r]],
                "x-school" : [r for r in All if "School" not in Factions[r]], "x-troupe" : [r for r in All if "Troupe" not in Factions[r]],
                "x-vampiric" : [r for r in All if "Vampiric" not in Factions[r]], "x-witches" : [r for r in All if "Witches" not in Factions[r]],
                "x-wolves" : [r for r in All if "Wolves" not in Factions[r]],
                "o-chaos" : [r for r in AllRoles if ["Ch"] == Categories[r]], "o-counteractive" : [r for r in AllRoles if ["Co"] == Categories[r]],
                "o-investigative" : [r for r in AllRoles if ["I"] == Categories[r]], "o-killing" : [r for r in AllRoles if ["K"] == Categories[r]],
                "o-protective" : [r for r in AllRoles if ["P"] == Categories[r]], "o-support" : [r for r in AllRoles if ["S"] == Categories[r]],
                "o-coven" : [r for r in All if ["Coven"] == Factions[r]], "o-prophets" : [r for r in All if ["Prophets"] == Factions[r]],
                "o-school" : [r for r in All if ["School"] == Factions[r]], "o-troupe" : [r for r in All if ["Troupe"] == Factions[r]],
                "o-vampiric" : [r for r in All if ["Vampiric"] == Factions[r]], "o-witches" : [r for r in All if ["Witches"] == Factions[r]],
                "o-wolves" : [r for r in All if ["Wolves"] == Factions[r]]}
            if message.lower() != "all":
                for r in All:
                    for c in conditions:
                        if c in ref:
                            if r not in ref[c]:
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

    @commands.command(pass_context=True)
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

    @commands.command(pass_context=True)
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
                        "Emissary" : "- Target the Harbinger with an action that would cause them to change alignment.\n- Survive *End of Days*.\n- (Random) Be a Drunk in a game where the Harbinger is present.",
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

    @commands.command(pass_context=True)
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

    @commands.command(pass_context=True)
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

    @commands.command(pass_context=True)
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

    @commands.command(pass_context=True)
    async def magic8ball(ctx):
        results = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes, definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yep.",
                "Signs point to yes.", "Reply hazy. Try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
                "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
        await ctx.send(random.choice(results))

    @commands.command(pass_context=True)
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
            if type(message) == list:
                options = message
            else:
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

    @commands.command(pass_context=True)
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

    @commands.command(pass_context=True)
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

    async def GetStats(ID):
            scope = ['https://spreadsheets.google.com/feeds',
                    'https://www.googleapis.com/auth/drive']
            creds = SAC.from_json_keyfile_name("google api.json", scope)
            gclient = gspread.authorize(creds)
            sheet = gclient.open_by_key("1TrCrVmpjocMevw5iEj8L0xNQywwRQ5iWoa28gnJrkMQ").worksheet("Summary")
            records = sheet.get_all_records()
            info = [d for d in records if d["USERID"] == ID or d["ALT USERID"] == ID]
            if info == []:
                return "Error"
            else:
                return info[0]
def setup(client):
    client.add_cog(Other(client))