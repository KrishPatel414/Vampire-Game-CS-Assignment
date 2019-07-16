#Krish Patel
#Tuesday, January 22 2019(Due Date)
#Dracula's Forest
#Survival Vampire Game




import pygame
pygame.init()
from random import randint

WIDTH=1000      #1200 is the biggest allowed for this assignment
HEIGHT=700      #700 is the biggest height allowed

#Create my game screen
game_window=pygame.display.set_mode((WIDTH,HEIGHT))

bat=False

#Death/Dust sound effect
death_sound_effect=pygame.mixer.Sound("Death_sound_effect.wav")
#Vampire eating sound effect
Vampire_bite_sound=pygame.mixer.Sound("Vampire_bite.wav")
#Beginning evil laugh sound effect
Vampire_laugh=pygame.mixer.Sound("evil_laugh.wav")
#Human1 sound effect
attack_sound_effect=pygame.mixer.Sound("human1 attack.wav")


#Import image of vampire looking right
Vampire=pygame.image.load("VampireRight.png")
#Get rectangle of vampire image
VampireRect=Vampire.get_rect()
Vampire_W=VampireRect.width
Vampire_H=VampireRect.height
#Co-ordinates of vampire
Vampire_x=645
Vampire_y=565
vampire_transformation=0
#End screen
gane_over=pygame.image.load("You Died.png")
delay=10
#Load in font
font = pygame.font.SysFont("Courier New Bold",25)

#Load in font for title(enlarged font)
title_font = pygame.font.SysFont("Courier New Bold",100)

#Load in welcome screen background
castle=pygame.image.load("castle.png")

#Load in human 1/hunter image
hunter_1=pygame.image.load("Human Sprites.png")

#Get rectangle of human 1 image
hunter_1Rect=hunter_1.get_rect()
hunter_1_W=hunter_1Rect.width
hunter_1_H=hunter_1Rect.height

#Co-ordinate of human 1
hunter_1_x=10
hunter_1_y=400
#Speed of human 1
Human_speed_x=3
Human_speed_y=3
#Boolean to see if human 1 is dead
is_dead_hunter_1=False

#Load in human 2 image
Human_2=pygame.image.load("Sprites of human 1.png")
#Get rectangle of human 2 image
Human_2Rect=Human_2.get_rect()
Human_2_W=Human_2Rect.width
Human_2_H=Human_2Rect.height

#Co-ordinate of human 2
Human_2_x=990
Human_2_y=400
#Speed of human 2
Human_2_speed_x=3
Human_2_speed_y=3
#Boolean to see if human 2 is dead
is_dead_human_2=False

#Load in human 3 image
Human_3=pygame.image.load("professor_1.png")
#Get rectangle of human 3 image
Human_3Rect=Human_3.get_rect()
Human_3_W=Human_3Rect.width
Human_3_H=Human_3Rect.height
#Co-ordinate of human 3
Human_3_x=500
Human_3_y=680
#Speed of human 3
Human_3_speed_x=3
Human_3_speed_y=3
#Boolean to see if human 3 is dead
is_dead_human_3=False

sound_counter=1

#Load in health bar outline 
health_bar=pygame.image.load("Health Bar.png")
#MAX health/where the health bear ends
health_bar_x=230

#Height of health bar "filling"
health_bar_y=55

#Load in day/night cycle
SUN=pygame.image.load("SUN.png")
MOON=pygame.image.load("MOON.png")

#Separate leg image for planned walking animation
Leg=pygame.image.load("LEG.png")
Leg_left=pygame.image.load("Leg_left.png")
Leg_left_2=pygame.image.load("Leg_left.png")

#Load in field
Field=pygame.image.load("grass1.png")
Leg_left=pygame.image.load("Leg_left.png")
Leg_left_2=pygame.image.load("Leg_left.png")

#Load in oval
oval=pygame.image.load("oval4.png")
#Get rectangle of image
ovalRect=oval.get_rect()
oval_W=ovalRect.width
oval_H=ovalRect.height
#Co-ordinates of oval
oval_x=645
oval_y=565

#Load in oval 2
oval_2=pygame.image.load("oval4.png")
#Get rectangle of image
oval_2Rect=oval_2.get_rect()
oval_2_W=oval_2Rect.width
oval_2_H=ovalRect.height
#Co-ordinates of oval
oval_2_x=250
oval_2_y=565


#Load in skeleton character
skeleton=pygame.image.load("skeletons_L_1.png")
#Get rectangle of image
skeletonRect=skeleton.get_rect()
skeleton_W=skeletonRect.width
skeleton_H=skeletonRect.height

#Get co-ordinates of skeleton
skeleton_x=250
skeleton_y=565

#Skeleton walking speed
skeleton_speed_x=3
skeleton_speed_y=3

#Counter for skeleton animation
skeleton_counter=0
is_dead_skeleton=False
#Counter for animation
bat_transformation=0

#Speed of vampire
Vampire_speed=5

#Day counter
day=0

#Counters for human walking animation
human_counter=0
human_2_counter=0
human_3_counter=0
death_counter=0

