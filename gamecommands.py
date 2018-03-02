import discord
from discord.ext import commands
import asyncio
from wolfiebot import *
from config import *

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
            player_role = discord.utils.get(ctx.message.server.roles, name="Player")
            players = ctx.message.mentions
            for p in players:
                if "Player" not in [y.name for y in p.roles]:
                    await self.client.add_roles(p, player_role)
        else:
            await self.client.say("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def endgame(self, ctx):
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            player_role = discord.utils.get(ctx.message.server.roles, name="Player")
            dead_role = discord.utils.get(ctx.message.server.roles, name="Dead")
            mayor_role = discord.utils.get(ctx.message.server.roles, name="Mayor")
            deputy_role = discord.utils.get(ctx.message.server.roles, name="Deputy")
            for user in [m for m in ctx.message.server.members if player_role in m.roles]:
                await self.client.remove_roles(user,player_role)
            for user in [m for m in ctx.message.server.members if dead_role in m.roles]:
                await self.client.remove_roles(user,dead_role)
            for user in [m for m in ctx.message.server.members if mayor_role in m.roles]:
                await self.client.remove_roles(user,mayor_role)
            for user in [m for m in ctx.message.server.members if deputy_role in m.roles]:
                await self.client.remove_roles(user,deputy_role)
            for c in [c for c in ctx.message.server.channels]:
                if c.name == "wolves":
                    await self.client.delete_channel(c)
                elif c.name == "coven":
                    await self.client.delete_channel(c)
                elif c.name == "twins":
                    await self.client.delete_channel(c)
                elif c.name == "tardis":
                    await self.client.delete_channel(c)
                elif c.name == "seance":
                    await self.client.delete_channel(c)
            for user in ctx.message.server.members:
                await ctx.invoke(self.client.get_command("lockjaw"),user=user,status="f")
                await ctx.invoke(self.client.get_command("medium"),user=user,status="f")
            await self.client.say("Game ended successfully!")
        else:
            await self.client.say("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def rungame(self, ctx, *, message: str):
        global PlayerInfo, NeedDeputy
        await self.client.say("This command is in development.")
        return
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            game_channel = self.client.get_channel("392995027909083137")
            voting_channel = self.client.get_channel("393470084217176075")
            notes_channel = self.client.get_channel("393476547954212874")
            dead_channel = self.client.get_channel("392995124423950344")
            player_role = discord.utils.get(ctx.message.server.roles, name="Player")
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
            n = 0
            while True:
                n = n+1
                report = "{}; 900; {}".format(n,report)
                await ctx.invoke(self.client.get_command("daytimer"),message=report)
                mayor_role = discord.utils.get(ctx.message.server.roles, name="Mayor")
                deputy_role = discord.utils.get(ctx.message.server.roles, name="Deputy")
                if mayor_role not in [x for y in [p.roles for p in ctx.message.server.members if player_role in p.roles] for x in y]:
                    if deputy_role in [x for y in [p.roles for p in ctx.message.server.members if player_role in p.roles] for x in y]:
                        deputy = [p for p in ctx.message.server.members if deputy_role in p.roles][0]
                        await self.client.add_roles(deputy, mayor_role)
                        await self.client.remove_roles(deputy, deputy_role)
                        await self.client.send_message(game_channel,"{} has become Mayor! Choose your deputy with *w.choosedeputy @player*.".format(deputy.mention))
                        NeedDeputy = True
                        while NeedDeputy == True:
                            await asyncio.sleep(5)
                    else:
                        await self.client.send_message(voting_channel,"MAYORAL ELECTION")
                        mayor = await ctx.invoke(self.client.get_command("playervote"))
                        elected = [p for p in ctx.message.server.members if p.nick == mayor][0]
                        await self.client.add_roles(elected, mayor_role)
                        await self.client.send_message(game_channel,"{} has been elected as Mayor! Choose your deputy with *w.choosedeputy @player*.".format(elected.mention))
                        NeedDeputy = True
                        while NeedDeputy == True:
                            await asyncio.sleep(5)
                if n != 1:
                    await self.client.send_message(voting_channel,"LYNCH")
                    lynched = await ctx.invoke(self.client.get_command("playervote"))
                    lynched = [p for p in ctx.message.server.members if p.nick == lynched][0]
                    if True: # if not saved
                        await ctx.invoke(self.client.get_command("kill"),player=lynched.mention)
                        await self.client.send_message(game_channel,"{} has been voted to be Lynched!\n\nThey were a {} {}!".format(lynched.mention))
                        # message declaring lynched, role
                    else: # if saved
                        await self.client.send_message(game_channel,"{} has been voted to be Lynched!\n\nBut they were saved!".format(lynched.mention))
                        # remove used up save
                # keep working on this
        else:
            await self.client.say("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def giveroles(self, ctx, *, message: str):
        global PlayerInfo
        notes_channel = self.client.get_channel("393476547954212874")
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            message = message.split(", ")
            x = []
            for m in message:
                m = m.split(": ")
                m[0] = m[0].lower()
                if "(" in m[1]:
                    y = m[1].split(" (")
                    m[1] = y[0]
                    modifier = y[1]
                    m.append(modifier[:-1])
                else:
                    m.append("")
                chan = discord.utils.get(ctx.message.server.channels, name="{}-priv".format(m[0]))
                m.append(chan)
                gm_role = discord.utils.get(ctx.message.server.roles, name="Game Master")
                bot_role = discord.utils.get(ctx.message.server.roles, name="Bots")
                user = [u for u in ctx.message.server.members if chan.permissions_for(u).read_messages == True and gm_role not in u.roles and bot_role not in u.roles][0]
                m.append(user)
                x.append(m)
            PlayerInfo = {m[0] : [m[4], m[3], m[1], [m[2]]] for m in x}
            for player in PlayerInfo:
                if PlayerInfo[player][3] == [""]:
                    PlayerInfo[player][3] = []
                    modifier = False
                else:
                    modifier = True
                if PlayerInfo[player][2] in GoodRoles:
                    alignment = "Good"
                elif PlayerInfo[player][2] in EvilRoles:
                    alignment = "Evil"
                elif PlayerInfo[player][2] in NeutralRoles:
                    alignment = "Neutral"
                else:
                    await self.client.say("{} is not a role!".format(PlayerInfo[player][2]))
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
                await self.client.send_message(PlayerInfo[player][1],output)
                await ctx.invoke(self.client.get_command(descCommands[PlayerInfo[player][2]]), where=PlayerInfo[player][1])
                if modifier == True:
                    await ctx.invoke(self.client.get_command(descCommands[PlayerInfo[player][3][0]]), where=PlayerInfo[player][1])
            rolereport = ""
            for p in PlayerInfo:
                mod = ""
                for m in PlayerInfo[p][3]:
                    mod = "{} {}".format(mod,m)
                rolereport = ("{}{} - {} {}{}\n".format(rolereport,p.title(),PlayerInfo[p][4],PlayerInfo[p][2],mod))
            await self.client.send_message(notes_channel,rolereport)
        else:
            await self.client.say("You need to be a GM to use this command!")
            
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
            await self.client.say(embed=embed)
        else:
            await self.client.say("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def daytimer(self, ctx, *, message: str):
        global Day
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            game_channel = self.client.get_channel("392995027909083137")
            voting_channel = self.client.get_channel("393470084217176075")
            message = message.split("; ")
            n = message[0]
            secs = int(message[1])
            anno = message[2].split("/")
            a = ""
            for x in anno:
                a = "{}\n{}".format(a,x)
            await self.client.send_message(game_channel,"DAY {}\n{}".format(n, a))
            perms = discord.PermissionOverwrite()
            perms.read_messages = True
            perms.send_messages = False
            perms.add_reactions = True
            player = discord.utils.get(ctx.message.server.roles, name="Player")
            await self.client.edit_channel_permissions(voting_channel, player, perms)
            perms = discord.PermissionOverwrite()
            perms.send_messages = True
            perms.add_reactions = True
            player = discord.utils.get(ctx.message.server.roles, name="Player")
            await self.client.edit_channel_permissions(game_channel, player, perms)
            for chan in [c for c in ctx.message.server.channels if c.name == "seance"]:
                await self.client.delete_channel(chan)
            Day = True
            for i in range(0, secs):
                await asyncio.sleep(1)
                if (secs-i) % 300 == 0:
                    await self.client.send_message(game_channel,"{} minutes remaining until Night!".format(int((secs-i)/60)))
                if (secs-i) == 180:
                    await self.client.send_message(game_channel,"3 minutes remaining until Night!")
                if (secs-i) == 120:
                    await self.client.send_message(game_channel,"2 minutes remaining until Night!")
                if (secs-i) == 60:
                    await self.client.send_message(game_channel,"1 minute remaining until Night!")
                if (secs-i) == 30:
                    await self.client.send_message(game_channel,"30 seconds remaining until Night!")
                if (secs-i) <= 10 and (secs-i) != 1:
                    await self.client.send_message(game_channel,"{} seconds remaining until Night!".format(secs-i))
                if (secs-i) == 1:
                    await self.client.send_message(game_channel,"1 second remaining until Night!")
                if Day == False:
                    break
            Day = False
            await self.client.send_message(game_channel,"NIGHT {}".format(n))
            perms = discord.PermissionOverwrite()
            perms.read_messages = True
            perms.send_messages = False
            perms.add_reactions = False
            player = discord.utils.get(ctx.message.server.roles, name="Player")
            await self.client.edit_channel_permissions(voting_channel, player, perms)
            perms = discord.PermissionOverwrite()
            perms.send_messages = False
            perms.add_reactions = True
            player = discord.utils.get(ctx.message.server.roles, name="Player")
            await self.client.edit_channel_permissions(game_channel, player, perms)
        else:
            await self.client.say("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def playervote(self, ctx):
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            voting_channel = self.client.get_channel("393470084217176075")
            options = ""
            role = discord.utils.get(ctx.message.server.roles, name="Player")
            players = [p.nick for p in ctx.message.server.members if role in p.roles and p.nick != None]
            for name in [p.name for p in ctx.message.server.members if role in p.roles and p.nick == None]:
                players.append(name)
            players = sorted(players)
            for p in players:
                if p == players[0]:
                    options = p
                else:
                    options = "{}, {}".format(options,p)
            n = len([p.nick for p in ctx.message.server.members if role in p.roles])/2+1
            voted = await ctx.invoke(self.client.get_command("vote"),message=options,where=voting_channel,needed=n)
            return voted
        else:
            await self.client.say("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def choosedeputy(self, ctx, *, chosen: discord.Member):
        global NeedDeputy
        if NeedDeputy == True:
            if "Mayor" in [y.name for y in ctx.message.author.roles]:
                await ctx.invoke(self.client.get_command("deputy"),player=chosen,invoked=True)
                NeedDeputy = False
                await self.client.say("{} has been chosen as Deputy!".format(chosen.mention))
            else:
                await self.client.say("You need to be the Mayor to use this command!")
        else:
            await self.client.say("A Deputy cannot be chosen at this time.")

    @commands.command(pass_context=True)
    async def night(self, ctx):
        global Day
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            if Day == False:
                await self.client.say("It is either already night or there is no game happening.")
            else:
                Day = False
        else:
            await self.client.say("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def kill(self, ctx, player: discord.Member):
        player_role = discord.utils.get(ctx.message.server.roles, name="Player")
        dead_role = discord.utils.get(ctx.message.server.roles, name="Dead")
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            if "Player" in [y.name for y in player.roles]:
                await self.client.add_roles(player, dead_role)
                await self.client.remove_roles(player, player_role)
                if "Mayor" in [y.name for y in player.roles]:
                    mayor_role = discord.utils.get(ctx.message.server.roles, name="Mayor")
                    await self.client.remove_roles(player, mayor_role)
                if "Deputy" in [y.name for y in player.roles]:
                    deputy_role = discord.utils.get(ctx.message.server.roles, name="Deputy")
                    await self.client.remove_roles(player, deputy_role)
                await ctx.invoke(self.client.get_command("lockjaw"),user=player,status="f")
                await ctx.invoke(self.client.get_command("medium"),user=player,status="f")
            else:
                await self.client.say("User is either already dead or not in the game.")
        else:
            await self.client.say("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def mayor(self, ctx, player: discord.Member):
        mayor_role = discord.utils.get(ctx.message.server.roles, name="Mayor")
        deputy_role = discord.utils.get(ctx.message.server.roles, name="Deputy")
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            if "Player" in [y.name for y in player.roles]:
                if mayor_role not in [x for y in [p.roles for p in ctx.message.server.members if player_role in p.roles] for x in y]:
                    await self.client.add_roles(player, mayor_role)
                    if deputy_role in [y for y in player.roles]:
                        await self.client.remove_roles(player, deputy_role)
                else:
                    await self.client.say("There is already a Mayor in this game.")
            else:
                await self.client.say("User is either dead or not in the game.")
        else:
            await self.client.say("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def deputy(self, ctx, player: discord.Member, invoked=False):
        mayor_role = discord.utils.get(ctx.message.server.roles, name="Mayor")
        deputy_role = discord.utils.get(ctx.message.server.roles, name="Deputy")
        if "Game Master" in [y.name for y in ctx.message.author.roles] or invoked == True:
            if "Player" in [y.name for y in player.roles]:
                if deputy_role not in [x for y in [p.roles for p in ctx.message.server.members if player_role in p.roles] for x in y]:
                    if mayor_role not in [y for y in player.roles]:
                        await self.client.add_roles(player, deputy_role)
                    else:
                        await self.client.say("User is the Mayor.")
                else:
                    await self.client.say("There is already a Deputy in this game.")
            else:
                await self.client.say("User is either dead or not in the game.")
        else:
            await self.client.say("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def wolves(self, ctx):
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            server = ctx.message.server
            everyone_perms = discord.PermissionOverwrite(read_messages=False)
            wolf_perms = discord.PermissionOverwrite(read_messages=True)
            everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
            gm = discord.ChannelPermissions(target=discord.utils.get(server.roles, name="Game Master"),overwrite=wolf_perms)
            wolves_channel = discord.utils.get(server.channels,name="wolves")
            if wolves_channel == None:
                wolves_channel = await self.client.create_channel(server, "wolves", everyone, gm)
            players = ctx.message.mentions
            for p in players:
                await self.client.edit_channel_permissions(wolves_channel, p, wolf_perms)
        else:
            await client.say("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def twin(self, ctx, p1: discord.Member, p2: discord.Member):
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            server = ctx.message.server
            everyone_perms = discord.PermissionOverwrite(read_messages=False)
            twin_perms = discord.PermissionOverwrite(read_messages=True)
            everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
            gm = discord.ChannelPermissions(target=discord.utils.get(server.roles, name="Game Master"),overwrite=twin_perms)
            p1 = discord.ChannelPermissions(target=p1,overwrite=twin_perms)
            p2 = discord.ChannelPermissions(target=p2,overwrite=twin_perms)
            await self.client.create_channel(server, "twins", everyone, gm, p1, p2)
        else:
            await client.say("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def tardis(self, ctx, timelord: discord.Member, companion: discord.Member):
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            server = ctx.message.server
            everyone_perms = discord.PermissionOverwrite(read_messages=False)
            crew_perms = discord.PermissionOverwrite(read_messages=True)
            everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
            gm = discord.ChannelPermissions(target=discord.utils.get(server.roles, name="Game Master"),overwrite=crew_perms)
            tardises = [c for c in server.channels if c.name=="tardis"]
            if tardises == []:
                everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
                gm = discord.ChannelPermissions(target=discord.utils.get(server.roles, name="Game Master"),overwrite=crew_perms)
                tl = discord.ChannelPermissions(target=timelord,overwrite=crew_perms)
                tardis_channel = await self.client.create_channel(server, "tardis", everyone, gm, tl)
            else:
                tardis_channel = [c for c in tardises if c.permissions_for(timelord).read_messages == True][0]
            if tardis_channel.permissions_for(companion).read_messages == False:
                await self.client.edit_channel_permissions(tardis_channel, companion, crew_perms)
            else:
                await self.client.delete_channel_permissions(tardis_channel, companion)
        else:
            await client.say("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def coven(self, ctx, p=""):
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            server = ctx.message.server
            everyone_perms = discord.PermissionOverwrite(read_messages=False)
            fate_perms = discord.PermissionOverwrite(read_messages=True)
            everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
            gm = discord.ChannelPermissions(target=discord.utils.get(server.roles, name="Game Master"),overwrite=fate_perms)
            coven_channel = discord.utils.get(server.channels,name="coven")
            if coven_channel == None:
                coven_channel = await self.client.create_channel(server, "coven", everyone, gm)
            players = ctx.message.mentions
            if isinstance(p, list):
                players = p
            for p in players:
                await self.client.edit_channel_permissions(coven_channel, p, fate_perms)
        else:
            await client.say("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def seance(self, ctx, medium: discord.Member, target: discord.Member):
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            server = ctx.message.server
            everyone_perms = discord.PermissionOverwrite(read_messages=False)
            seance_perms = discord.PermissionOverwrite(read_messages=True)
            everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
            gm = discord.ChannelPermissions(target=discord.utils.get(server.roles, name="Game Master"),overwrite=seance_perms)
            seance_channel = await self.client.create_channel(server, "seance", everyone, gm)
            players = [medium, target]
            for p in players:
                await self.client.edit_channel_permissions(seance_channel, p, seance_perms)
        else:
            await client.say("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def lockjaw(self, ctx, user: discord.Member, status: str):
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            game_channel = self.client.get_channel("392995027909083137")
            voting_channel = self.client.get_channel("393470084217176075")
            status = status.lower()
            if status == "t" or status == "true":
                gperms = discord.PermissionOverwrite()
                vperms = discord.PermissionOverwrite()
                gperms.send_messages = False
                gperms.add_reactions = False
                vperms.add_reactions = False
                await self.client.edit_channel_permissions(game_channel, user, gperms)
                await self.client.edit_channel_permissions(voting_channel, user, vperms)
            elif status == "f" or status == "false":
                await self.client.delete_channel_permissions(game_channel, user)
                await self.client.delete_channel_permissions(voting_channel, user)
        else:
            await client.say("You need to be a GM to use this command!")

    @commands.command(pass_context=True)
    async def medium(self, ctx, user: discord.Member, status: str):
        if "Game Master" in [y.name for y in ctx.message.author.roles]:
            dead_channel = self.client.get_channel("392995124423950344")
            status = status.lower()
            if status == "t" or status == "true":
                perms = discord.PermissionOverwrite()
                perms.read_messages = True
                await self.client.edit_channel_permissions(dead_channel, user, perms)
            elif status == "f" or status == "false":
                await self.client.delete_channel_permissions(dead_channel, user)
        else:
            await client.say("You need to be a GM to use this command!")

def setup(client):
    client.add_cog(GameCommands(client))
