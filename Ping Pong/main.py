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

class Player(GameSprite):
    def update_top(self):
        keys = key.get_pressed()
        if keys [K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys [K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

    def update_bottom(self):
        keys = key.get_pressed()
        if keys [K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys [K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

player_top = Player('Ping Pong\\platform.png', 200, 10, 4, 150, 50)
player_bottom = Player('Ping Pong\\platform.png', 200, 640, 4, 150, 50)
ball = GameSprite('Ping Pong\\bola.png', 200, 350, 3, 50, 50)

fps = time.Clock()

speed_x = 3
speed_y = 3

while True:
    for e in event.get():
        if e.type == QUIT:
            exit()
    window.blit(background, (0,0))
    player_top.update_top()
    player_top.reset()
    player_bottom.update_bottom()
    player_bottom.reset()
    ball.reset()

    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if ball.rect.x < 0 or ball.rect.x > win_width - 50:
        speed_x *= -1

    if sprite.collide_rect(player_top, ball) or sprite.collide_rect(player_bottom, ball):
        speed_y *= -1

    display.update()
    fps.tick(60)