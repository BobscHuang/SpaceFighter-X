from tkinter import *
from time import *
from random import *
import sys
import time
root = Tk()
s = Canvas(root, width=1000, height=1000, background= "black")
s.pack()

######################################
##                                  ##
##          SpaceFighter X          ##
##           By: Bob Huang          ##
##    Last Edited: Jan 25, 2017     ##
##                                  ##
######################################

#Create Circle From Centre
def create_circle(x, y, radius, fill = "", outline = "black", width = 1):
    
    Name = s.create_oval(x - radius, y - radius, x + radius, y + radius, fill = fill, outline = outline, width = width)
    return Name

#Resets Enemy Location
def Fighter_Location_Reset(indexNum, Probability):
    
    FighterX[indexNum] = randint(0, 1000)
    FighterY[indexNum] = randint(-2000, -50)
    FighterSpeed[indexNum] = randint(3, 5)
    FighterFR[indexNum] = randint(int(enemyFireRate * 0.8), int(enemyFireRate * 1.2))

    if Probability < 2000:
        level = choice([1] * 10 + [2] * 1 + [3] * 0)

    elif Probability < 5000:
        level = choice([1] * 1 + [2] * 10 + [3] * 1)

    else:
        level = choice([1] * 1 + [2] * 2 + [3] * 10)


    if level == 1:
        Fighterimg[indexNum] = choice([greenFighterimg, greenFighter2img])
        FighterHP[indexNum] = 1 * (diffculty_Inc + int(score / 16000))
        FighterHPTotal[indexNum] = 1 * (diffculty_Inc + int(score / 16000))
        killScore[indexNum] = 50

    elif level == 2:
        Fighterimg[indexNum] = choice([yellowFighterimg, yellowFighter2img])
        FighterHP[indexNum] = 2 * (diffculty_Inc + int(score / 16000))
        FighterHPTotal[indexNum] = 2 * (diffculty_Inc + int(score / 16000))
        killScore[indexNum] = 80

    elif level == 3:
        Fighterimg[indexNum] = choice([redFighterimg, redFighter2img])
        FighterHP[indexNum] = 3 * (diffculty_Inc + int(score / 16000))
        FighterHPTotal[indexNum] = 3 * (diffculty_Inc + int(score / 16000))
        killScore[indexNum] = 130

    if Fighterimg[indexNum] == greenFighter2img or Fighterimg[indexNum] == yellowFighter2img or Fighterimg[indexNum] == redFighter2img:
        FighterType[indexNum] = "Double"

    else:
        FighterType[indexNum] = "Single"

#Diffculty Setting
def Diffculty(diffculty):
    global enemyFireRate, enemyProjectileSpeed, FighterNum, sethitPoints, diffculty_Inc, boss_Projectile_Num
    
    if diffculty == "NON":
        enemyFireRate = 300
        enemyProjectileSpeed = 3
        FighterNum = 4
        sethitPoints = 9
        diffculty_Inc = 1
        boss_Projectile_Num = 10
        
    elif diffculty == "EASY":
        enemyFireRate = 170
        enemyProjectileSpeed = 3
        FighterNum = 6
        sethitPoints = 7
        diffculty_Inc = 1
        boss_Projectile_Num = 20

    elif diffculty == "MEDIUM":
        enemyFireRate = 110
        enemyProjectileSpeed = 5
        FighterNum = 9
        sethitPoints = 5
        diffculty_Inc = 1.5
        boss_Projectile_Num = 40

    elif diffculty == "HARD":
        enemyFireRate = 50
        enemyProjectileSpeed = 7
        FighterNum = 13
        sethitPoints = 3
        diffculty_Inc = 2.5
        boss_Projectile_Num = 100

#Start Menu
def Start_Menu():
    global game_Start, start_Button, start_Button_Text, logo, inst_Button, inst_Button_Text, Exit_Button, Exit_Button_Text

    start_Button = s.create_rectangle(200, 500, 800, 600, fill = "red", outline = "white", width = 4)
    start_Button_Text = s.create_text(500, 550, text = "START", font = "Helvetica 60 bold", fill = "white")
    Exit_Button = s.create_rectangle(200, 800, 800, 900, fill = "red", outline = "white", width = 4)
    
    inst_Button = s.create_rectangle(200, 650, 800, 750, fill = "red", outline = "white", width = 4)
    inst_Button_Text = s.create_text(500, 700, text = "RULES", font = "Helvetica 60 bold", fill = "white")
    Exit_Button_Text = s.create_text(500, 850, text = "EXIT", font = "Helvetica 60 bold", fill = "white")
    
    logo = s.create_image(500, 250, image = Logoimg)

    if ClickX != None:
        
        if ClickX < 800 and ClickX > 200 and ClickY < 600 and ClickY > 500:
            game_Start = "Diffculty"

        elif ClickX < 800 and ClickX > 200 and ClickY < 750 and ClickY > 650:
            game_Start = "Rules"

        elif ClickX < 800 and ClickX > 200 and ClickY < 900 and ClickY > 800:
            Exit()
            

