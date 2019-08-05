import pygame
import time
import random

pygame.init() #Instantiate all the module in pygame.
crash_sound = pygame.mixer.Sound("Crash.wav")
pygame.mixer.music.load("Race_Car.wav")

display_width = 800    #width of the window
display_height = 500   #height of the window

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)

bright_red =(255,0,0)
bright_green =(0,255,0)

block_color = (53,115,255)
car_width = 73



gameDisplay = pygame.display.set_mode((display_width,display_height))  #Height and Weight

pygame.display.set_caption("RACEY")                                #Caption on the Window

clock = pygame.time.Clock()                                             

carImg = pygame.image.load('racecar.png')                               #LOAD THE IMAGE OF THE CAR
pygame.display.set_icon(carImg)
pause = False

def things_dodged(count):                   #This function basically put a score on the top left on the screen.
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count) , True,black)
    gameDisplay.blit(text,(0,0))
    
def things(thingx,thingy ,thingw,thingh,color):                                #it basically draws the obstacle.
    pygame.draw.rect(gameDisplay,block_color,[thingx,thingy,thingw,thingh])
    
#To display the car location.
def car(x,y):
     gameDisplay.blit(carImg, (x,y))   #to display the car in hgiven coordinates

def text_objects(text,font):
    textSurface = font.render(text,True,black)
    return textSurface , textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf , TextRect)

    pygame.display.update()
    time.sleep(2)

    game_loop()


def button(msg ,x,y,w,h,i,a,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    #print(click)

        #print(mouse)

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,a,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
##            if action == "play":
##                game_loop()
##
##            elif action == "quit":
##                pygame.quit()
##                quit()
            
            
    else:
        pygame.draw.rect(gameDisplay,i,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg,smallText)
    textRect.center = ((x+(w/2),y+(h/2)))
    gameDisplay.blit(textSurf ,textRect)

    
def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False

    
def paused():

    pygame.mixer.music.pause()

    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #gameDisplay.fill(white)
        

        button("Continue",150,400,100,50,green,bright_green,unpause)
        button("Quit",550,400,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)  

def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    message_display('DISHOOM')


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("RACE 4", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf , TextRect)
          
        
        button("GO!",150,400,100,50,green,bright_green,game_loop)
        button("QUIT!!",550,400,100,50,red,bright_red,quitgame)
        

        #print(mouse)



        #pygame.draw.rect(gameDisplay,red,(550,400,100,50))

        
        pygame.display.update()
        clock.tick(15)
            



def game_loop():
    global pause
    pygame.mixer.music.play(-1)
    
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_chnge = 0    


    thing_startx = random.randrange(0,display_width)            #to display the obstacle randomly
    thing_starty = -600
    thing_speed = 7                                          #speed of the obstaccle
    thing_width = 100
    thing_height = 100
    

    dodged = 0
    
    gameExit = False

    while not gameExit:

        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:            #if any key is pressed or not.
                if event.key == pygame.K_LEFT:          #if Left key is pressed.
                    x_chnge =-5
                elif event.key == pygame.K_RIGHT:       #IF Right key is pressed.
                    x_chnge =5
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_chnge = 0


        x += x_chnge
            
        gameDisplay.fill(white)
        #things(thingx ,thingw,thingh,color)
        things(thing_startx, thing_starty,thing_width,thing_height,black)

        thing_starty += thing_speed
        
        car(x,y)
        things_dodged(dodged)
        
        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged *1.2)  #to make it more interesting we are making the obstacle little bigger.

            
        if  y < thing_starty + thing_height:
            print('Y_crossOver')

            if x > thing_startx and x < thing_startx + thing_width  or x+car_width > thing_startx and x + car_width < thing_startx + car_width:
                print('X_crossOver')
                crash()
                
        pygame.display.update() #update the whole screen

        clock.tick(60) # fps

game_intro()
game_loop()
pygame.quit()
quit()
