import discord
from discord.ext import commands



class Help():

    def __init__(self, client):
        self.client = client
    
    @commands.command(pass_context=True)
    async def help(ctx):
        await ctx.send("""Hi there! My name is **Wolfie**! I'm the (WIP) bot for the **Werewolf Server**. This is what I can do:
```md
<w.help> - Shows this message.
<w.gm_help> - Shows commands available for GMs only.
<w.gamerules> - Provides a link to the rules for playing the game.
<w.scoreboard> - Provides a link to the scoreboard and tracker.
<w.roleguide> - Provides a link to the role creation guide.
<w.library> - Provides a list of document links.

<w.stats (@user)> - Gives scoreboard statistics for mentioned user, or self if no user is given.

<w.rolelist> - Provides a list of roles in the game, plus commands to see more information.
<w.listroles (space seperated list of tags as parameters)> - Lists all roles that have all the tags provided.
<w.achieve (role)> - Lists nonstandard ways of gaining given role.
<w.icon (role)> - Displays icon for given role.

<w.register (name)> - Create a private channel for yourself.
<w.generatelist> - Shows commands to generate rolelists.
<w.vote (options to vote between seperated by commas)> - Displays a list of specified options to vote on.
<w.advancedvote (options to vote between seperated by commas; time; needed)> - w.vote, but better.

<w.randomchoice (comma seperated list of options)> - Randomly chooses from given options.
<w.randomrole (space seperated list of tags as parameters)> - Randomly gives a role that has all the tags provided.
<w.flip (number of coins to flip)> - Flips a specified amount of coins.
<w.roll (#d#)> - Rolls specified dice.
<w.magic8ball> - Ask Wolfie a question!

<w.score (wins:loses)> - Displays score for given statistics.```""")

    @commands.command(pass_context=True)
    async def gm_help(ctx):
        await ctx.send("""```md
<w.setplayers (mentions)> - Sets all users mentioned as Player. If any mentioned are already Player, removes role.
<w.setprivs (@player: name, etc)> - Creates priv channels for all players using name as start of channel name.
<w.giveroles (player: role [(modifier)], etc)> - Gives players listed the applied role.
<w.gamestatus> - Returns all players in the current game with information about them. 

<w.daytimer (n; seconds; announcements)> - Sets a timer for the day, unlocks #game at start, locks #game when it ends. Seperate lines in announcements with /.
<w.playervote ([time])> - Creates a vote in #voting for the players. Time is 900 seconds if not given.
<w.night> - Ends day.

<w.mayor (@player)> - Sets given player as Mayor.
<w.deputy (@player)> - Sets given player as Deputy.
<w.kill (mentions)> - Kills the mentioned players.
<w.revive (mentions)> - Revives the mentioned players.```""")
        await ctx.send("""```md
<w.wolves (mentions)> - Creates #wolves if it does not exist, and gives mentioned players permissions for it.
<w.twin (@twin1 @twin2)> - Creates #twins channel for specified players.
<w.tardis (@timelord @companion)> - Creates/fetches #tardis channel for timelord, if companion is not companion gives them permissions, otherwise removes permissions.
<w.coven (mentions)> - Creates #coven if it does not exist, and gives mentioned players permissions for it.
<w.vampires (mentions)> - Creates #wolves if it does not exist, and gives mentioned players permissions for it.
<w.seance (@medium @target)> - Creates a seance between medium and target; this is removed at the start of a day.

<w.lockjaw (@player boolean)> - If boolean true, lockjaws player; if false, unlockjaws player.
<w.medium (@player boolean)> - If boolean true, gives player perms to see #dead; if false, removes perms.
<w.sonic (comma-seperated list of all roles in game)> - Returns a Sonic result for roles provided.

<w.endgame> - Ends game, removing all game roles and permissions from all members of guild and deleting all priv channels.```""")

@commands.command(pass_context=True)
async def gamerules(ctx):
    embed=discord.Embed(description="""This link details the rules for playing Werewolf.
If you have any questions or suggestions for improvement on the rules, contact Army with them. They'll be happy to help!
(If that doesn't work, here's the link: https://bit.ly/werewolf-gamerules)""")
    embed.set_author(name="Werewolf Party Game Rules", url='https://bit.ly/werewolf-gamerules', icon_url='https://i.imgur.com/hYA0Uqu.png')
    await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def scoreboard(ctx):
        embed=discord.Embed(description="""This spreadsheet includes the scoreboards and a game tracker.
(If that doesn't work, here's the link: https://bit.ly/werewolf-scoreboard)""")
        embed.set_author(name="Werewolf Scoreboard/Tracker", url='https://bit.ly/werewolf-scoreboard', icon_url='https://i.imgur.com/hYA0Uqu.png')
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def roleguide(ctx):
        embed=discord.Embed(description="""This link details design principles for creating and suggesting roles.
(If that doesn't work, here's the link: https://bit.ly/werewolf-roleguide)""")
        embed.set_author(name="Army's Guide to Role Creation", url='https://bit.ly/werewolf-roleguide', icon_url='https://i.imgur.com/hYA0Uqu.png')
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def library(ctx):
        await ctx.send(embed=(discord.Embed(description="""- Game Rules: https://bit.ly/werewolf-gamerules
- Scoreboard/Tracker: https://bit.ly/werewolf-scoreboard
- Role Creation Guide: https://bit.ly/werewolf-roleguide""")))


def setup(client):
    client.add_cog(Help(client))