#Player Choose Diffculty
def Diffculty_Choose():
    global Easy_Button, Medium_Button, Hard_Button, Easy_Button_Text, Medium_Button_Text, Hard_Button_Text, game_Start, diffculty_Logo

    diffculty_Logo = s.create_image(500, 250, image = diffcultyLogoimg)
    
    Easy_Button = s.create_rectangle(200, 500, 800, 600, fill = "red", outline = "white", width = 4)
    Medium_Button = s.create_rectangle(200, 650, 800, 750, fill = "red", outline = "white", width = 4)
    Hard_Button = s.create_rectangle(200, 800, 800, 900, fill = "red", outline = "white", width = 4)

    Easy_Button_Text = s.create_text(500, 550, text = "EASY", font = "Helvetica 60 bold", fill = "white")
    Medium_Button_Text = s.create_text(500, 700, text = "MEDIUM", font = "Helvetica 60 bold", fill = "white")
    Hard_Button_Text = s.create_text(500, 850, text = "HARD", font = "Helvetica 60 bold", fill = "white")

    if ClickX != None:
        if ClickX < 800 and ClickX > 200 and ClickY < 600 and ClickY > 500:
            Diffculty("EASY")
            Starting_Values()
            game_Start = True

        elif ClickX < 800 and ClickX > 200 and ClickY < 750 and ClickY > 650:
            Diffculty("MEDIUM")
            Starting_Values()
            game_Start = True

        elif ClickX < 800 and ClickX > 200 and ClickY < 900 and ClickY > 800:
            Diffculty("HARD")
            Starting_Values()
            game_Start = True

#Rules Page
def Rules():
    global Rules_Back_Button, Rules_Down_Button, Rules_Up_Button, Rules_Back_Button_Text, game_Start, rules
    
    Rules_Back_Button = s.create_rectangle(300, 800, 700, 900, fill = "red", outline = "white", width = 4)
    Rules_Down_Button = s.create_polygon(270, 800, 150, 850, 270, 900, fill = "red", outline = "white", width = 4)
    Rules_Up_Button = s.create_polygon(730, 800, 850, 850, 730, 900, fill = "red", outline = "white", width = 4)

    Rules_Back_Button_Text = s.create_text(500, 850, text = "BACK", font = "Helvetica 60 bold", fill = "white")

    rules = s.create_image(500, 400, image = rulesimg)

    if ClickX != None:     
        if ClickX < 700 and ClickX > 300 and ClickY < 900 and ClickY > 800:
            game_Start = False

#Resets Click History
def Click_Reset():
    global ClickX, ClickY
    
    ClickX = None
    ClickY = None

#Mouse Movement
def MouseMove(event):
    global PlayerX, PlayerY, Alive

    if Alive == True:
        PlayerX = event.x
        PlayerY = event.y

#Mouse Click
def MouseClick(event):
    global ClickX, ClickY
    
    ClickX = event.x
    ClickY = event.y

#KeyBoard Click
def KeyClick(event):
    global game_Start
    
    if Alive == True and game_Start == True:
        game_Start = "Pause"
    

