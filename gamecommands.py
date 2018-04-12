import discord
from discord.ext import commands
import asyncio
from wolfiebot import *
from roles import *

# PlayerInfo structure:
# player : [user, channel ref, role, [modifiers], alignment, alive/dead]

global NeedDeputy
NeedDeputy = True

class GameCommands():
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def setplayers(self, ctx):
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            player_role = discord.utils.get(ctx.message.guild.roles, name="Player")
            players = ctx.message.mentions
            for p in players:
                if "Player" not in [y.name for y in p.roles]:
                    await p.add_roles(player_role)
                else:
                    await p.remove_roles(player_role)
        else:
            await ctx.send("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def endgame(self, ctx):
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            global Day, DayCount
            Day = False
            player_role = discord.utils.get(ctx.message.guild.roles, name="Player")
            dead_role = discord.utils.get(ctx.message.guild.roles, name="Dead")
            mayor_role = discord.utils.get(ctx.message.guild.roles, name="Mayor")
            deputy_role = discord.utils.get(ctx.message.guild.roles, name="Deputy")
            guild = ctx.message.guild
            for user in [m for m in guild.members if player_role in m.roles]:
                await user.remove_roles(player_role)
            for user in [m for m in guild.members if dead_role in m.roles]:
                await user.remove_roles(dead_role)
            for user in [m for m in guild.members if mayor_role in m.roles]:
                await user.remove_roles(mayor_role)
            for user in [m for m in guild.members if deputy_role in m.roles]:
                await user.remove_roles(deputy_role)
            gamechans = ["wolves", "coven", "twins", "tardis", "seance", "guide", "vampires"]
            for c in [c for c in guild.channels]:
                if c.name in gamechans:
                    await c.delete()
            game_channel = self.client.get_channel(392995027909083137)
            voting_channel = self.client.get_channel(393470084217176075)
            perms = discord.PermissionOverwrite()
            perms.read_messages = True
            perms.send_messages = False
            perms.add_reactions = True      
            await voting_channel.set_permissions(player_role, overwrite=perms)
            perms = discord.PermissionOverwrite()
            perms.send_messages = True
            perms.add_reactions = True
            await game_channel.set_permissions(player_role, overwrite=perms)
            for user in guild.members:
                await ctx.invoke(self.client.get_command("lockjaw"),user=user,status="f")
                await ctx.invoke(self.client.get_command("medium"),user=user,status="f")
            await ctx.send("Game ended successfully!")
        else:
            await ctx.send("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def rungame(self, ctx, *, message: str):
        global PlayerInfo, NeedDeputy
        await ctx.send("This command is in development.")
        return
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            game_channel = self.client.get_channel(392995027909083137)
            voting_channel = self.client.get_channel(393470084217176075)
            notes_channel = self.client.get_channel(393476547954212874)
            dead_channel = self.client.get_channel(392995124423950344)
            player_role = discord.utils.get(ctx.message.guild.roles, name="Player")
            message = message.split("; ")
            gamemode = message[0]
            await ctx.invoke(self.client.get_command("giveroles",message=message[1]))
            report = "Game Start!"
            if "Cultist" in [PlayerInfo[p][2] for p in PlayerInfo]:
                report == "{}/A Cultist is present in this game!".format(report)
            if "Priest" in [PlayerInfo[p][2] for p in PlayerInfo]:
                report == "{}/A Priest is present in this game!".format(report)
            if "Merchant" in [PlayerInfo[p][2] for p in PlayerInfo]:
                report == "{}/A Merchant is present in this game!".format(report)
            DayCount = 0
            time = 900
            while True:
                DayCount = DayCount+1
                report = "{}; {}; {}".format(DayCount,time,report)
                await ctx.invoke(self.client.get_command("daytimer"),message=report)
                mayor_role = discord.utils.get(ctx.message.guild.roles, name="Mayor")
                deputy_role = discord.utils.get(ctx.message.guild.roles, name="Deputy")
                if mayor_role not in [x for y in [p.roles for p in ctx.message.guild.members if player_role in p.roles] for x in y]:
                    if deputy_role in [x for y in [p.roles for p in ctx.message.guild.members if player_role in p.roles] for x in y]:
                        deputy = [p for p in ctx.message.guild.members if deputy_role in p.roles][0]
                        await deputy.add_roles(mayor_role)
                        await deputy.remove_roles(deputy_role)
                        await game_channel.send("{} has become Mayor! Choose your deputy with *w.choosedeputy @player*.".format(deputy.mention))
                        NeedDeputy = True
                        while NeedDeputy == True:
                            await asyncio.sleep(5)
                    else:
                        await voting_channel.send("MAYORAL ELECTION")
                        mayor = await ctx.invoke(self.client.get_command("playervote"),s=time)
                        elected = [p for p in ctx.message.guild.members if p.nick == mayor][0]
                        await elected.add_roles(mayor_role)
                        await game_channel.send("{} has been elected as Mayor! Choose your deputy with *w.choosedeputy @player*.".format(elected.mention))
                        NeedDeputy = True
                        while NeedDeputy == True:
                            await asyncio.sleep(5)
                if DayCount != 1:
                    await voting_channel.send("LYNCH")
                    lynched = await ctx.invoke(self.client.get_command("playervote"),s=time)
                    lynched = [p for p in ctx.message.guild.members if p.nick == lynched][0]
                    if True: # if not saved
                        await ctx.invoke(self.client.get_command("kill"),player=lynched.mention)
                        await game_channel.send("{} has been voted to be Lynched!\n\nThey were a {} {}!".format(lynched.mention))
                        # message declaring lynched, role
                    else: # if saved
                        await game_channel.send("{} has been voted to be Lynched!\n\nBut they were saved!".format(lynched.mention))
                        # remove used up save
                # keep working on this
        else:
            await ctx.send("You need to be a GM to use this command!")

    #giveroles command using classes
    """@commands.command(pass_context=True)
    async def giveroles(self, ctx, *, message: str, wolvesclass=None):
        global PlayerInfo
        notes_channel = self.client.get_channel(393476547954212874)
        chan = await ctx.invoke(self.client.get_command("wolves"))
        wolvesclass = Wolves(chan)
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            message = message.split(", ")
            x = []
            for m in message:
                m = m.split(": ")
                m[0] = m[0].lower()
                m[0] = m[0].replace(" ","-")
                name = m[0]
                if "(" in m[1]:
                    y = m[1].split(" (")
                    m[1] = y[0]
                    modifier = y[1]
                    m.append(modifier[:-1])
                else:
                    m.append(None)
                gm_role = discord.utils.get(ctx.message.guild.roles, name="Game Master")
                bot_role = discord.utils.get(ctx.message.guild.roles, name="Bots")
                narr_role = discord.utils.get(ctx.message.guild.roles, name="Narrator")
                chan = discord.utils.get(ctx.message.guild.channels, name="{}-priv".format(m[0]))
                user = [u for u in ctx.message.guild.members if chan.permissions_for(u).read_messages == True and gm_role not in u.roles and bot_role not in u.roles and narr_role not in u.roles][0]
                if m[1] in WolfRoles:
                    role = roleclasses[m[1]](wolvesclass)
                else:
                    role = roleclasses[m[1]]()
                try:
                    if m[2] != None:
                        m = Player(user, chan, role, roleclasses[m[2]]())
                    else:
                        m = Player(user, chan, role)
                except KeyError:
                    await ctx.send("There was a problem applying {}'s roles.".format(name))
                    return
                x.append([name,m])
            PlayerInfo = {p[0] : p[1] for p in x}
            for player in PlayerInfo:
                if PlayerInfo[player].alignment == "Good" or PlayerInfo[player].alignment == "Neutral":
                    a = " {}".format(PlayerInfo[player].alignment)
                elif PlayerInfo[player].alignment == "Evil":
                    a = "n {}".format(PlayerInfo[player].alignment)
                if PlayerInfo[player].modifiers != []:
                    output = "You are a{} {}{}!".format(a,PlayerInfo[player].role.name,PlayerInfo[player].modifiers[0])
                else:
                    output = "You are a{} {}{}!".format(a,PlayerInfo[player].role.name)
                await PlayerInfo[player][1].send(output)
                await ctx.invoke(self.client.get_command(descCommands[PlayerInfo[player].role]), where=PlayerInfo[player].privchannel)
                if PlayerInfo[player].modifiers != []:
                    await ctx.invoke(self.client.get_command(descCommands[PlayerInfo[player].modifiers[0]]), where=PlayerInfo[player].privchannel)
            rolereport = ""
            for p in sorted(list(PlayerInfo)):
                mod = ""
                for m in PlayerInfo[p].modifiers:
                    mod = "{} {}".format(mod,m)
                rolereport = ("{}{} - {} {}{}\n".format(rolereport,p.title(),PlayerInfo[p].alignment,PlayerInfo[p].role.name,mod))
            await notes_channel.send(rolereport)
        else:
            await ctx.send("You need to be a GM to use this command!")"""

    @commands.command(pass_context=True)
    async def giveroles(self, ctx, *, message: str):
        global PlayerInfo
        notes_channel = self.client.get_channel(393476547954212874)
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            message = message.split(", ")
            x = []
            for m in message:
                m = m.split(": ")
                m[0] = m[0].lower()
                m[0] = m[0].replace(" ","-")
                if "(" in m[1]:
                    y = m[1].split(" (")
                    m[1] = y[0]
                    modifier = y[1]
                    m.append(modifier[:-1])
                else:
                    m.append("")
                chan = discord.utils.get(ctx.message.guild.channels, name="{}-priv".format(m[0]))
                m.append(chan)
                gm_role = discord.utils.get(ctx.message.guild.roles, name="Game Master")
                bot_role = discord.utils.get(ctx.message.guild.roles, name="Bots")
                narr_role = discord.utils.get(ctx.message.guild.roles, name="Narrator")
                user = [u for u in ctx.message.guild.members if chan.permissions_for(u).read_messages == True and gm_role not in u.roles and bot_role not in u.roles and narr_role not in u.roles][0]
                m.append(user)
                x.append(m)
            PlayerInfo = {m[0] : [m[4], m[3], m[1], [m[2]]] for m in x}
            for player in PlayerInfo:
                if PlayerInfo[player][3] == [""]:
                    PlayerInfo[player][3] = []
                    modifier = False
                else:
                    modifier = True
                if PlayerInfo[player][2] in [r for r in AllRoles if Alignments[r] == "G"]:
                    alignment = "Good"
                elif PlayerInfo[player][2] in [r for r in AllRoles if Alignments[r] == "E"]:
                    alignment = "Evil"
                elif PlayerInfo[player][2] in [r for r in AllRoles if Alignments[r] == "N"]:
                    alignment = "Neutral"
                else:
                    await ctx.send("{} is not a role!".format(PlayerInfo[player][2]))
                PlayerInfo[player].append(alignment)
                PlayerInfo[player].append("Alive")
                if modifier == True:
                    mod = " {}".format(PlayerInfo[player][3][0])
                else:
                    mod = ""
                if PlayerInfo[player][4] == "Good" or PlayerInfo[player][4] == "Neutral":
                    a = " {}".format(PlayerInfo[player][4])
                elif PlayerInfo[player][4] == "Evil":
                    a = "n {}".format(PlayerInfo[player][4])
                output = "You are a{} {}{}!".format(a,PlayerInfo[player][2],mod)
                await PlayerInfo[player][1].send(output)
                await ctx.invoke(self.client.get_command(descCommands[PlayerInfo[player][2]]), where=PlayerInfo[player][1])
                if modifier == True:
                    await ctx.invoke(self.client.get_command(descCommands[PlayerInfo[player][3][0]]), where=PlayerInfo[player][1])
            rolereport = ""
            for p in sorted(list(PlayerInfo)):
                mod = ""
                for m in PlayerInfo[p][3]:
                    mod = "{} {}".format(mod,m)
                rolereport = ("{}{} - {} {}{}\n".format(rolereport,p.title(),PlayerInfo[p][4],PlayerInfo[p][2],mod))
            await notes_channel.send(rolereport)
        else:
            await ctx.send("You need to be a GM to use this command!")
            
    @commands.command(pass_context=True)
    async def gamestatus(self, ctx):
        global PlayerInfo
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            output = "```"
            for p in PlayerInfo:
                mod = ""
                for m in PlayerInfo[p][3]:
                    mod = "{} {}".format(mod,m)
                output = "{}\n{} - {} {}{} - {}".format(output,p.upper(),PlayerInfo[p][4],PlayerInfo[p][2],mod,PlayerInfo[p][5])
            output = "{}```".format(output)
            embed = discord.Embed(title="Game Status",description=output)
            await ctx.send(embed=embed)
        else:
            await ctx.send("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def daytimer(self, ctx, *, message: str):
        global Day
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            game_channel = self.client.get_channel(392995027909083137)
            voting_channel = self.client.get_channel(393470084217176075)
            message = message.split("; ")
            n = message[0]
            secs = int(message[1])
            anno = message[2].split("/")
            a = ""
            for x in anno:
                a = "{}\n{}".format(a,x)
            await game_channel.send("DAY {}\n{}".format(n, a))
            player = discord.utils.get(ctx.message.guild.roles, name="Player")
            perms = discord.PermissionOverwrite()
            perms.read_messages = True
            perms.send_messages = False
            perms.add_reactions = True      
            await voting_channel.set_permissions(player, overwrite=perms)
            perms = discord.PermissionOverwrite()
            perms.send_messages = True
            perms.add_reactions = True
            await game_channel.set_permissions(player, overwrite=perms)
            for chan in [c for c in ctx.message.guild.channels if c.name == "seance"]:
                await chan.delete()
            Day = True
            for i in range(0, secs):
                await asyncio.sleep(1)
                if (secs-i) % 300 == 0:
                    await game_channel.send("{} minutes remaining until Night!".format(int((secs-i)/60)))
                if (secs-i) == 180:
                    await game_channel.send("3 minutes remaining until Night!")
                if (secs-i) == 120:
                    await game_channel.send("2 minutes remaining until Night!")
                if (secs-i) == 60:
                    await game_channel.send("1 minute remaining until Night!")
                if (secs-i) == 30:
                    await game_channel.send("30 seconds remaining until Night!")
                if (secs-i) == 10:
                    await game_channel.send("10 seconds remaining until Night!")
                if Day == False:
                    break
            Day = False
            await game_channel.send("NIGHT {}".format(n))
            perms = discord.PermissionOverwrite()
            perms.read_messages = True
            perms.send_messages = False
            perms.add_reactions = False
            await voting_channel.set_permissions(player, overwrite=perms)
            perms = discord.PermissionOverwrite()
            perms.send_messages = False
            perms.add_reactions = True
            await game_channel.set_permissions(player, overwrite=perms)
        else:
            await ctx.send("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def playervote(self, ctx, s=900):
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            voting_channel = self.client.get_channel(393470084217176075)
            options = ""
            role = discord.utils.get(ctx.message.guild.roles, name="Player")
            players = [p.nick for p in ctx.message.guild.members if role in p.roles and p.nick != None]
            for name in [p.name for p in ctx.message.guild.members if role in p.roles and p.nick == None]:
                players.append(name)
            n = round(len([p.nick for p in ctx.message.guild.members if role in p.roles])/2)
            voted = await ctx.invoke(self.client.get_command("vote"),message=players,where=voting_channel,needed=n,time=s)
            return voted
        else:
            await ctx.send("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def choosedeputy(self, ctx, *, chosen: discord.Member):
        global NeedDeputy
        if NeedDeputy == True:
            if "Mayor" in [y.name for y in ctx.message.author.roles]:
                await ctx.invoke(self.client.get_command("deputy"),player=chosen,invoked=True)
                NeedDeputy = False
                await ctx.send("{} has been chosen as Deputy!".format(chosen.mention))
            else:
                await ctx.send("You need to be the Mayor to use this command!")
        else:
            await ctx.send("A Deputy cannot be chosen at this time.")

    @commands.command(pass_context=True)
    async def night(self, ctx):
        global Day
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            if Day == False:
                await ctx.send("It is either already night or there is no game happening.")
            else:
                Day = False
        else:
            await ctx.send("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def kill(self, ctx, player: discord.Member):
        player_role = discord.utils.get(ctx.message.guild.roles, name="Player")
        dead_role = discord.utils.get(ctx.message.guild.roles, name="Dead")
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            if "Player" in [y.name for y in player.roles]:
                await player.add_roles(dead_role)
                await asyncio.sleep(1)
                await player.remove_roles(player_role)
                if "Mayor" in [y.name for y in player.roles]:
                    await asyncio.sleep(1)
                    mayor_role = discord.utils.get(ctx.message.guild.roles, name="Mayor")
                    await player.remove_roles(mayor_role)
                if "Deputy" in [y.name for y in player.roles]:
                    await asyncio.sleep(1)
                    deputy_role = discord.utils.get(ctx.message.guild.roles, name="Deputy")
                    await player.remove_roles(deputy_role)
                await asyncio.sleep(1)
                await ctx.invoke(self.client.get_command("lockjaw"),user=player,status="f")
                await ctx.invoke(self.client.get_command("medium"),user=player,status="f")
            else:
                await ctx.send("User is either already dead or not in the game.")
        else:
            await ctx.send("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def revive(self, ctx, player: discord.Member):
        player_role = discord.utils.get(ctx.message.guild.roles, name="Player")
        dead_role = discord.utils.get(ctx.message.guild.roles, name="Dead")
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            if "Dead" in [y.name for y in player.roles]:
                await player.add_roles(player_role)
                await asyncio.sleep(1)
                await player.remove_roles(dead_role)
                await asyncio.sleep(1)
            else:
                await ctx.send("User is either already alive or not in the game.")
        else:
            await ctx.send("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def mayor(self, ctx, player: discord.Member):
        player_role = discord.utils.get(ctx.message.guild.roles, name="Player")
        mayor_role = discord.utils.get(ctx.message.guild.roles, name="Mayor")
        deputy_role = discord.utils.get(ctx.message.guild.roles, name="Deputy")
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            if "Player" in [y.name for y in player.roles]:
                if mayor_role not in [x for y in [p.roles for p in ctx.message.guild.members if player_role in p.roles] for x in y]:
                    await player.add_roles(mayor_role)
                    if deputy_role in [y for y in player.roles]:
                        await player.remove_roles(deputy_role)
                else:
                    await ctx.send("There is already a Mayor in this game.")
            else:
                await ctx.send("User is either dead or not in the game.")
        else:
            await ctx.send("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def deputy(self, ctx, player: discord.Member, invoked=False):
        player_role = discord.utils.get(ctx.message.guild.roles, name="Player")
        mayor_role = discord.utils.get(ctx.message.guild.roles, name="Mayor")
        deputy_role = discord.utils.get(ctx.message.guild.roles, name="Deputy")
        if "Game Master" in [y.name for y in ctx.message.author.roles] or invoked == True:
            if "Player" in [y.name for y in player.roles]:
                if deputy_role not in [x for y in [p.roles for p in ctx.message.guild.members if player_role in p.roles] for x in y]:
                    if mayor_role not in [y for y in player.roles]:
                        await player.add_roles(deputy_role)
                    else:
                        await ctx.send("User is the Mayor.")
                else:
                    await ctx.send("There is already a Deputy in this game.")
            else:
                await ctx.send("User is either dead or not in the game.")
        else:
            await ctx.send("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def wolves(self, ctx):
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            guild = ctx.message.guild
            wolf_perms = discord.PermissionOverwrite(read_messages=True)
            wolves_channel = discord.utils.get(guild.channels,name="wolves")
            if wolves_channel == None:
                everyone_perms = discord.PermissionOverwrite(read_messages=False)
                overwrites = {guild.default_role : everyone_perms, discord.utils.get(guild.roles, name="Game Master") : wolf_perms}
                category = discord.utils.get(guild.categories, name="priv channels")
                wolves_channel = await guild.create_text_channel("wolves", overwrites=overwrites, category=category)
            players = ctx.message.mentions
            for p in players:
                await wolves_channel.set_permissions(p, overwrite=wolf_perms)
            return wolves_channel
        else:
            await ctx.send("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def twin(self, ctx, p1: discord.Member, p2: discord.Member):
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            guild = ctx.message.guild
            everyone_perms = discord.PermissionOverwrite(read_messages=False)
            twin_perms = discord.PermissionOverwrite(read_messages=True)
            overwrites = {guild.default_role : everyone_perms, discord.utils.get(guild.roles, name="Game Master") : twin_perms, p1 : twin_perms, p2: twin_perms}
            category = discord.utils.get(guild.categories, name="priv channels")
            chan = await guild.create_text_channel("twins", overwrites=overwrites, category=category)
            return chan
        else:
            await ctx.send("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def tardis(self, ctx, timelord: discord.Member, companion: discord.Member):
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            guild = ctx.message.guild
            everyone_perms = discord.PermissionOverwrite(read_messages=False)
            crew_perms = discord.PermissionOverwrite(read_messages=True)
            tardises = [c for c in guild.channels if c.name=="tardis"]
            if [c for c in tardises if c.permissions_for(timelord).read_messages == True] == []:
                overwrites = {guild.default_role : everyone_perms, discord.utils.get(guild.roles, name="Game Master") : crew_perms, timelord : crew_perms}
                category = discord.utils.get(guild.categories, name="priv channels")
                tardis_channel = await guild.create_text_channel("tardis", overwrites=overwrites, category=category)
            else:
                tardis_channel = [c for c in tardises if c.permissions_for(timelord).read_messages == True][0]
            if tardis_channel.permissions_for(companion).read_messages == False:
                await tardis_channel.set_permissions(companion, overwrite=crew_perms)
            else:
                await tardis_channel.set_permissions(companion, overwrite=None)
            return tardis_channel
        else:
            await ctx.send("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def coven(self, ctx, p=""):
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            guild = ctx.message.guild
            everyone_perms = discord.PermissionOverwrite(read_messages=False)
            fate_perms = discord.PermissionOverwrite(read_messages=True)
            coven_channel = discord.utils.get(guild.channels,name="coven")
            if coven_channel == None:
                overwrites = {guild.default_role : everyone_perms, discord.utils.get(guild.roles, name="Game Master") : fate_perms}
                category = discord.utils.get(guild.categories, name="priv channels")
                coven_channel = await guild.create_text_channel("coven", overwrites=overwrites, category=category)
            players = ctx.message.mentions
            if isinstance(p, list):
                players = p
            for p in players:
                await coven_channel.set_permissions(p, overwrite=fate_perms)
            return coven_channel
        else:
            await ctx.send("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def seance(self, ctx, medium: discord.Member, target: discord.Member):
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            guild = ctx.message.guild
            everyone_perms = discord.PermissionOverwrite(read_messages=False)
            seance_perms = discord.PermissionOverwrite(read_messages=True)
            overwrites = {guild.default_role : everyone_perms, discord.utils.get(guild.roles, name="Game Master") : seance_perms, medium : seance_perms, target : seance_perms}
            category = discord.utils.get(guild.categories, name="priv channels")
            chan = await guild.create_text_channel("seance", overwrites=overwrites, category=category)
            return chan
        else:
            await ctx.send("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def vampires(self, ctx):
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            guild = ctx.message.guild
            vampire_perms = discord.PermissionOverwrite(read_messages=True)
            vampires_channel = discord.utils.get(guild.channels,name="vampires")
            if vampires_channel == None:
                everyone_perms = discord.PermissionOverwrite(read_messages=False)
                overwrites = {guild.default_role : everyone_perms, discord.utils.get(guild.roles, name="Game Master") : vampire_perms}
                category = discord.utils.get(guild.categories, name="priv channels")
                vampires_channel = await guild.create_text_channel("vampires", overwrites=overwrites, category=category)
            players = ctx.message.mentions
            for p in players:
                await vampires_channel.set_permissions(p, overwrite=vampire_perms)
            return vampires_channel
        else:
            await ctx.send("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def lockjaw(self, ctx, user: discord.Member, status="t"):
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            game_channel = self.client.get_channel(392995027909083137)
            voting_channel = self.client.get_channel(393470084217176075)
            status = status.lower()
            if status == "t" or status == "true":
                gperms = discord.PermissionOverwrite()
                vperms = discord.PermissionOverwrite()
                gperms.send_messages = False
                gperms.add_reactions = False
                vperms.add_reactions = False
                await game_channel.set_permissions(user, overwrite=gperms)
                await voting_channel.set_permissions(user, overwrite=vperms)
            elif status == "f" or status == "false":
                await game_channel.set_permissions(user, overwrite=None)
                await voting_channel.set_permissions(user, overwrite=None)
        else:
            await ctx.send("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def medium(self, ctx, user: discord.Member, status="t"):
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            dead_channel = self.client.get_channel(392995124423950344)
            status = status.lower()
            if status == "t" or status == "true":
                perms = discord.PermissionOverwrite()
                perms.read_messages = True
                await dead_channel.set_permissions(user, overwrite=perms)
            elif status == "f" or status == "false":
                await dead_channel.set_permissions(user, overwrite=None)
        else:
            await ctx.send("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def sonic(self, ctx, *, roles=""):
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            if roles == "":
                await ctx.send("""Usage of command <w.sonic>:
```md
<w.sonic (comma-seperated list of all roles in game)>

Example: <w.sonic Direwolf, Werewolf, Seer, Jailor>
Output: 'Direwolf, Drunk, Jailor, Shifter'```""")
                return None
            roles = roles.split(", ")
            random.shuffle(roles)
            sonic = []
            All = [r for r in AllRoles if r not in [x.title() for x in roles]]
            for i in range(0, round(len(roles)/2)):
                sonic.append(roles[i])
            for i in range(0, round((len(roles)-0.5)/2)):
                sonic.append(random.choice(All))
            sonic = sorted(sonic)
            output = sonic[0]
            for i in range(1,len(sonic)):
                output = "{}, {}".format(output,sonic[i])
            await ctx.send(output)
            return sonic

def setup(client):
    client.add_cog(GameCommands(client))
