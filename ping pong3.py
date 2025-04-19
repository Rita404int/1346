

from pygame import *

wind =display.set_mode((700 , 500))
fon = (200,225,235)
wind.fill(fon)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_height ,player_width,  player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_height,player_width))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        wind.blit(self.image, (self.rect.x , self.rect.y))

class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys[K_s] and self.rect.y < 495:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed() 
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys[K_DOWN] and self.rect.y < 495:
            self.rect.y += self.speed 

game = True
finish= False
clock = time.Clock()
FPS = 60

p2 = Player("nlo1.jpg",15,250,80,100,70)
p1 = Player("nlo2.jpg",675,250,80,100,70)
m = GameSprite("images.jpg",200,200,4,50,50)

font.init()
font1 = font.Font(None, 35)
lose1 = font1.render("Player 1 lose!",True,(200,0,0))
lose = font1.render("Player 2 lose!",True,(200,0,0))

speed_x =3
speed_y =3

while game:
    for e in event.get():
        if e.type ==  QUIT:
            game = False
    if finish != True:
        wind.fill(fon)

        p1.update1()
        p2.update2()
        m.rect.y += speed_y 
        m.rect.x += speed_x

        if  sprite.collide_rect(p1,m) or sprite.collide_rect(p2,m):
            speed_x *= -1
            speed_y *= -1

        if m.rect.y > 460 or m.rect.y < 0:
            speed_y *= - 1

        if m.rect.x  < 0 :
            finish = True
            wind.blit(lose1, (200, 200))

        if  m.rect.x > 700:
            finish = True
            wind.blit(lose, (200, 200))

        p1.reset()
        p2.reset()
        m.reset()

    display.update()
    clock.tick(FPS)