#Sets Default Values
def Starting_Values():
    global hitTime
    global game_Start, Logoimg, diffcultyLogoimg, Easy_Button, Hard_Button, Medium_Button, Easy_Button_Text, Medium_Button_Text, Hard_Button_Text
    global diffculty_Logo, gamePauseimg, rulesimg, rules
    global menu_Button, menu_Button_Text, retry_Button, retry_Button_Text
    global Rules_Back_Button, Rules_Up_Button, Rules_Down_Button, Rules_Back_Button_Text
    global greenProjectile, greenProjectileX, greenProjectileY, player_Projectile_Num, Player_Projectile
    global PlayerX, PlayerY, ClickX, ClickY, Player, gameOver, Alive, hitPoints, Damage
    global explosionimg, explosionX, explosionY, explosionFrame, explosion
    global spaceShip, greenFighterimg, redFighterimg, yellowFighterimg, greenFighter2img, redFighter2img, yellowFighter2img
    global killScore, FighterX, FighterY, FighterSpeed, Fighterimg, FighterHP, FighterHPTotal, Fighter, FighterHPBar, FighterHPBarOutline
    global FighterType, FighterFR
    global redProjectile, enemyProjectileX, enemyProjectileY, enemy_Projectile
    global scoreText, score, heartimg, heart
    global spaceStationimg, spaceStationHPFull, spaceStationHP, spaceStationX, spaceStationY, Boss, spaceStation_Direction
    global boss_Projectile_Speedx, boss_Projectile_Speedy, boss_Projectileimg, boss_Projectilex, boss_Projectiley, boss_Projectile
    global Player_Projectile_Del, enemy_Projectile_Del, upgrade_Del, Fighter_Del, explosion_Del
    global projectileNumUpgradeimg, projectileDamUpgradeimg, projectileUpgradeY, projectileUpgradeX, projectileUpgrade, projectileUpgradeimg
    global glassimg, glassX, glassY, glass, frameNum, Diffculty

    s.delete("all")

    #Timer
    hitTime = time.time()

    #Key Binds
    s.bind("<Motion>", MouseMove)
    s.bind("<Button-1>", MouseClick)
    s.bind("<Escape>", KeyClick)
    
    game_Start = False

    #Logo
    Logoimg = PhotoImage(file = "./Assets/Logo.gif")
    diffcultyLogoimg = PhotoImage(file = "./Assets/Diffculty Logo.gif")
    gamePauseimg = PhotoImage(file = "./Assets/Game Paused.gif")

    #Rules Visuals
    rulesimg = PhotoImage(file = "./Assets/CS Game Rules.gif")
    rules = None

    #Default Buttons
    Easy_Button = None
    Medium_Button = None
    Hard_Button = None
    Easy_Button_Text = None
    Medium_Button_Text = None
    Hard_Button_Text = None
    diffculty_Logo = None
    menu_Button = None
    menu_Button_Text = None
    retry_Button = None
    retry_Button_Text = None
    Rules_Back_Button = None
    Rules_Up_Button = None
    Rules_Down_Button = None
    Rules_Back_Button_Text = None

    #Player Projectiles
    greenProjectile = PhotoImage(file = "./Assets/Green Projectile.gif")
    greenProjectileX = []
    greenProjectileY = []

    player_Projectile_Num = 1
    Player_Projectile = [None] * 20

    #Player
    hitPoints = sethitPoints
    PlayerX = 500
    PlayerY = 800
    ClickX = None
    ClickY = None
    Player = None
    gameOver = None
    Alive = True
    Damage = 1

    #Explosion
    explosionimg = []
    explosionX = []
    explosionY = []
    explosionFrame = []
    explosion = [None] * 100
    for i in range(1, 8):
        explosionimg.append(PhotoImage(file = "./Assets/Explosion/Explosion " + str(i) + ".gif"))
       
    #Ships
    spaceShip = PhotoImage(file = "./Assets/SpaceShip.gif")
    greenFighterimg = PhotoImage(file = "./Assets/Green Fighter.gif")
    redFighterimg = PhotoImage(file = "./Assets/Red Fighter.gif")
    yellowFighterimg = PhotoImage(file = "./Assets/Yellow Fighter.gif")
    greenFighter2img = PhotoImage(file = "./Assets/Green Fighter 2.gif")
    redFighter2img = PhotoImage(file = "./Assets/Red Fighter 2.gif")
    yellowFighter2img = PhotoImage(file = "./Assets/Yellow Fighter 2.gif")

    #Score
    scoreText = None
    score = 0
    
    #Fighter Default Settings
    killScore = [50] * FighterNum
    FighterX = [None] * FighterNum
    FighterY = [None] * FighterNum
    FighterSpeed = [None] * FighterNum
    Fighterimg = [None] * FighterNum
    FighterHP = [None] * FighterNum
    FighterHPTotal = [None] * FighterNum
    Fighter = [None] * FighterNum
    FighterHPBar = [None] * FighterNum
    FighterHPBarOutline = [None] * FighterNum
    FighterType = [None] * FighterNum
    FighterFR = [None] * FighterNum

    for i in range(FighterNum):
        Fighter_Location_Reset(i, score)

    #Enemy Projectiles
    redProjectile = PhotoImage(file = "./Assets/Enemy Red Projectile.gif")
    enemyProjectileX = []
    enemyProjectileY = []
    enemy_Projectile = [None] * int(FighterNum * 5 * diffculty_Inc)

    #Player Health Points
    heartimg = PhotoImage(file = "./Assets/Heart.gif")
    heart = [None] * hitPoints

    #Bosses
    boss_Projectileimg = PhotoImage(file = "./Assets/Boss Projectile.gif")
    spaceStationimg = PhotoImage(file = "./Assets/spacestation.gif")
    spaceStationHPFull = 300 * diffculty_Inc
    spaceStationHP = 300 * diffculty_Inc
    spaceStationX = 500
    spaceStationY = -500
    Boss = False
    spaceStation_Direction = "L"
    boss_Projectile_Speedx = []
    boss_Projectile_Speedy = []
    boss_Projectilex = []
    boss_Projectiley = []
    boss_Projectile = [None] * boss_Projectile_Num

    #Deletion Arrays
    Player_Projectile_Del = []
    enemy_Projectile_Del = []
    upgrade_Del = []
    Fighter_Del = []
    explosion_Del = []

    #Projectile Upgrade
    projectileNumUpgradeimg = PhotoImage(file = "./Assets/Projectile Number Upgrade.gif")
    projectileDamUpgradeimg = PhotoImage(file = "./Assets/Projectile Damage Upgrade.gif")
    projectileUpgradeX = []
    projectileUpgradeY = []
    projectileUpgrade = [None] * 10
    projectileUpgradeimg = []

    #Cracked Glass
    glassimg = PhotoImage(file = "./Assets/Cracked Glass.gif")
    glassX = []
    glassY = []
    glass = [None] * 10

    frameNum = 0

