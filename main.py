import pygame
import random
import pygame.mixer

#Background Color
bground = (0, 0, 0)

#Snake (object) colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0,0,255)
white = (255, 255, 255)

#Olympic Medals (food colors)
gold = (207,181,59)
silver = (192, 192, 192)
bronze = (185, 125, 65)
olympic_medals = (gold, silver, bronze)

#Loop Variables
clock = pygame.time.Clock()
score = 0
placement = (10,10)
replacement = (5, 10, 200, 50)
placement = (10,10)
mini_size = [300, 200]
normal_size = [800, 600]
standard = 25
boundary = 10
time = (30)

#User chooses if they want small or normal sizes game (screen size)

game_type = input('''Type 'normal' for normal game with easy, medium, and hard levels. Type 'mini' for miniature game: ''')
if game_type == 'mini':
    tail, segment, food = 5, 5, 5
    dimension = mini_size
    d_w = 300
    d_l = 200
    font_size = standard
    bound = boundary
    color = input('Choose stanimal Color: red, green, or blue. Enter any key for white default')
    if color == 'red':
        color = red
    elif color == 'green':
        color = green
    elif color == 'blue':
        color = blue
    else:
        color = white

#This is the normal size.
#User picks snake color (default = white) and difficulty level (changes snake size)
else:
    dimension = normal_size
    d_w = 800
    d_l = 600
    font_size = standard
    bound = boundary
    color = input('Choose stanimal Color: red, green, or blue. Enter any key for white default')
    if color == 'red':
        color = red
    elif color == 'green':
        color = green
    elif color == 'blue':
        color = blue
    else:
        color = white

    difficulty = input('Choose difficulty level: Easy, Medium, or Hard.')
    if difficulty == 'Easy':
        tail, segment, food = 5, 5, 5
    elif difficulty == "Medium":
        tail, segment, food = 10, 10, 10
    elif difficulty == "Hard":
        tail, segment, food = 15, 15, 15
    else:
        tail, segment, food = 10, 10, 10

change_amount = tail
go = change_amount
start = 40


class Window:

    def __init__(self, width=500, height=480):
        pygame.init() #initialize Pygame
        pygame.display.set_caption('Snake Olympics: Results')


        #setting window size
        self.width = width
        self.height = height

        #creating screen
        self.screen = pygame.display.set_mode((self.width, self.height))

class Main:

    def __init__(self, surface):
        self.surface = surface
        self.size = []
        self.head = None
        self.over = False
        self.x_change = go
        self.y_change = 0
        self.x = start
        self.y = start
        self.length = tail
        self.max = tail
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


    def change(self):
        
        self.x += self.x_change
        self.y += self.y_change
        
        if (self.x, self.y) in self.size:
            self.over = True

        self.size.insert(0, (self.x, self.y))
        self.head = pygame.Rect(self.x, self.y, segment, segment)
        
        if (self.max > self.length):
            self.length += tail
      
        if (len(self.size) > self.max):
            delete = self.size.pop(-1)
            pygame.draw.rect(self.surface, bground, (delete[0], delete[1], segment, segment), 0)

        if (len(self.size) > self.length):
            delete = self.size.pop(-1)
            pygame.draw.rect(self.surface, bground, (delete[0], delete[1], segment, segment), 0)

    def draw(self):
        
        pygame.draw.rect(self.surface, self.color, (self.head))
        x, y = self.size[-1]
        pygame.draw.rect(self.surface, bground, (x, y, segment, segment), 0)


    def locale(self):
       
        return self.x, self.y

    def full(self):
       
        self.max += tail

class Lunch:
    def __init__(self, surface):
        self.surface = surface
        x_cord = random.randint(bound, surface.get_width() - bound)
        y_cord = random.randint(bound, surface.get_height() - bound)
        self.x = x_cord
        self.y = y_cord
        self.rect = pygame.Rect(self.x, self.y, food, food)
        self.color = random.choice(olympic_medals)

    def motion(self):
        self._display_surf.fill((0,0,0))
        self.player.draw(self._display_surf, self._image_surf)
        pygame.display.flip()

    def locale(self):

        return self.x, self.y

    def draw(self):

        pygame.draw.rect(self.surface, self.color, (self.rect))

    def blit(self,screen):

        rect = pygame.Rect(self.x,self.y,standard,standard)
        pygame.draw.rect(screen,self.color,rect)

    def contact(self, lead):

        if lead.colliderect(self):
            return True
        else:
            return False

    def away(self):

        pygame.draw.rect(self.surface, bground, (self.x, self.y, food, food), 0)

#Pygame Initiation
pygame.init()
screen = pygame.display.set_mode(dimension)
pygame.display.set_caption('Snake Olympics')
pygame.mixer.music.load('bgmusic.wav')
pygame.mixer.music.play(loops= -1)

stanimal = Main(screen)
lunch = Lunch(screen)



stanimal_loop = True
while stanimal_loop:

    stanimal.change()
    stanimal.draw()
    lunch.draw()


    if stanimal.over:
        stanimal_loop = False

       
    elif stanimal.x <= 0 or stanimal.x >= d_w - 1:
        stanimal_loop = False
        
    elif stanimal.y <= 0 or stanimal.y >= d_l - 1:
        stanimal_loop = False
    elif lunch.contact(stanimal.head):
   


        if lunch.color is bronze:
            score += 1
            stanimal.full()
            pygame.draw.rect(screen, bground, replacement) 
            myfont = pygame.font.SysFont("times", standard)
            label = myfont.render(("Score: "+str(score)+' Bronze! +1!'), 1, bronze)
            screen.blit(label, placement)
            lunch.away()
            lunch = Lunch(screen)

        elif lunch.color is silver:
            score +=2
            stanimal.full()
            pygame.draw.rect(screen, bground, replacement) 
            myfont = pygame.font.SysFont("times", standard)
            label = myfont.render(("Score: "+str(score)+ ' Silver! +2!'), 1, silver)
            screen.blit(label, placement)
            
            lunch.away()
            lunch = Lunch(screen)



        elif lunch.color is gold:
            score +=3
            stanimal.full()
            pygame.draw.rect(screen, bground, replacement) 
            myfont = pygame.font.SysFont("times", standard)
            label = myfont.render(("Score: "+str(score)+ ' Gold! +3!'), 1, gold)
            screen.blit(label, placement)
           
            lunch.away()
            lunch = Lunch(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
          
        elif event.type == pygame.KEYDOWN:
            stanimal.event(event)
           

    pygame.display.flip()
    clock.tick(time)


pygame.quit()








