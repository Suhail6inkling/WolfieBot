class GenerateList():


    def __init__(self, client):
        self.client = client

    @client.group(pass_context=True)
    async def generatelist(ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("Available Gamemodes to generate lists for: \n(Give Players and Roles as comma seperated lists)\n```md\nStandard - <w.generatelist standard [players]>\n\
Anonymous Register - <w.generatelist anons [players] : [roles]>\nDuality - <w.generatelist duality [players]>\nMoral Feud - <w.generatelist morals [players]>\n\
Truth & Claw - <w.generatelist tac [players]>```")

    @generatelist.command(pass_context=True)
    async def standard(ctx, *, message: str):
        Evil=[r for r in AllRoles if Alignments[r] == "E" if r not in AchievableRoles]
        for r in Evil:
            if r in AchievableRoles:
                Evil.remove(r)
        Evil.remove("Direwolf")
        Evil.remove("Werewolf")
        Good=[r for r in AllRoles if Alignments[r] == "G" if r not in AchievableRoles]
        for r in Good:
            if r in AchievableRoles:
                Good.remove(r)
        Good.remove("Priest")
        Neutral=[r for r in AllRoles if Alignments[r] == "N" if r not in AchievableRoles]
        Mod=[m for m in Modifiers if m not in AchievableModifiers]
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
                elif "Cultist Twin" in combined or "Priest Twin" in combined:
                    continue
                elif [i for i in ["Backstabber {}".format(m) for m in Modifiers] if i in combined] != []:
                    continue
                elif [i for i in ["{} Conduit".format(a) for a in AllRoles if a not in [r for r in AllRoles if Species[r] == "Human" and "K" in Categories[r]]] if i in combined] != []:
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

def setup(client):
    client.add_cog(GenerateList(client))