#Default Values for Stars
def Star_Values():
    global starX, starY, starSpeed, starNum, starSize, star
    
    starX = []
    starY = []
    starSpeed = []
    starNum = 250
    starSize = []
    star = [None] * starNum

    for i in range(starNum):
        starX.append(randint(-50, 1050))
        starY.append(randint(-50, 1050))
        starSpeed.append(randint(1, 3))
        starSize.append(randint(1, 4))

#Creates Stars in Background
def create_Stars(starNum):
    
    for f in range(starNum):
        star[f] = create_circle(starX[f], starY[f], starSize[f] / 2, fill = "white", outline = "white")

        if frameNum % 3 == 0:
            starY[f] = starY[f] + starSpeed[f]

        if starY[f] > 1050:
            starY[f] = -50

#Create Upgrade Drops
def upgrade_Drop():
    global player_Projectile_Num, Damage
    
    for f in range(len(projectileUpgradeX)):
        projectileUpgrade[f] = s.create_image(projectileUpgradeX[f], projectileUpgradeY[f], image = projectileUpgradeimg[f])
        projectileUpgradeY[f] = projectileUpgradeY[f] + 1

        if projectileUpgradeY[f] >= 1050:
            upgrade_Del.append(f)

        if projectileUpgradeX[f] < PlayerX + 40 and projectileUpgradeX[f] > PlayerX - 40 and projectileUpgradeY[f] < PlayerY + 25 and projectileUpgradeY[f] > PlayerY - 25:
            upgrade_Del.append(f)

            if projectileUpgradeimg[f] == projectileNumUpgradeimg:
                
                if player_Projectile_Num != 3:
                    player_Projectile_Num = player_Projectile_Num + 1

            elif projectileUpgradeimg[f] == projectileDamUpgradeimg:

                Damage = Damage + 0.5

#Creates Enemies
def create_Enemy(FighterNum):
    
    #Creates Enemy Fired Projectiles
    for f in range(FighterNum):
        
        if frameNum % FighterFR[f] == 0:

            if FighterType[f] == "Single":
                enemyProjectileX.append(FighterX[f])
                enemyProjectileY.append(FighterY[f])

            elif FighterType[f] == "Double":
                enemyProjectileX.append(FighterX[f] + 10)
                enemyProjectileY.append(FighterY[f])
                enemyProjectileX.append(FighterX[f] - 10)
                enemyProjectileY.append(FighterY[f])

    for f in range(len(enemyProjectileX)):
        enemy_Projectile[f] = s.create_image(enemyProjectileX[f], enemyProjectileY[f], image = redProjectile)
        enemyProjectileY[f] = enemyProjectileY[f] + enemyProjectileSpeed

        if enemyProjectileY[f] > 1050 or enemyProjectileY[f] < - 50:
            enemy_Projectile_Del.append(f)
            
    #Creates Enemies 
    for f in range(FighterNum):
        Fighter[f] = s.create_image(FighterX[f], FighterY[f], image = Fighterimg[f])

        if frameNum % 2 == 0:
            FighterY[f] = FighterY[f] + FighterSpeed[f]

        if FighterY[f] > 1050:
            Fighter_Del.append(f)

    #Creates Enemy Health Bars
    for f in range(FighterNum):
        FighterHPBar[f] = s.create_rectangle(FighterX[f] - 25, FighterY[f] - 30, FighterX[f] + 25 * (1 - (1 - FighterHP[f] / FighterHPTotal[f]) * 2), FighterY[f] - 35, fill = "red")
        FighterHPBarOutline[f] = s.create_rectangle(FighterX[f] - 25, FighterY[f] - 30, FighterX[f] + 25, FighterY[f] - 35, fill = '', outline = "white")

