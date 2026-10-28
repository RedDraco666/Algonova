from pygame import *

win_width = 500
win_height = 700

window = display.set_mode((win_width, win_height))
display.set_caption('Ping Pong Game')
background = transform.scale(image.load('Ping Pong\\Background.jpg   '), (win_width, win_height))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

player_top = GameSprite('Ping Pong\\platform.png', 200, 10, 4, 150, 50)
player_bottom = GameSprite('Ping Pong\\platform.png', 200, 640, 4, 150, 50)
ball = GameSprite('Ping Pong\\bola.png', 200, 350, 3, 50, 50)

clock = time.Clock()

while True:
    for e in event.get():
        if e.type == QUIT:
            exit()
    window.blit(background, (0,0))
    player_top.reset()
    player_bottom.reset()
    ball.reset()

    ball.rect.x += ball.speed
    ball.rect.y += ball.speed

    display.update()
    clock.tick(60)