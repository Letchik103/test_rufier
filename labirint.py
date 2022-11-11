
from pygame import *
 

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (55, 55))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
   def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
 

class Enemy(GameSprite):
    side = "left"
    def update(self):
        if self.rect.x <= 470:
            self.side = "right"
        if self.rect.x >= win_width - 85:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
 
class Wall(sprite.Sprite):
   def __init__(self, color_1, color_2, color_3, wall_width, wall_height, wall_x, wall_y):
       super().__init__()
       self.color_1 = color_1
       self.color_2 = color_2
       self.color_3 = color_3
       self.width = wall_width
       self.height = wall_height
       self.image = Surface((self.width, self.height))
       self.image.fill((color_1, color_2, color_3))
       self.rect = self.image.get_rect()
       self.rect.x = wall_x
       self.rect.y = wall_y
   def draw_wall(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
       draw.rect(window, (self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.width, self.height))
win_width = 700
win_height = 700
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("galaxy_1.jpg"), (win_width, win_height))
 
wall1 = Wall(0, 60, 30, 30, 500, 120, 270)
wall2 = Wall(0, 60, 30, 360, 30, 120, 250)
wall3 = Wall(0, 60, 30, 30, 140, 300, 120)
wall4 = Wall(0, 60, 30, 30, 300, 450, 250)
wall5 = Wall(0, 60, 30, 10, 700, 0, 0)
wall6 = Wall(0, 60, 30, 700, 10, 0, 0)
wall7 = Wall(0, 60, 30, 10, 700, 690, 0)
wall8 = Wall(0, 60, 30, 700, 10, 0, 690)
wall9 = Wall(0, 60, 30, 30, 140, 500, 0)
wall10 = Wall(0, 60, 30, 200, 30, 0, 105)
wall11 = Wall(0, 60, 30, 200, 30, 280, 550)
wall12 = Wall(0, 60, 30, 200, 30, 150, 400)
walls = sprite.Group()
walls.add(wall1)
walls.add(wall2)
walls.add(wall3)
walls.add(wall4)
walls.add(wall5)
walls.add(wall6)
walls.add(wall7)
walls.add(wall8)
walls.add(wall9)
walls.add(wall10)
walls.add(wall11)
walls.add(wall12)
konec = GameSprite('cup.png',160,300,0)
ufo = Player('spaceship_1.png',30,600,4)
enemy = Enemy('ufo_4.png',600,550,2)
 
 
game = True
finish = False
clock = time.Clock()
FPS = 60
 
font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))
 
mixer.init()
mixer.music.load('fon.ogg')
mixer.music.play()
 
otkr = mixer.Sound('otkr.ogg')
stena = mixer.Sound('stena.ogg')
vrag = mixer.Sound('vrag.ogg') 
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
  
    if finish != True:
        window.blit(background,(0, 0))
        ufo.update()
        enemy.update()
      
        ufo.reset()
        enemy.reset()
        konec.reset()
 
        walls.draw(window)

        if sprite.collide_rect(ufo, enemy):
           finish = True
           mixer.music.load('vrag.ogg')
           window.blit(lose, (200, 300))
           vrag.play()
           
        if sprite.spritecollide(ufo, walls, False):
            finish = True
            mixer.music.load('stena.ogg')
            mixer.music.play()
            window.blit(lose, (200, 300))
            
        if sprite.collide_rect(ufo, konec):
           finish = True
           mixer.music.load('otkr.ogg')
           window.blit(win, (200, 300))
           otkr.play()
           
    display.update()
    clock.tick(FPS)