#Enemy Hitboxes and Explosions
def enemy_Hitbox_Explosion():
    global score
        
    for f in range(len(greenProjectileY)):

        for i in range(FighterNum):
            
            if greenProjectileX[f] < FighterX[i] + 20 and greenProjectileX[f] > FighterX[i] - 20 and greenProjectileY[f] < FighterY[i] + 20 and greenProjectileY[f] > FighterY[i] - 20:

                FighterHP[i] = FighterHP[i] - Damage
                
                if f not in Player_Projectile_Del:
                    Player_Projectile_Del.append(f)

                if FighterHP[i] <= 0:
                    FighterHP[i] = 0
                    
                    #Upgrade Drop Chance
                    if randint(1, 35) == 1 and Player_Projectile != 3:
                        projectileUpgradeX.append(FighterX[i])
                        projectileUpgradeY.append(FighterY[i])

                        if player_Projectile_Num != 3:
                            projectileUpgradeimg.append(choice([projectileNumUpgradeimg, projectileDamUpgradeimg]))

                        else:
                            projectileUpgradeimg.append(projectileDamUpgradeimg)

                    #Explosion X Y
                    explosionX.append(FighterX[i])
                    explosionY.append(FighterY[i])
                    explosionFrame.append(0)
                    score = score + killScore[i]
                    Fighter_Del.append(i)

#Creates Player
def create_Player():
    global Player, PlayerX, PlayerY, greenProjectile 
        
    #Creates Player Fired Projectiles   
    if player_Projectile_Num == 1 and frameNum % 20 == 0:
        
        greenProjectileX.append(PlayerX)
        greenProjectileY.append(PlayerY)

    elif player_Projectile_Num == 2 and  frameNum % 13 == 0:

        if frameNum % 2 == 0:
            greenProjectileX.append(PlayerX - 20)

        else:
            greenProjectileX.append(PlayerX + 20)
            
        greenProjectileY.append(PlayerY)

    elif player_Projectile_Num == 3 and  frameNum % 7 == 0:

        if frameNum % 3 == 0:
            greenProjectileX.append(PlayerX - 30)

        elif frameNum % 3 == 1:
            greenProjectileX.append(PlayerX)

        else:
            greenProjectileX.append(PlayerX + 30)

        greenProjectileY.append(PlayerY)

    if Damage == 1:
        greenProjectile = PhotoImage(file = "./Assets/Green Projectile.gif")

    elif Damage == 1.5:
        greenProjectile = PhotoImage(file = "./Assets/Yellow Projectile.gif")

    elif Damage == 2:
        greenProjectile = PhotoImage(file = "./Assets/Red Projectile.gif")

    else:
        greenProjectile = PhotoImage(file = "./Assets/Blue Projectile.gif")

    for f in range(len(greenProjectileX)):
        
        Player_Projectile[f] = s.create_image(greenProjectileX[f], greenProjectileY[f], image = greenProjectile)
        greenProjectileY[f] = greenProjectileY[f] - 15

        if greenProjectileY[f] <= -100:
            Player_Projectile_Del.append(f)

    #Creates Spaceship of Player
    Player = s.create_image(PlayerX, PlayerY, image = spaceShip)

