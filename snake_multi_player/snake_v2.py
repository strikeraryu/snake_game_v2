import pygame
import random
import math
pygame.init()

game_run = True
snk_score = 0
snk2_score = 0
# __GAME__ Snake
while game_run:
    scl = 15
    size = scl
    border = 1

    digit = [pygame.image.load('digit/0.png'), pygame.image.load('digit/1.png'), pygame.image.load('digit/2.png'), pygame.image.load('digit/3.png'), pygame.image.load('digit/4.png'),
             pygame.image.load('digit/5.png'), pygame.image.load('digit/6.png'), pygame.image.load('digit/7.png'), pygame.image.load('digit/8.png'), pygame.image.load('digit/9.png')]

    # define window witth size and name "SNAKE GAME"
    win = pygame.display.set_mode((size * 40, size * 40))
    pygame.display.set_caption("SNAKE GAME")
    clock = pygame.time.Clock()

# to calculate distance between two point
    def distance(x, y, x1, y1):
        ret = math.sqrt((x-x1)**2+(y-y1)**2)
        return ret

    def score_print(score, x, y):
        number = []
        if score == 0:
            number.append(0)
        else:
            while score > 0:
                number.append(score % 10)
                score //= 10
        for i in range(len(number)):
            win.blit(digit[number[i]], (x, y))
            x -= 20

    class snake(object):
        def __init__(self, x, y, height, width, colour):
            self.x = x
            self.y = y
            self.height = height
            self.width = width
            self.vel = scl
            self.dir = "stop"
            self.tail_size = 0
            self.tail_x = []
            self.tail_y = []
            self.colour = colour

# To check fruit is eaten

        def eat(self):
            dist = distance(self.x, self.y, fruit_x, fruit_y)
            if dist < scl:
                fruit_gen()
                self.tail_size += 1
                self.tail_x.insert(0, self.x)
                self.tail_y.insert(0, self.y)

# To draw the snake and the fruit
        def move(self):
            if self.tail_size >= 1:
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

        def draw(self):
            self.eat()
            if allow:
                pygame.draw.rect(win, self.colour, (self.x + border, self.y +
                                                    border, self.width - border, self.height - border))
            for i in range(self.tail_size):
                if allow:
                    pygame.draw.rect(
                        win, (self.colour[0]//2, self.colour[1]//2, self.colour[2]//2), (self.tail_x[i] + border, self.tail_y[i] + border, self.width - border, self.height - border))

        def die(self):
            if self.y < 0 or self.y > size*40-self.height or self.x < 0 or self.x > size*40-self.width:
               return True
            for i in range(self.tail_size):
                if self.x == self.tail_x[i] and self.y == self.tail_y[i]:
                    return True

# to genrate fruit
    def fruit_gen():
        global fruit_x
        global fruit_y
        fruit_x = random.randrange(3, 39)
        fruit_y = random.randrange(3, 39)
        fruit_x *= scl
        fruit_y *= scl

# to draw the elements
    def redrawgamewindow():
        global snk_score,snk2_score,run,allow

        if allow:
            win.fill((0, 0, 0))
            snk.move()
            if snk.die():
                snk2_score += 1
                pygame.time.delay(500)
                win.fill((snk2.colour))
                pygame.display.update()
                pygame.time.delay(1000)
                run = False
                snk.allow = False
                snk2.allow = False
            snk.draw()

            snk2.move()
            if snk2.die():
                snk_score += 1
                pygame.time.delay(500)
                win.fill((snk.colour))
                pygame.display.update()
                pygame.time.delay(1000)
                run = False
                snk.allow = False
                snk2.allow = False
            snk2.draw()

            if run:
                pygame.draw.rect(win, (255, 0, 0), (fruit_x + border,
                                                    fruit_y + border, size - border, size - border))

                score_print(snk_score, scl*36, 3)
                score_print(snk2_score, scl*3, 3)
            pygame.display.update()

# main loop
    run = True
    allow = True
    snk = snake(scl * 30, scl * 20, size, size, (0, 60, 250))
    snk2 = snake(scl * 10, scl * 20, size, size, (0, 250, 0))
    fruit_x = scl * int(100/scl)
    fruit_y = scl * int(350/scl)
    while run:
        clock.tick(10)

# To check the events done in the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

# To take the inputs of keys pressed
        keys = pygame.key.get_pressed()
# To move the snake
        if keys[pygame.K_UP] and snk.dir != "down":
            snk.dir = "up"
        elif keys[pygame.K_DOWN] and snk.dir != "up":
            snk.dir = "down"
        elif keys[pygame.K_LEFT] and snk.dir != "right":
            snk.dir = "left"
        elif keys[pygame.K_RIGHT] and snk.dir != "left":
            snk.dir = "right"

        if keys[pygame.K_w] and snk2.dir != "down":
            snk2.dir = "up"
        elif keys[pygame.K_s] and snk2.dir != "up":
            snk2.dir = "down"
        elif keys[pygame.K_a] and snk2.dir != "right":
            snk2.dir = "left"
        elif keys[pygame.K_d] and snk2.dir != "left":
            snk2.dir = "right"

        if distance(snk.x, snk.y, snk2.x, snk2.y) < scl:
            if snk.tail_size > snk2.tail_size:
                snk_score += 1
                pygame.time.delay(500)
                win.fill((snk.colour))
                pygame.display.update()
                pygame.time.delay(1000)
                run = False
                snk.allow = False
                snk2.allow = False

            elif snk2.tail_size > snk.tail_size:
                snk2_score += 1
                pygame.time.delay(500)
                win.fill((snk2.colour))
                pygame.display.update()
                pygame.time.delay(1000)
                run = False
                snk.allow = False
                snk2.allow = False

            else:
                pygame.time.delay(500)
                win.fill((255, 255, 255))
                pygame.display.update()
                pygame.time.delay(1000)
                run = False
                snk.allow = False
                snk2.allow = False

        for i in range(snk.tail_size):
            if distance(snk2.x, snk2.y, snk.tail_x[i], snk.tail_y[i]) < scl:
                snk_score += 1
                pygame.time.delay(500)
                win.fill((snk.colour))
                pygame.display.update()
                pygame.time.delay(1000)
                run = False
                snk.allow = False
                snk2.allow = False

        for i in range(snk2.tail_size):
            if distance(snk.x, snk.y, snk2.tail_x[i], snk2.tail_y[i]) < scl:
                snk2_score += 1
                pygame.time.delay(500)
                win.fill((snk2.colour))
                pygame.display.update()
                pygame.time.delay(1000)
                run = False
                snk.allow = False
                snk2.allow = False

        if run:
            redrawgamewindow()

# to quit pyagame
