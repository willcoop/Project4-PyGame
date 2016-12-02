
#import modles
import pygame
import random
import pygame.mixer

#Background Color
BLACK = (0, 0, 0)

#Snake Colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0,0,255)
white = (255, 255, 255)

#define sizes of sprites
#Olympic Medals
gold = (207,181,59)
silver = (192, 192, 192)
bronze = (185, 125, 65)
olympic_medals = (gold, silver, bronze)



color = input('Choose Snake Color: red, green, or blue. Enter any key for white default')
if color == 'red':
    color = red
elif color == 'green':
    color = green
elif color == 'blue':
    color = blue
else:
    color = white

'''difficulty = input('Choose difficulty level: Easy, Medium, or Hard')
if difficulty == 'Easy':
    tail, segment, food = 5, 5, 5
elif difficulty == "Medium":
    tail, segment, food = 10, 10, 10
elif difficulty == "Hard":
    tail, segment, food = 15, 15, 15'''

'''color = WHITE'''
tail, segment, food = 10, 10, 10
change_amount = tail
go = change_amount





class Main:
#create Snake
    def __init__(self, surface):
        self.surface = surface

        self.x = surface.get_width() / 2
        self.y = surface.get_height() / 2
    
        self.length = tail
        self.max = tail

        self.x_change = go
        self.y_change = 0

        self.size = []
        self.head = None
        self.over = False

        self.color = color

    def event(self, event):
   
        if event.key == pygame.K_LEFT:
            self.x_change = -change_amount
            self.y_change = 0
        elif event.key == pygame.K_RIGHT:
            self.x_change = change_amount
            self.y_change = 0
        if event.key == pygame.K_UP:
            self.x_change = 0
            self.y_change = -change_amount
        elif event.key == pygame.K_DOWN:
            self.x_change = 0
            self.y_change = change_amount


    def move(self):
        #Snake movement
        self.x += self.x_change
        self.y += self.y_change
        #what happens if snake touches self
        if (self.x, self.y) in self.size:
            self.over = True

        self.size.insert(0, (self.x, self.y))
        self.head = pygame.Rect(self.x, self.y, segment, segment)
        #how big snake will grow
        if (self.max > self.length):
            self.length += tail
        #growth control, stop from growing too long
        if (len(self.size) > self.max):
            delete = self.size.pop(-1)
            pygame.draw.rect(self.surface, BLACK, (delete[0], delete[1], segment, segment), 0)

        if (len(self.size) > self.length):
            delete = self.size.pop(-1)
            pygame.draw.rect(self.surface, BLACK, (delete[0], delete[1], segment, segment), 0)

    def draw(self):
        #create a piece of snake
        pygame.draw.rect(self.surface, self.color, (self.head))
        x, y = self.size[-1]
        pygame.draw.rect(self.surface, BLACK, (x, y, segment, segment), 0)


    def position(self):
        #where snake is at on screen
        return self.x, self.y

    def eat(self):
        #it snake eats food, it grows
        self.max += tail

class Lunch:
    #create food on screen
    def __init__(self, surface):
        self.surface = surface
        x_cord = random.randint(0, surface.get_width())
        y_cord = random.randint(0, surface.get_height())
        self.x = x_cord
        self.y = y_cord
        #places food randomly
        self.rect = pygame.Rect(self.x, self.y, food, food)
        self.color = random.choice(olympic_medals)

    def position(self):
        #find where food is at
        return self.x, self.y

    def draw(self):
        #draw the apple food
        pygame.draw.rect(self.surface, self.color, (self.rect))

    
    def contact(self, lead):
        #see if snake collided with food
        if lead.colliderect(self):
            return True
        else:
            return False

    def erase(self):
        #erase food that was ate
        pygame.draw.rect(self.surface, BLACK, (self.x, self.y, food, food), 0)


screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption(''''Coop's Crazy Snake Game''')
# Set the title of the window

#make screen
clock = pygame.time.Clock()
score = 0
pygame.mixer.init()
'''impact = pygame.mixer.Sound("sounds/impact.wav")'''
#initalize sound for eating

snake = Main(screen)
food1 = Lunch(screen)

#create sprites
running = True
#Game is running


while running:
    snake.move()
    snake.draw()
    food1.draw()
    pygame.init()
    #draw sprites and update

    if snake.over:
        running = False
        #end game is snake hits self
    elif snake.x <= 0 or snake.x >= 805:
        running = False
        #if snake leaves screen boundaries
    elif snake.y <= 0 or snake.y >= 605:
        running = False
    elif food1.contact(snake.head):
        #when snake eats apple, update score and play sound and erase old apple


        if food1.color is bronze:
            score += 1
            snake.eat()
            pygame.draw.rect(screen, BLACK, (5, 10, 200, 50)) 
            myfont = pygame.font.SysFont("times", 30)
            label = myfont.render(("Score: "+str(score)+' Bronze! +1!'), 1, gold)
            screen.blit(label, (10, 10))
            food1.erase()
            food1 = Lunch(screen)

        elif food1.color is silver:
            score =+ 2
            snake.eat()
            pygame.draw.rect(screen, BLACK, (5, 10, 200, 50)) 
            myfont = pygame.font.SysFont("times", 30)
            label = myfont.render(("Score: "+str(score)+' Silver! +2!'), 1, gold)
            screen.blit(label, (10, 10))
            food1.erase()
            food1 = Lunch(screen)

        elif food1.color is gold:
            score +=3
            snake.eat()
            pygame.draw.rect(screen, BLACK, (5, 10, 200, 50)) 
            myfont = pygame.font.SysFont("times", 30)
            label = myfont.render(("Score: "+str(score)+ ' Gold! +3!'), 1, gold)
            screen.blit(label, (10, 10))
            #pygame.display.flip()
            # http://www.pygame.org/docs/tut/tom/games2.html
            food1.erase()
            food1 = Lunch(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            #endgame
        elif event.type == pygame.KEYDOWN:
            snake.event(event)
            #while running, move snake during key presses

    pygame.display.flip()
    clock.tick(30)