#Player Hitboxes and Affects
def player_Hitbox_Explosion():
    global Alive, hitPoints, hitTime

    #Fghter Projectiles
    for f in range(len(enemyProjectileX)):
        if Alive == True:
            
            if time.time() - hitTime > 1:
                
                if enemyProjectileX[f] < PlayerX + 40 and enemyProjectileX[f] > PlayerX - 40 and enemyProjectileY[f] < PlayerY + 25 and enemyProjectileY[f] > PlayerY - 25:
                    hitPoints = hitPoints - 1
                    enemy_Projectile_Del.append(f)
                    hitTime = time.time()

                    #Add Broken Glass
                    glassX.append(randint(0, 1000))
                    glassY.append(randint(0, 1000))

                if hitPoints == 0:
                    Alive = False
                    
                    for i in range(20):
                        explosionX.append(PlayerX + randint(-50, 50))
                        explosionY.append(PlayerY + randint(-50, 50))
                        explosionFrame.append(0)

    #Boss Projectiles
    for f in range(len(boss_Projectilex)):
        if Alive == True:
            
            if time.time() - hitTime > 1:
                
                if boss_Projectilex[f] < PlayerX + 40 and boss_Projectilex[f] > PlayerX - 40 and boss_Projectiley[f] < PlayerY + 25 and boss_Projectiley[f] > PlayerY - 25:
                    hitPoints = hitPoints - 1
                    hitTime = time.time()
                    boss_Projectilex[f] = 1200
                    boss_Projectiley[f] = 1200

                    #Add Broken Glass
                    glassX.append(randint(0, 1000))
                    glassY.append(randint(0, 1000))

                if hitPoints == 0:
                    Alive = False
                    
                    for i in range(20):
                        explosionX.append(PlayerX + randint(-50, 50))
                        explosionY.append(PlayerY + randint(-50, 50))
                        explosionFrame.append(0)

#Creates Game Boss
def create_Boss():
    global spaceStation, spaceStationX, spaceStationY, spaceStationHPBar, spaceStationHPBarOutline, spaceStation_Direction, spaceStationHP, score, Boss

    #Boss Projectiles
    if spaceStationY >= 300 and spaceStationHP > 0:
        Boss_Projectile()

    #Game Boss
    Boss = True
    spaceStation = s.create_image(spaceStationX, spaceStationY, image = spaceStationimg)
    spaceStationHPBar = s.create_rectangle(spaceStationX - 200, spaceStationY - 150, spaceStationX + 200 * (1 - (1 - spaceStationHP / spaceStationHPFull) * 2), spaceStationY - 160, fill = "red")
    spaceStationHPBarOutline = s.create_rectangle(spaceStationX - 200, spaceStationY - 150, spaceStationX + 200, spaceStationY - 160, outline = "white", fill = '')

    if spaceStationY < 300:
        spaceStationY = spaceStationY + 2

    else:
        
        if spaceStationX > 150 and spaceStation_Direction == "L":
            spaceStationX = spaceStationX - 3

        elif spaceStationX < 850 and spaceStation_Direction == "R":
            spaceStationX = spaceStationX + 3

        if spaceStationX < 150:
            spaceStation_Direction = "R"

        elif spaceStationX > 850:
            spaceStation_Direction = "L"

    for f in range(len(greenProjectileY)):

        if greenProjectileX[f] < spaceStationX + 120 and greenProjectileX[f] > spaceStationX - 120 and greenProjectileY[f] < spaceStationY + 120 and greenProjectileY[f] > spaceStationY - 120:
            spaceStationHP = spaceStationHP - Damage
            Player_Projectile_Del.append(f)

    if spaceStationHP <= 0:
        score = score + 3000

        for i in range(60):
            explosionX.append(spaceStationX + randint(-100, 100))
            explosionY.append(spaceStationY + randint(-100, 100))
            explosionFrame.append(0)
        
#Creates Boss Projectiles
def Boss_Projectile():
    global boss_Projectilex, boss_Projectiley, boss_Projectile_Speedx, boss_Projectile_Speedy
    
    if frameNum % 170 == 0:
        boss_Projectilex = []
        boss_Projectiley = []
        boss_Projectile_Speedx = []
        boss_Projectile_Speedy = []
    
        for f in range(boss_Projectile_Num):
            boss_Projectilex.append(spaceStationX + randint(-20, 20))
            boss_Projectiley.append(spaceStationY + randint(-20, 20))

            if f % 2 == 0:
                boss_Projectile_Speedx.append(randint(-8, 8))

                if boss_Projectile_Speedx[f] < 5 and boss_Projectile_Speedx[f] > -5:
                    boss_Projectile_Speedy.append(choice([-8, -7, -6, -5, 5, 6, 7, 8]))

                else:
                    boss_Projectile_Speedy.append(randint(-8, 8))
            
            else:
                boss_Projectile_Speedy.append(randint(-8, 8))

                if boss_Projectile_Speedy[f] < 5 and boss_Projectile_Speedy[f] > -5:
                    boss_Projectile_Speedx.append(choice([-8, -7, -6, -5, 5, 6, 7, 8]))

                else:
                    boss_Projectile_Speedx.append(randint(-8, 8))

    #Hit Box
    for f in range(len(boss_Projectilex)):
        boss_Projectile[f] = s.create_image(boss_Projectilex[f], boss_Projectiley[f], image = boss_Projectileimg)
        boss_Projectilex[f] = boss_Projectile_Speedx[f] + boss_Projectilex[f]
        boss_Projectiley[f] = boss_Projectile_Speedy[f] + boss_Projectiley[f]

