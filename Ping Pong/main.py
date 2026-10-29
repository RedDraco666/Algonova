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

font.init()
text = font.Font(None, 40)

text_top = text.render('Player top wins!', 1, (255, 255, 255))
text_bottom = text.render('Player bottom wins!', 1, (255, 255, 255))

score_top = 0
score_bottom = 0

gameover = False

while True:
    for e in event.get():
        if e.type == QUIT:
            exit()
    if not gameover:
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

        if ball.rect.y < 0:
            ball.rect.x = 200
            ball.rect.y = 350
            score_bottom += 1

        if ball.rect.y > win_height - 50:
            ball.rect.x = 200
            ball.rect.y = 350
            score_top += 1

        if sprite.collide_rect(player_top, ball) or sprite.collide_rect(player_bottom, ball):
            speed_y *= -1

        text_top_score = text.render('Score: ' + str(score_top), 1, (255, 255, 255))
        text_bottom_score = text.render('Score: ' + str(score_bottom), 1, (255, 255, 255))
        window.blit(text_top_score, (10, 10))
        window.blit(text_bottom_score, (10, win_height - 40))

        if score_top >= 11:
            window.blit(text_top, (100, 300))
            display.update()
            gameover = True

        if score_bottom >= 11:
            window.blit(text_bottom, (100, 300))
            display.update()
            gameover = True

    display.update()
    fps.tick(60)