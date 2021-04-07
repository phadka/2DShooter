import sys, pygame, random
from bullet import *
from enemy import *
pygame.init()
pygame.display.set_caption("2D-Shooter")
pygame.display.set_icon(pygame.image.load("gun.png"))

size = width, height = 1200, 800
rot = 0.0
cooldown = 0
score = 0
game_over = False

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

gun_img = pygame.transform.smoothscale(pygame.image.load("gun.png").convert(), (80, 80))
gunrect = gun_img.get_rect()
gunrect.center = 600, 400

bullet_img = pygame.image.load("bullet.png").convert()
bullets = []

enemy_img = pygame.transform.smoothscale(pygame.image.load("enemy.png").convert(), (60, 60))
enemies = []

background_img = pygame.transform.smoothscale(pygame.image.load("background.jpg").convert(), (1200, 800))

score_font = pygame.font.SysFont("arial", 25)
game_over_font = pygame.font.SysFont("arial", 40)

def draw_gun():
    old_center = gunrect.center
    new_image = pygame.transform.rotate(gun_img, rot)
    rect = new_image.get_rect()
    rect.center = old_center
    screen.blit(new_image, rect)

def rotate_gun():
    global rot
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        rot = rot + 3.0
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        rot = rot - 3.0

def shoot():
    global cooldown
    cooldown = cooldown - 1
    for bul in bullets:
        bul.update()
    if pygame.key.get_pressed()[pygame.K_SPACE] and cooldown < 0:
        new_bullet = Bullet(rot)
        bullets.append(new_bullet)
        cooldown = 20

def draw_bullets():
    for bul in bullets:
        new_image = pygame.transform.rotate(bullet_img, bul.rot)
        rect = new_image.get_rect()
        rect.center = bul.x, bul.y
        screen.blit(new_image, rect)

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def spaw_enemies():
    for en in enemies:
        en.update()
    if random.random() * 60 < 1:
        new_enemy = Enemy()
        enemies.append(new_enemy)

def draw_enemies():
    for en in enemies:
        new_image = pygame.transform.rotate(enemy_img, en.rot)
        rect = new_image.get_rect()
        rect.center = en.x, en.y
        screen.blit(new_image, rect)

def check_for_hits():
    for bul in bullets:
        if bul.x > 1200 or bul.x < 0 or bul.y < 0 or bul.y > 800:
            bullets.remove(bul)
            continue
        for en in enemies:
            if bul.x > en.x - 30 and bul.x < en.x + 30 and bul.y > en.y - 30 and bul.y < en.y + 30:
                global score
                score += 1
                enemies.remove(en)
                bullets.remove(bul)
                break

def check_if_game_over():
    for en in enemies:
        if en.x > 550 and en.x < 650 and en.y > 350 and en.y < 450:
            global game_over
            game_over = True

def draw_score():
    text = score_font.render("Punktzahl: " + str(score), True, (255, 255, 255))
    rect = text.get_rect()
    rect.center = 600, 100
    screen.blit(text, rect)

def draw_endscreen():
    score_text = score_font.render("Punktzahl: " + str(score), True, (255, 255, 255))
    game_over_text = game_over_font.render("Spiel Vorbei!", True, (255, 255, 255))
    score_rect = score_text.get_rect()
    game_over_rect = game_over_text.get_rect()
    score_rect.center = 600, 500
    game_over_rect.center = 600, 300
    screen.blit(score_text, score_rect)
    screen.blit(game_over_text, game_over_rect)

def draw_background():
    screen.blit(background_img, pygame.Rect(0, 0, 1200, 800))

while True:
    screen.fill((255, 255, 255))
    handle_events()
    if not game_over:
        rotate_gun()
        shoot()
        spaw_enemies()
        check_for_hits()
        check_if_game_over()
        draw_background()
        draw_gun()
        draw_bullets()
        draw_enemies()
        draw_score()
    else:
        draw_background()
        draw_endscreen()
    pygame.display.flip()
    clock.tick(60)