#Creates Explosion
def create_Explosion():
    
    for f in range(len(explosionX)):
        explosion[f] = s.create_image(explosionX[f], explosionY[f], image = explosionimg[explosionFrame[f]])

        if frameNum % 3 == 0:
            explosionFrame[f] = explosionFrame[f] + 1

        if explosionFrame[f] == 7:
            explosion_Del.append(f)

#Miscllaneous Affects
def other_Affects():
    global scoreText, gameOver

    #Creates Broken Glass
    if game_Start == True:
        for f in range(len(glassX)):
            glass[f] = s.create_image(glassX[f], glassY[f], image = glassimg)

    #Score during game
    if Alive == True and game_Start == True:
        scoreText = s.create_text(900, 90, text = score, font = "Helvetica 40 bold", fill = "white")

        #Player Health Points
        for f in range(hitPoints):
            heart[f] = s.create_image(970 - f * 60, 35, image = heartimg)

#End Game Screen
def Game_Over():
    global menu_Button, menu_Button_Text, retry_Button, retry_Button_Text, gameOver, scoreText, game_Start, Exit_Button_Text, Exit_Button
    
    menu_Button = s.create_rectangle(200, 500, 800, 600, fill = "red", outline = "white", width = 4)
    menu_Button_Text = s.create_text(500, 550, text = "MENU", font = "Helvetica 60 bold", fill = "white")
    
    Exit_Button = s.create_rectangle(200, 800, 800, 900, fill = "red", outline = "white", width = 4)
    Exit_Button_Text = s.create_text(500, 850, text = "EXIT", font = "Helvetica 60 bold", fill = "white")

    retry_Button = s.create_rectangle(200, 650, 800, 750, fill = "red", outline = "white", width = 4)
    retry_Button_Text = s.create_text(500, 700, text = "RETRY", font = "Helvetica 60 bold", fill = "white")

    gameOver = s.create_text(500, 330, text = "GAMEOVER", font = "Helvetica 100 bold", fill = "white")
    scoreText = s.create_text(500, 430, text = "SCORE: " + str(score), font = "Helvetica 60 bold", fill = "white")

    if ClickX != None:
        if ClickX < 800 and ClickX > 200 and ClickY < 600 and ClickY > 500:
            Starting_Values()
            game_Start = False

        elif ClickX < 800 and ClickX > 200 and ClickY < 750 and ClickY > 650:
            Starting_Values()
            game_Start = True

        elif ClickX < 800 and ClickX > 200 and ClickY < 900 and ClickY > 800:
            Exit()

#Closes the Game
def Exit():
    s.delete("all")
    s.update
    root.destroy()
    sys.exit("Game has exited.")

