import pygame
pygame.init()

white = (255,255,255)
black = (0,0,0)


red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)


gameDisplay = pygame.display.set_mode((800,600))

gameDisplay.fill(white)

pixAr = pygame.PixelArray(gameDisplay) #pixel
pixAr[10][20] = green

pygame.draw.line(gameDisplay,blue,(100,200),(300,450),5)
pygame.draw.rect(gameDisplay,red,(400,400,50,25))
pygame.draw.circle(gameDisplay,black,(150,150),75)
pygame.draw.polygon(gameDisplay,green,((26,75),(79,125),(528,658)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