#Load in tree image
tree=pygame.image.load("tree.png")
#Get rectangle of tree image
treeRect=tree.get_rect()
tree_W=treeRect.width
tree_H=treeRect.height
#Co-ordinates of tree
tree_x=100
tree_y=400
field_height=300

#Positions of the Moon
moon_x=-200
moon_y=50

#Positions of Sun
sun_x=-200
sun_y=50

#Boolean to see if vampire is dead
vampire_is_dead=False

#X Speed of the Sun
sun_speed_x=10

health_bar_decrease=0

#X Speed of the Moon
moon_speed_x=10

#Colours for game
SKY_COLOUR=(133, 177, 247)
DAY_SKY_COLOUR=(133, 177, 247)
BLACK=( 0, 0, 0)
YELLOW=(255, 255, 0)
WHITE=(255,255 ,255)
GREEN=(4, 255, 0)
NIGHT_SKY_COLOUR=(61, 99, 160)
RED=(255, 20, 20)
CLOUDY_SKY=(86, 89, 88)

bat_counter=0
########
#More Booleans for game
start=False
game=True
menu=True
human_generate=False
#Game loop
while game:
    pygame.event.get()
    keys = pygame.key.get_pressed()
    #Fill screen with sky blue
    game_window.fill(SKY_COLOUR)
    #Create variables to store rectangle images
    treeRect=pygame.Rect(tree_x,tree_y,tree_W,tree_H)
    VampireRect=pygame.Rect(Vampire_x,Vampire_y,Vampire_W,Vampire_H)
    hunter_1Rect=pygame.Rect(hunter_1_x,hunter_1_y,hunter_1_W,hunter_1_H)
    Human_2Rect=pygame.Rect(Human_2_x,Human_2_y,Human_2_W,Human_2_H)
    Human_3Rect=pygame.Rect(Human_3_x,Human_3_y,Human_3_W,Human_3_H)
    ovalRect=pygame.Rect(oval_x,oval_y,oval_W,oval_H)
    oval_2Rect=pygame.Rect(oval_2_x,oval_2_y,oval_2_W,oval_2_H)
    skeletonRect=pygame.Rect(skeleton_x,skeleton_y,skeleton_W,skeleton_H)
    
    #Leg 1 and Leg 2 x and y values
    leg_x_1=Vampire_x+22
    leg_y_1=Vampire_y+50
    leg_x_2=Vampire_x+12
    leg_y_2=Vampire_y+50
    

    #If menu boolean is true, implement text. The \n function would have been used but was not working
    if menu==True:
        game_window.blit(castle,(0,0))
        #Makes Menu easier to read
        pygame.draw.rect(game_window, BLACK,(0, 550, 1000, 200),0)
        menu1 = font.render("As days pass, Dracula craves more and more of the blood of humans. It has been many days since",1,WHITE)
        menu2 = font.render("mortals have stepped into his woods and as days pass he becomes weaker. Today, Dracula heard",1,WHITE)
        menu3 = font.render("humans wandering.Help him satisfy his craving!",1,WHITE)
        menu5 = font.render("Use the WASD keys to move Dracula. Press and hold o to transform into a Bat",1,WHITE)
        menu6 = font.render("Hold L to transform back into a vampire! During transformations make you immobile and take some time.",1,WHITE)
        menu7 = font.render("As a bat Dracula's speed increases, he can survive in the Sun but can only eat skeletons. Skeletons",1,WHITE)
        menu8 = font.render("spawn after 5 days. During the night Dracula is safe to move about but as soon as he steps into the sunlight",1,WHITE)
        menu9 = font.render("he turns to dust.",1,WHITE)
        menu10 = font.render("Every night, if Dracula is not satisfied by his craving of human blood, he loses 1/3 of his health.",1,WHITE)
        menu11 = font.render("Possible Snacks for Dracula(Human form) Encompass:",1,WHITE)
        menu12 = font.render("- Weak Humans(Woman and professor)",1,WHITE)
        menu13 = font.render("- Hunter Humans(Blue anime character)",1,WHITE)
        menu14 = font.render("While weak humans likely allow you to consume them, hunters may attack you! To eat humans press",1,WHITE)
        menu15 = font.render("space when you collide with them . If you stay near the hunter for a long time, they may hit you again,",1,WHITE)
        menu16 = font.render("so be quick!This deals 1/3 damage to you! Good Luck- Press 'q' to continue",1,WHITE)
        title = title_font.render("Dracula's Forest",1,WHITE)
        #Location of text
        game_window.blit(menu1,(0,0))
        game_window.blit(menu2,(0,20))
        game_window.blit(menu3,(0,40))
        
        game_window.blit(menu5,(0,460))
        game_window.blit(menu6,(0,480))
        game_window.blit(menu7,(0,500))
        game_window.blit(menu8,(0,520))
        game_window.blit(menu9,(0,540))
        game_window.blit(menu10,(0,560))
        game_window.blit(menu11,(0,580))
        game_window.blit(menu12,(0,600))
        game_window.blit(menu13,(0,620))
        game_window.blit(menu14,(0,640))
        game_window.blit(menu15,(0,660))
        game_window.blit(menu16,(0,680))
        game_window.blit(title,(225,HEIGHT/2))
    
    #If q is pressed menu goes away and game starts
    if keys[pygame.K_q]:
        #Evil laugh is played
        Vampire_laugh.play()
        #Game begins
        start=True
        #Menu disappears
        menu=False

    #If start==true, the game begins
    if start==True:

        #Display the Day number
        day_text = font.render("Day "+str(day),1,BLACK)
        #Location of day counter
        game_window.blit(day_text,(100,10))

        
        #Proccess of making the sun and moon cycle
        #The sun appears and moves at a constant rate
        game_window.blit(SUN,(sun_x,sun_y))
        sun_x=sun_x+sun_speed_x
        #When the sun reaches the width+100 the moon appears
        if sun_x>=WIDTH+100:
            if SKY_COLOUR==DAY_SKY_COLOUR:
                human_spawn1=randint(1,3)

            #Sky turns dark
            SKY_COLOUR=NIGHT_SKY_COLOUR
            #Moon appears and moves right accross the screen at a constant rate
            game_window.blit(MOON,(moon_x,moon_y))
            moon_x=moon_x+moon_speed_x

        
        #When the moon reaches an x-value of the width+100 the sun appears
        if moon_x>=WIDTH+100:
            #Sky turns light
            SKY_COLOUR=DAY_SKY_COLOUR
            #Both the sun and moon's x-values reset
            moon_x=-200
            sun_x=-200
            health_bar_x=health_bar_x-58.3
            day=day+1

        
        #While the vampire is not dead
        if vampire_is_dead==False:
            #Draw in all of the images
            game_window.blit(oval,(oval_x,oval_y))
            game_window.blit(oval_2,(oval_2_x,oval_2_y))
            game_window.blit(Field,(0,300))
            pygame.draw.line(game_window, RED, (55,55),(health_bar_x, health_bar_y), 41)
            game_window.blit(health_bar,(0,0))
            game_window.blit(Field,(400,300))
            game_window.blit(Field,(800,300))
            game_window.blit(Leg,(leg_x_1,leg_y_1))
            game_window.blit(Leg,(leg_x_2,leg_y_2))
            game_window.blit(Vampire,(Vampire_x,Vampire_y))

            game_window.blit(hunter_1,(hunter_1_x,hunter_1_y))
            #Based on random number generator, spawn the number of humans and types of humans at night
            if SKY_COLOUR==NIGHT_SKY_COLOUR and human_spawn1==3:
                game_window.blit(hunter_1,(hunter_1_x,hunter_1_y))
                
            if SKY_COLOUR==NIGHT_SKY_COLOUR and human_spawn1==2:
                game_window.blit(Human_2,(Human_2_x,Human_2_y))
                game_window.blit(hunter_1,(hunter_1_x,hunter_1_y))
                if is_dead_human_2==True:
                    game_window.blit(Human_3,(Human_3_x,Human_3_y))

            elif SKY_COLOUR==NIGHT_SKY_COLOUR and human_spawn1==3:
                game_window.blit(Human_3,(Human_3_x,Human_3_y))
                game_window.blit(hunter_1,(hunter_1_x,hunter_1_y))
                if is_dead_human_3==True:
                    game_window.blit(Human_2,(Human_2_x,Human_2_y))
   
            else:
                game_window.blit(Human_2,(Human_2_x,Human_2_y))
                game_window.blit(Human_3,(Human_3_x,Human_3_y))


            #If it is day 5(day==5)spawn the skeleton
            if day>5:
                game_window.blit(skeleton,(skeleton_x,skeleton_y))
                #Skeleton animation
                skeleton_counter=skeleton_counter+1
                if  skeleton_counter==1:
                    skeleton=pygame.image.load("skeletons_L_1.png")
                if  skeleton_counter==2:
                    skeleton=pygame.image.load("skeletons_L_2.png")
                if  skeleton_counter==3:
                    skeleton=pygame.image.load("skeletons_L_3.png")
                if  skeleton_counter==4:
                    skeleton=pygame.image.load("skeletons_L_4.png")
                if  skeleton_counter==5:
                    skeleton=pygame.image.load("skeletons_L_5.png")
                    skeleton_counter=0
                    
            #Spawn trees infront of characters
            game_window.blit(tree,(400,300))
            game_window.blit(tree,(0,300))

            #This section of the code will allow the human 1/2/3 and skeleton to move randomly and bounce off the edges of the field

            #Increase both x and y values to make character move
            skeleton_y=skeleton_y+skeleton_speed_y
            skeleton_x=skeleton_x+skeleton_speed_x

            #Restrict character to area provided
            if skeleton_y>=HEIGHT or skeleton_y<=300:
                skeleton_speed_y=-skeleton_speed_y

            if skeleton_x>=WIDTH or skeleton_x<=0:
                skeleton_speed_x=-skeleton_speed_x

            #Increase both x and y values to make character move
            hunter_1_y=hunter_1_y+Human_speed_y
            hunter_1_x=hunter_1_x+Human_speed_x
            #Animation counter 
            human_counter=human_counter+1
            
            #Restrict character to area provided
            if hunter_1_y>=HEIGHT or hunter_1_y<=300:
                Human_speed_y=-Human_speed_y

            if hunter_1_x>=WIDTH or hunter_1_x<=0:
                Human_speed_x=-Human_speed_x
                
            #Increase both x and y values to make character move
            Human_2_y=Human_2_y+Human_2_speed_y
            Human_2_x=Human_2_x+Human_2_speed_x
            #Animation counter
            human_2_counter=human_2_counter+1
            
            #Restrict character to area provided
            if Human_2_y>=HEIGHT or Human_2_y<=300:
                Human_2_speed_y=-Human_2_speed_y

            if Human_2_x>=WIDTH or Human_2_x<=0:
                Human_2_speed_x=-Human_2_speed_x

            #Increase both x and y values to make character move
            Human_3_y=Human_3_y+Human_3_speed_y
            Human_3_x=Human_3_x+Human_3_speed_x

            #Animation counter 
            human_3_counter=human_3_counter+1

            #Restrict character to area provided
            if Human_3_y>=HEIGHT or Human_3_y<=300:
                Human_3_speed_y=-Human_3_speed_y

            if Human_3_x>=WIDTH or Human_3_x<=0:
                Human_3_speed_x=-Human_3_speed_x  
            

            #This section of code will have previous counters increase and as the values increase the images differ and create an animation
            if  human_2_counter==5:
                Human_2=pygame.image.load("Sprites of human 2.png")
            if  human_2_counter==10:
                Human_2=pygame.image.load("Sprites of human 3.png")
            if  human_2_counter==15:
                Human_2=pygame.image.load("Sprites of human 4.png")
            if  human_2_counter==20:
                Human_2=pygame.image.load("Sprites of human 5.png")
            if  human_2_counter==25:
                Human_2=pygame.image.load("Sprites of human 6.png")
            if  human_2_counter==30:
                Human_2=pygame.image.load("Sprites of human 7.png")
            if  human_2_counter==35:
                Human_2=pygame.image.load("Sprites of human 8.png")
            if  human_2_counter==40:
                Human_2=pygame.image.load("Sprites of human 9.png")
            if  human_2_counter==45:
                Human_2=pygame.image.load("Sprites of human 10.png")
                human_2_counter=0
                
            #This section of code will have previous counters increase and as the values increase the images differ and create an animation
            if  human_3_counter==5:
                Human_3=pygame.image.load("professor_2.png")
            if  human_3_counter==10:
                Human_3=pygame.image.load("professor_3.png")
            if  human_3_counter==15:
                Human_3=pygame.image.load("professor_4.png")
            if  human_3_counter==20:
                Human_3=pygame.image.load("professor_5.png")
            if  human_3_counter==25:
                Human_3=pygame.image.load("professor_6.png")
            if  human_3_counter==30:
                Human_3=pygame.image.load("professor_7.png")
            if  human_3_counter==35:
                Human_3=pygame.image.load("professor_8.png")
            if  human_3_counter==40:
                Human_3=pygame.image.load("professor_9.png")
                human_3_counter=0

            #This section of code will have previous counters increase and as the values increase the images differ and create an animation
            if  human_counter==5:
                hunter_1=pygame.image.load("Human Sprites.png")
            if  human_counter==10:
                hunter_1=pygame.image.load("Human Sprites 2.png")
            if  human_counter==15:
                hunter_1=pygame.image.load("Human Sprites3.png")
            if  human_counter==20:
                hunter_1=pygame.image.load("Human Sprites4.png")
            if  human_counter==25:
                hunter_1=pygame.image.load("Human Sprites5.png")
            if  human_counter==30:
                hunter_1=pygame.image.load("Human Sprites6.png")
            if  human_counter==35:
                hunter_1=pygame.image.load("Human Sprites7.png")
            if  human_counter==40:
                hunter_1=pygame.image.load("Human Sprites8.png")
            if  human_counter==45:
                hunter_1=pygame.image.load("Human Sprites9.png")
            if  human_counter==50:
                hunter_1=pygame.image.load("Human Sprites10.png")
            if  human_counter==55:
                hunter_1=pygame.image.load("Human Sprites11.png")
                human_counter=0

            
            #If o is held, an animation occurs allowing the vampire to transform into a bat
            if keys[pygame.K_o] and bat==False:
                #Make separate legs disapear
                bat_transformation=bat_transformation+1
                if bat_transformation==5:
                    Leg=pygame.image.load("invisable1.png")
                    Vampire=pygame.image.load("bat1.png")
                    Vampire_speed=0
                if bat_transformation==10:
                    Vampire=pygame.image.load("bat1.png")
                    Vampire_speed=0
                if bat_transformation==15:
                    Vampire=pygame.image.load("bat2.png")
                    Vampire_speed=0
                if bat_transformation==20:
                    Vampire=pygame.image.load("bat3.png")
                    Vampire_speed=0
                if bat_transformation==25:
                    Vampire=pygame.image.load("bat4.png")
                    Vampire_speed=0
                if bat_transformation==30:
                    Vampire=pygame.image.load("bat5.png")
                    Vampire_speed=0
                if bat_transformation==35:
                    Vampire=pygame.image.load("bat6.png")
                    Vampire_speed=10
                    vampire_transformation=0
                    bat=True
                    


            if keys[pygame.K_l] and bat==True:
                #Make separate legs disapear
                vampire_transformation=vampire_transformation+1
                if vampire_transformation==5:
                    Vampire=pygame.image.load("bat6.png")
                    Vampire_speed=0
                if vampire_transformation==10:
                    Vampire=pygame.image.load("bat5.png")
                    Vampire_speed=0
                if vampire_transformation==15:
                    Vampire=pygame.image.load("bat4.png")
                    Vampire_speed=0
                if vampire_transformation==20:
                    Vampire=pygame.image.load("bat3.png")
                    Vampire_speed=0
                if vampire_transformation==25:
                    Vampire=pygame.image.load("bat2.png")
                    Vampire_speed=0
                if vampire_transformation==30:
                    Vampire=pygame.image.load("bat1.png")
                    Vampire_speed=0
                if vampire_transformation==35:
                    Vampire_speed=5
                    Vampire=pygame.image.load("VampireRight.png")
                    Leg=pygame.image.load("Leg.png")
                    bat_transformation=0
                    bat=False
            #If exit is pressed end game
            if keys[pygame.K_ESCAPE]:
                game=False
                exit()

            #If w is pressed, vampire will move up(Y value decreases)
            if keys[pygame.K_w] and SKY_COLOUR==NIGHT_SKY_COLOUR or keys[pygame.K_w] and SKY_COLOUR==DAY_SKY_COLOUR:
                Vampire_y= Vampire_y-Vampire_speed

            #If a is pressed, vampire will move left(x value decreases)
            if keys[pygame.K_a] and SKY_COLOUR==NIGHT_SKY_COLOUR or keys[pygame.K_a] and SKY_COLOUR==DAY_SKY_COLOUR:
                Vampire_x= Vampire_x-Vampire_speed
                #Images are altered to make character turn
                Leg=pygame.image.load("Leg_left.png")
                Vampire=pygame.image.load("VampireLeft.png")

                #If bat transformation counter is above 0 and less than or equal to 5, keep certain image(So that pressing A will not change image)
                if bat_transformation>0 and bat_transformation<=5:
                    Leg=pygame.image.load("invisable1.png")
                    Vampire=pygame.image.load("bat1.png")

                #If bat transformation counter is above 5 and less than or equal to 10, keep certain image(So that pressing A will not change image)
                if bat_transformation>5 and bat_transformation<=10:
                    Leg=pygame.image.load("invisable1.png")
                    Vampire=pygame.image.load("bat1.png")
                #If bat transformation counter is above 10 and less than or equal to 15, keep certain image(So that pressing A will not change image)
                if bat_transformation>10 and bat_transformation<=15:
                    Leg=pygame.image.load("invisable1.png")
                    Vampire=pygame.image.load("bat2.png")

                #If bat transformation counter is above 15 and less than or equal to 20, keep certain image(So that pressing A will not change image)
                if bat_transformation>15 and bat_transformation<=20:
                    Leg=pygame.image.load("invisable1.png")
                    Vampire=pygame.image.load("bat3.png")

                #If bat transformation counter is above 20 and less than or equal to 25, keep certain image(So that pressing A will not change image)
                if bat_transformation>20 and bat_transformation<=25:
                    Leg=pygame.image.load("invisable1.png")
                    Vampire=pygame.image.load("bat4.png")

                #If bat transformation counter is above 25 and less than or equal to 30, keep certain image(So that pressing A will not change image)
                if bat_transformation>25 and bat_transformation<=30:
                    Leg=pygame.image.load("invisable1.png")
                    Vampire=pygame.image.load("bat5.png")

                #If bat transformation counter is greater than or equal to 35, keep certain image(So that pressing A will not change image)
                if bat_transformation>=35 :
                    Leg=pygame.image.load("invisable1.png")
                    Vampire=pygame.image.load("bat6_L.png")

                #If vampire transformation counter is above 0 and less than or equal to 5, keep certain image(So that pressing A will not change image)
                if vampire_transformation>0 and vampire_transformation<=5 and bat_transformation>=35:
                    Leg=pygame.image.load("invisable1.png")
                    Vampire=pygame.image.load("bat6.png")
                    
                #If vampire transformation counter is above 5 and less than or equal to 10, keep certain image(So that pressing A will not change image)
                if vampire_transformation>5 and vampire_transformation<=10:
                    Leg=pygame.image.load("invisable1.png")
                    Vampire=pygame.image.load("bat5.png")

                #If vampire transformation counter is above 10 and less than or equal to 15, keep certain image(So that pressing A will not change image)
                if vampire_transformation>10 and vampire_transformation<=15:
                    Leg=pygame.image.load("invisable1.png")
                    Vampire=pygame.image.load("bat4.png")
                    
                #If vampire transformation counter is above 15 and less than or equal to 20, keep certain image(So that pressing A will not change image)
                if vampire_transformation>15 and vampire_transformation<=20:
                    Leg=pygame.image.load("invisable1.png")
                    Vampire=pygame.image.load("bat3.png")

                #If vampire transformation counter is above 20 and less than or equal to 25, keep certain image(So that pressing A will not change image)
                if vampire_transformation>20 and vampire_transformation<=25:
                    Leg=pygame.image.load("invisable1.png")
                    Vampire=pygame.image.load("bat2.png")

                #If vampire transformation counter is above 25 and less than or equal to 30, keep certain image(So that pressing A will not change image)
                if vampire_transformation>25 and vampire_transformation<=30:
                    Vampire=pygame.image.load("bat2.png")
                
                #If vampire transformation counter greater than or equal to 35, keep certain image(So that pressing A will not change image)
                if vampire_transformation==35:
                    Vampire=pygame.image.load("VampireLeft.png")

                


            #If s is pressed, vampire will move down (Y value increases)   
            if  keys[pygame.K_s] and SKY_COLOUR==NIGHT_SKY_COLOUR or  keys[pygame.K_s] and SKY_COLOUR==DAY_SKY_COLOUR:
                Vampire_y= Vampire_y+Vampire_speed
                
            #Is d is pressed, vampire will move right(x value increases)                              
            if  keys[pygame.K_d] and SKY_COLOUR==NIGHT_SKY_COLOUR or keys[pygame.K_d] and SKY_COLOUR==DAY_SKY_COLOUR:
                Vampire_x= Vampire_x+Vampire_speed
                #Images are altered to make character turn
                Leg=pygame.image.load("Leg.png")
                Vampire=pygame.image.load("VampireRight.png")
                #If bat transformation counter is above 0 and less than or equal to 5, keep certain image(So that pressing D will not change image)
                if bat_transformation>0 and bat_transformation<=5:
                    Leg=pygame.image.load("invisable1.png")
                    Vampire=pygame.image.load("bat1.png")
                #If bat transformation counter is above 5 and less than or equal to 10, keep certain image(So that pressing D will not change image)
                if bat_transformation>5 and bat_transformation<=10:
                    Leg=pygame.image.load("invisable1.png")
                    Vampire=pygame.image.load("bat1.png")

                #If bat transformation counter is above 10 and less than or equal to 15, keep certain image(So that pressing D will not change image)
                if bat_transformation>10 and bat_transformation<=15:
                    Leg=pygame.image.load("invisable1.png")
                    Vampire=pygame.image.load("bat2.png")

                #If bat transformation counter is above 15 and less than or equal to 20, keep certain image(So that pressing D will not change image)
                if bat_transformation>15 and bat_transformation<=20:
                    Leg=pygame.image.load("invisable1.png")
                    Vampire=pygame.image.load("bat3.png")
                #If bat transformation counter is above 20 and less than or equal to 25, keep certain image(So that pressing D will not change image)
                if bat_transformation>20 and bat_transformation<=25:
                    Leg=pygame.image.load("invisable1.png")
                    Vampire=pygame.image.load("bat4.png")
                #If bat transformation counter is above 25 and less than or equal to 30, keep certain image(So that pressing D will not change image)
                if bat_transformation>25 and bat_transformation<=30:
                    Leg=pygame.image.load("invisable1.png")
                    Vampire=pygame.image.load("bat5.png")
                
                #If bat transformation counter is greater than or equal to 35, keep certain image(So that pressing D will not change image)
                if bat_transformation>=35 :
                    Leg=pygame.image.load("invisable1.png")
                    Vampire=pygame.image.load("bat6.png")

                #If vampire transformation counter is above 0 and less than or equal to 5, keep certain image(So that pressing D will not change image)
                if vampire_transformation>0 and vampire_transformation<=5:
                    Leg=pygame.image.load("invisable1.png")
                    Vampire=pygame.image.load("bat6.png")
                #If vampire transformation counter is above 5 and less than or equal to 10, keep certain image(So that pressing D will not change image)     
                if vampire_transformation>5 and vampire_transformation<=10:
                    Leg=pygame.image.load("invisable1.png")
                    Vampire=pygame.image.load("bat5.png")

                #If vampire transformation counter is above 10 and less than or equal to 15, keep certain image(So that pressing D will not change image)
                if vampire_transformation>10 and vampire_transformation<=15:
                    Leg=pygame.image.load("invisable1.png")
                    Vampire=pygame.image.load("bat4.png")

                #If vampire transformation counter is above 15 and less than or equal to 20, keep certain image(So that pressing D will not change image)
                if vampire_transformation>15 and vampire_transformation<=20:
                    Leg=pygame.image.load("invisable1.png")
                    Vampire=pygame.image.load("bat3.png")

                #If vampire transformation counter is above 20 and less than or equal to 25, keep certain image(So that pressing D will not change image)
                if vampire_transformation>20 and vampire_transformation<=25:
                    Leg=pygame.image.load("invisable1.png")
                    Vampire=pygame.image.load("bat2.png")

                #If vampire transformation counter is above 25 and less than or equal to 30, keep certain image(So that pressing D will not change image)
                if vampire_transformation>25 and vampire_transformation<=30:
                    Leg=pygame.image.load("invisable1.png")
                    Vampire=pygame.image.load("bat2.png")

                #If vampire transformation counter greater than or equal to 35, keep certain image(So that pressing D will not change image)
                if vampire_transformation==35:
                    Vampire=pygame.image.load("VampireRight.png")
                    Leg=pygame.image.load("Leg.png")

            #Keeps vampire inside of field
            if Vampire_y<=field_height-50:
                Vampire_y=Vampire_y+5
                
            if Vampire_x>=960:
                Vampire_x=Vampire_x-5
                
            if Vampire_x<=-20:
                Vampire_x=Vampire_x+5

            if Vampire_y>=620:
                Vampire_y=Vampire_y-5

            #Setting parameters for bat image
            if bat==True:
                if Vampire_y<=field_height-50:
                    Vampire_y=Vampire_y+10
                    
                if Vampire_x>=960:
                    Vampire_x=Vampire_x-10
                    
                if Vampire_x<=-20:
                    Vampire_x=Vampire_x+10

                if Vampire_y>=620:
                    Vampire_y=Vampire_y-10
                    
            #If the vampire leaves the shade during the day, vampire_is_dead==True(the vampire is dead)
            if not (SKY_COLOUR==NIGHT_SKY_COLOUR or ovalRect.colliderect(VampireRect) or oval_2Rect.colliderect(VampireRect)):
                vampire_is_dead=True

            #If the bat is in the sun it does not die.(If the bat image does not collide with the oval/shade images)
            if bat==True and not (SKY_COLOUR==NIGHT_SKY_COLOUR or ovalRect.colliderect(VampireRect) or oval_2Rect.colliderect(VampireRect)):
                vampire_is_dead=False
            human_attack=False

            #If space bar is pressed and vampire is collided with human1 he may eat human 1 or get hit
            if hunter_1Rect.colliderect(VampireRect) and keys[pygame.K_SPACE] and bat==False:
                Vampire_bite_sound.play()
                #50% chance to get hit
                attack_chance=randint(1,2)
                #If he gets hit, he loses 1/3 health
                if attack_chance==1:
                    attack_sound_effect.play()
                    health_bar_x=health_bar_x-58.3
                #If he eats the human, the human gets transported away
                if attack_chance==2:
                    hunter_1_x=-1000
                    hunter_1_x_speed=0
                    hunter_1_y_speed=0
                    #Human 1 death boolean is now true
                    is_dead_hunter_1=True
                    #If the vampire eats the human he gains 1/3 health
                    if health_bar_x<230:
                        health_bar_x=health_bar_x+58.3
                        #If the health bar surpases 230, the health bar is maxed out
                        if health_bar_x>=230:
                            health_bar_x=230

                
            
            #The vampire eats human 2 if human 2 and the vampire collide and the spacebar is pressed
            if Human_2Rect.colliderect(VampireRect)and keys[pygame.K_SPACE] and bat==False:
                #If he eats the human, the human gets transported away
                Vampire_bite_sound.play()
                Human_2_x=-1000
                Human_2_x_speed=0
                Human_2_y_speed=0
                #Human 2 death boolean is now true
                is_dead_human_2=True
                #If the vampire eats the human he gains 1/3 health
                if health_bar_x<230:
                        health_bar_x=health_bar_x+58.3
                        #If the health bar surpases 230, the health bar is maxed out
                        if health_bar_x>=230:
                            health_bar_x=230
            #The vampire eats human 3 if human 3 and the vampire collide and the spacebar is pressed
            if Human_3Rect.colliderect(VampireRect)and keys[pygame.K_SPACE] and bat==False:
                Vampire_bite_sound.play()
                #If he eats the human, the human gets transported away
                Human_3_x=-1000
                Human_3_x_speed=0
                Human_3_y_speed=0
                #Human 3 death boolean is now true
                is_dead_human_3=True
                #If the vampire eats the human he gains 1/3 health
                if health_bar_x<=230:
                        health_bar_x=health_bar_x+58.3
                        #If the health bar surpases 230, the health bar is maxed out
                        if health_bar_x>230:
                            health_bar_x=230
                            
             #The vampire eats human 3 if human 3 and the vampire collide and the spacebar is pressed
            if skeletonRect.colliderect(VampireRect)and keys[pygame.K_SPACE] and bat==True:
                #If he eats the human, the human gets transported away
                Vampire_bite_sound.play()
                skeleton_x=-1000
                skeleton_x_speed=0
                skeleton_y_speed=0
                #Human 3 death boolean is now true
                is_dead_skeleton=True
                #If the vampire eats the human he gains 1/3 health
                if health_bar_x<=230:
                        health_bar_x=health_bar_x+29.15
                        #If the health bar surpases 230, the health bar is maxed out
                        if health_bar_x>230:
                            health_bar_x=230
            #If all of the humans are eaten, they respawn
            if is_dead_hunter_1==True and is_dead_human_2==True and is_dead_human_3==True and day<5:
                is_dead_hunter_1=False
                is_dead_human_2=False
                is_dead_human_3=False
                #The 3 humans have their locations and speeds reset
                hunter_1_x=10
                hunter_1_y=400
                hunter_1_speed_x=3
                hunter_1_speed_y=3
        
                Human_2_x=990
                Human_2_y=500
                Human_2_speed_x=3
                Human_2_speed_y=3
                
                Human_3_x=500
                Human_3_y=500
                Human_3_speed_x=3
                Human_3_speed_y=3
            if day>=5 and is_dead_hunter_1==True and is_dead_human_2==True and is_dead_human_3==True and is_dead_skeleton:
                is_dead_hunter_1=False
                is_dead_human_2=False
                is_dead_human_3=False
                is_dead_skeleton=False
                
                #The 3 humans and skeleton have their locations and speeds reset
                hunter_1_x=10
                hunter_1_y=400
                hunter_1_speed_x=3
                hunter_1_speed_y=3
        
                Human_2_x=990
                Human_2_y=500
                Human_2_speed_x=3
                Human_2_speed_y=3
                
                Human_3_x=500
                Human_3_y=500
                Human_3_speed_x=3
                Human_3_speed_y=3

                skeleton_x=400
                skeleton_y=500
                skeleton_speed_x=3
                skeleton_speed_y=3
   
            #If the health bar is under a certain point, he is considered dead
            if health_bar_x<=65:
                vampire_is_dead=True
        #Vampire death sequence
            sound_counter=1
        else:
            #Previous images are loaded to keep the game imaging constant
            if sound_counter==1:
                death_sound_effect.play()
                sound_counter=2
            game_window.blit(oval,(oval_x,oval_y))
            hunter_1_y=hunter_1_y+Human_speed_y
            hunter_1_x=hunter_1_x+Human_speed_x
            human_counter=human_counter+1
            game_window.blit(Field,(0,300))
            game_window.blit(Field,(400,300))
            game_window.blit(Field,(800,300))
            game_window.blit(Leg,(leg_x_1,leg_y_1))
            #Health bar depleates
            pygame.draw.line(game_window, RED, (50,55),(health_bar_x, health_bar_y), 41)
            health_bar_x=health_bar_x-health_bar_decrease
            game_window.blit(health_bar,(0,0))
            #Humans freeze
            game_window.blit(hunter_1,(hunter_1_x,hunter_1_y))
            game_window.blit(Human_2,(Human_2_x,Human_2_y))
            Human_speed_x=0
            Human_speed_y=0
            Human_2_speed_x=0
            Human_2_speed_y=0
            game_window.blit(Leg,(leg_x_2,leg_y_2))
            game_window.blit(Vampire,(Vampire_x,Vampire_y))
            game_window.blit(tree,(400,300))
            game_window.blit(tree,(0,300))
            #Transport the moon and sun far away
            sun_x=-10000
            moon_x=-10000
            #Make speed of sun and moon 0
            sun_speed_x=0
            moon_speed_y=0

            Vampire_speed=0
            death_counter=death_counter+5
            health_bar_decrease=health_bar_decrease+3
            Leg=pygame.image.load("invisable1.png")
            #Sky turns grey
            SKY_COLOUR=CLOUDY_SKY
            #Prints the user's score in number of days
            day_text = font.render("You Survived for "+str(day)+" days!",1,YELLOW)
            #Location of text
            game_window.blit(day_text,(390,200))
            #Shows creators high score
            high_score = font.render("The creators high score was 8 days!",1,YELLOW)
            #Location of text
            game_window.blit(high_score,(350,220))

            #End of game title
            game_window.blit(gane_over,(WIDTH/2-150,HEIGHT/2-250))
            if health_bar_x<=30:
                health_bar_x=35
            #Death-dust animation for dead vampire
            delay=100
            if death_counter==5:
                Vampire=pygame.image.load("Vampire_Dust_-1.png")
                death_counter=death_counter+5
            elif death_counter==10:
                Vampire=pygame.image.load("Vampire_Dust_0.png")
                death_counter=death_counter+5
            elif death_counter==15:
                Vampire=pygame.image.load("Vampire_Dust_1.png")
                death_counter=death_counter+5
            elif death_counter==20:
                Vampire=pygame.image.load("Vampire_Dust_2.png")
                death_counter=death_counter+5
            elif death_counter==25:
                Vampire=pygame.image.load("Vampire_Dust_3.png")
                death_counter=death_counter+5
            elif death_counter==30:
                Vampire=pygame.image.load("Vampire_Dust_4.png")
                death_counter=death_counter+5
            elif death_counter==35:
                Vampire=pygame.image.load("Vampire_Dust_5.png")
                death_counter=death_counter+5
            elif death_counter==40:
                Vampire=pygame.image.load("Vampire_Dust_6.png")
                death_counter=death_counter+5
            elif death_counter==45:
                Vampire=pygame.image.load("Vampire_Dust_7.png")
                death_counter=death_counter+5
            else:
                Vampire=pygame.image.load("Vampire_Dust_8.png")
                death_counter=death_counter+5


    #Update the game window
    pygame.display.update()
    #Delay by 10 miliseconds
    pygame.time.delay(delay)

