#Deletes all Objects
def delete_All():

    s.delete(start_Button, start_Button_Text, logo, inst_Button, inst_Button_Text, Exit_Button, Exit_Button_Text)
    s.delete(Easy_Button, Medium_Button, Hard_Button, Easy_Button_Text, Medium_Button_Text, Hard_Button_Text, diffculty_Logo)
    s.delete(Player, scoreText, gameOver)
    s.delete(menu_Button, menu_Button_Text, retry_Button, retry_Button_Text, Exit_Button, Exit_Button_Text)
    s.delete(Rules_Back_Button, Rules_Down_Button, Rules_Up_Button, Rules_Back_Button_Text, rules)
    
    if Boss == True:
        s.delete(spaceStation, spaceStationHPBar, spaceStationHPBarOutline)
        for f in range(boss_Projectile_Num):
            s.delete(boss_Projectile[f])

    for f in range(len(Fighter_Del) -1, -1, -1):
        Fighter_Location_Reset(Fighter_Del[f], score)
        del Fighter_Del[f]

    for f in range(starNum):
        s.delete(star[f])

    for f in range(FighterNum):
        s.delete(Fighter[f], FighterHPBar[f], FighterHPBarOutline[f])

    for f in range(len(enemy_Projectile)):
        s.delete(enemy_Projectile[f])

    for f in range(len(enemy_Projectile_Del)):
        del enemyProjectileX[max(enemy_Projectile_Del)]
        del enemyProjectileY[max(enemy_Projectile_Del)]
        enemy_Projectile_Del.remove(max(enemy_Projectile_Del))
    
    for f in range(len(Player_Projectile)):
        s.delete(Player_Projectile[f])

    if len(Player_Projectile_Del) <= len(greenProjectileX):
        for f in range(len(Player_Projectile_Del)):
            del greenProjectileX[max(Player_Projectile_Del)]
            del greenProjectileY[max(Player_Projectile_Del)]
            Player_Projectile_Del.remove(max(Player_Projectile_Del))

    for f in range(len(explosion)):
        s.delete(explosion[f])

    for f in range(len(explosion_Del)):
        del explosionX[max(explosion_Del)]
        del explosionY[max(explosion_Del)]
        del explosionFrame[max(explosion_Del)]
        explosion_Del.remove(max(explosion_Del))

    for f in range(hitPoints):
        s.delete(heart[f])

    for f in range(len(projectileUpgradeX)):
        s.delete(projectileUpgrade[f])

    for f in range(len(upgrade_Del)):
        del projectileUpgradeX[max(upgrade_Del)]
        del projectileUpgradeY[max(upgrade_Del)]
        del projectileUpgradeimg[max(upgrade_Del)]
        upgrade_Del.remove(max(upgrade_Del))

    for f in range(len(glassX)):
        s.delete(glass[f])

#Changes User Screen
def Selection():
    if game_Start == False:
            Start_Menu()

    elif game_Start == "Diffculty":
        Diffculty_Choose()

    elif game_Start == "Rules":
        Rules()

    elif Alive == False and game_Start == True:
        Game_Over()

#Game Paused Screen  
def Pause_Menu():
    global resume_Button, resume_Button_Text, menu_Button, menu_Button_Text, game_Start, gamePause, Exit_Button, Exit_Button_Text

    gamePause = s.create_image(500, 280, image = gamePauseimg)
    
    resume_Button = s.create_rectangle(200, 500, 800, 600, fill = "red", outline = "white", width = 4)
    resume_Button_Text = s.create_text(500, 550, text = "RESUME", font = "Helvetica 60 bold", fill = "white")

    menu_Button = s.create_rectangle(200, 650, 800, 750, fill = "red", outline = "white", width = 4)
    menu_Button_Text = s.create_text(500, 700, text = "MENU", font = "Helvetica 60 bold", fill = "white")
    
    Exit_Button = s.create_rectangle(200, 800, 800, 900, fill = "red", outline = "white", width = 4)
    Exit_Button_Text = s.create_text(500, 850, text = "EXIT", font = "Helvetica 60 bold", fill = "white")

    if ClickX != None:
        if ClickX < 800 and ClickX > 200 and ClickY < 600 and ClickY > 500:
            delete_All()
            game_Start = True

        elif ClickX < 800 and ClickX > 200 and ClickY < 750 and ClickY > 650:
            Starting_Values()
            game_Start = False

        elif ClickX < 800 and ClickX > 200 and ClickY < 900 and ClickY > 800:
            Exit()
    

#Runs the Game
def runGame():
    global frameNum
    
    Diffculty("NON")
    Starting_Values()
    Star_Values()

    while True:

        if game_Start != "Pause":
            frameNum = frameNum + 1

            create_Stars(starNum)
            upgrade_Drop()

            if score >= 10000 and spaceStationHP > 0:
                create_Boss()

            if game_Start == True:
                create_Enemy(FighterNum)

            if Alive == True and game_Start == True:
                create_Player()
                enemy_Hitbox_Explosion()
                
            player_Hitbox_Explosion()
            create_Explosion()
        
            other_Affects()

            Selection()
            
            Click_Reset()
           
            s.update()
            
            if game_Start != "Pause":
                delete_All()

        else:
            Pause_Menu()
            s.update()
            s.delete(resume_Button, resume_Button_Text, gamePause, Exit_Button, Exit_Button_Text, menu_Button, menu_Button_Text)

root.after(0, runGame)
s.focus_set()
root.mainloop()

#Reminders
#Add HP bars for enemies #DONE
#Fix score tracker #DONE
#Add boss projectiles #DONE
#Add powerups #DONE
#Add start menu #DONE
#Add rules page #DONE
#Add diffculty settings #DONE
#Add hit effect #DONE
#Add 1s invcinibility after being hit #DONE
#Add pause menu #DONE







