import pygame
import random
import math
pygame.init()

game_run = True
#__GAME__ Snake

while game_run:
    scl = 12
    size = scl
    border = 1

#define window witth size and name "SNAKE GAME"
    win = pygame.display.set_mode((size * 40, size * 40))
    pygame.display.set_caption("SNAKE GAME")
    clock = pygame.time.Clock()

#to calculate distance between two point
    def distance(x, y, x1 ,y1):
        ret = math.sqrt((x-x1)**2+(y-y1)**2)
        return ret


    class snake(object):
        def __init__(self, x, y, height, width):
            self.x = x
            self.y = y
            self.height = height
            self.width = width
            self.vel = scl
            self.dir = "stop"
            self.tail_size = 0
            self.tail_x = []
            self.tail_y = []

#To check fruit is eaten
            
        def eat(self):
            dist = distance(self.x, self.y, fruit_x, fruit_y)
            if dist < scl:
                fruit_gen()
                self.tail_size+=1
                self.tail_x.insert(0,self.x)
                self.tail_y.insert(0,self.y)

#To draw the snake and the fruit
        def draw(self,win):
            global allow
            global run

            if self.tail_size>=1:
                self.tail_x.pop(0)
                self.tail_y.pop(0)
                self.tail_x.append(self.x)
                self.tail_y.append(self.y)
            if self.dir == "up":
                self.y -= self.vel
            elif self.dir == "down":
                self.y += self.vel
            elif self.dir == "left":
                self.x -= self.vel
            elif self.dir == "right":
                self.x += self.vel
            if self.y<0 or self.y>size*40-self.height or self.x<0 or self.x>size*40-self.width :
                run = False
                allow = False
                pygame.time.delay(500) 
            for i in range(self.tail_size):
                if self.x==self.tail_x[i] and self.y == self.tail_y[i]:
                    run = False
                    allow = False
                    pygame.time.delay(500)
            self.eat()
            if allow:
                pygame.draw.rect(win, (0, 255, 0), (self.x + border, self.y + border, self.width - border, self.height - border))
            x=250
            c=10
            for i in range(self.tail_size):
                x -= c
                if x == 80 or x == 250:
                    c *= -1
                if allow:
                    pygame.draw.rect(win, (0, x, 0), (self.tail_x[i] + border, self.tail_y[i] + border, self.width - border, self.height - border))

#to genrate fruit
    def fruit_gen():
        global fruit_x
        global fruit_y
        fruit_x = random.randrange(1,39)
        fruit_y = random.randrange(1,39)
        fruit_x *= scl
        fruit_y *= scl

#to draw the elements
    def redrawgamewindow():
        if allow:
            win.fill((0, 0, 0))
            snk.draw(win)
            pygame.draw.rect(win, (255, 0, 0), (fruit_x + border, fruit_y + border, size - border, size - border))
            pygame.display.update()

#main loop
    run = True
    allow = True
    snk = snake(scl * 20, scl * 20, size, size)
    fruit_x = scl * int(100/scl)
    fruit_y = scl * int(350/scl)
    while run:
        clock.tick(10)
        
#To check the events done in the window  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
#To take the inputs of keys pressed
        keys = pygame.key.get_pressed()
#To move the snake
        if keys[pygame.K_UP] and snk.dir != "down":
            snk.dir = "up"
        elif keys[pygame.K_DOWN] and snk.dir != "up":
            snk.dir = "down"
        elif keys[pygame.K_LEFT] and snk.dir != "right":
            snk.dir = "left"
        elif keys[pygame.K_RIGHT] and snk.dir != "left":
            snk.dir = "right"

        redrawgamewindow()
        
#to quit pyagame
                     
