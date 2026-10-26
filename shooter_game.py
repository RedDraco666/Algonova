from pygame import *
from random import randint

win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption('Space Shooter')
background = transform.scale(image.load('galaxy.jpg'), (win_width, win_height))

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
mixer.music.set_volume(0.1)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys [K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys [K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet('bullet.png',self.rect.centerx -30, self.rect.top, 15)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 600:
            self.rect.x = randint(80, 700)
            self.rect.y = 0

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

player = Player('rocket.png', 0, 420, 4)

bullets = sprite.Group()

enemies = sprite.Group()
for i in range(5):
    enemy = Enemy('ufo.png', randint(80, 700), -40, randint(1,5))
    asteroid = Enemy('asteroid.png', randint(80, 700), -40, randint(1,5))
    enemies.add(asteroid)
    enemies.add(enemy)

clock = time.Clock()

health  = 10
score = 0
font.init()
text = font.Font(None, 40)

text_win = text.render('You win!', 1, (255, 255, 255))
text_lose = text.render('You lose!', 1, (255, 255, 255))

game_over = False

while True:
    for e in event.get():
        if e.type == QUIT:
            exit()
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()

    if game_over == False:

        window.blit(background, (0,0))
        player.reset()
        player.update()
        enemies.draw(window)
        enemies.update()
        bullets.draw(window)
        bullets.update()

        text_score = text.render('Score: ' + str(score), 1, (255, 255, 255))
        text_health = text.render('Health: ' + str(health), 1, (255, 255, 255))

        window.blit(text_score, (10, 10))
        window.blit(text_health, (10, 50))

        collides = sprite.groupcollide(enemies, bullets, True, True)
        for c in collides:
            score += 1
            random_choice = randint(0,1)
            if random_choice == 0:
                asteroid = Enemy('asteroid.png', randint(80, 700), -40, randint(1,5))
                enemies.add(asteroid)
            else:
                ufo = Enemy('ufo.png', randint(80, 700), -40, randint(1,5))
                enemies.add(ufo)

        health_collides = sprite.spritecollide(player, enemies, True)
        for c in health_collides:
            health -= 1
            random_choice = randint(0,1)
            if random_choice == 0:
                asteroid = Enemy('asteroid.png', randint(80, 700), -40, randint(1,5))
                enemies.add(asteroid)
            else:
                ufo = Enemy('ufo.png', randint(80, 700), -40, randint(1,5))
                enemies.add(ufo)

        if health <= 0:
            window.blit(text_lose, (250, 250))
            game_over = True

        if score >= 21:
            window.blit(text_win, (250, 250))
            game_over = True

    display.update()
    clock.tick(60)


