import pygame
import sys
import math
pygame.init()

display = pygame.display.set_mode((800,600))
surf = pygame.Surface((800, 600))
clock = pygame.time.Clock()

#Title and Icon
pygame.display.set_caption("Zombinos")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
playerMode = 0
counter = 0

#Player

def drawSprite(num):
   player_walk_image = pygame.image.load("Assets/Characters/prisoner_character.png")
   cropped = pygame.Surface([30, 30], pygame.SRCALPHA, 32)
   cropped = cropped.convert_alpha()
   cropped.blit(player_walk_image, (0, 0), (num*30, 0, 30, 30)) # the images seem to be about 30 pixels apart?
   display.blit(cropped, (400, 300))

class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def main(self, display):
        global playerMode, counter
        counter += 1
        if counter > 10:
            playerMode = (playerMode + 1) % 2
            counter = 0
        drawSprite(playerMode)

#Player Bullets
class PlayerBullet:
    def __init__(self, x, y, mouse_x, mouse_y):
        self.x = x
        self.y = y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.speed = 15
        self.angle = math.atan2(y-mouse_y, x-mouse_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed
    def main(self, display):
        self.x -=int(self.x_vel)
        self.y -= int(self.y_vel)

        if abs(self.x - player.x) < 400 and abs(self.y - player.y) < 300:
          pygame.draw.circle(display, (0,0,0), (self.x, self.y), 5)


player = Player(400, 300, 32, 32)

#Movement
display_scroll = [0,0]

player_bullets = []

#Game Loop
while True:
    
    # RGB
    display.fill((24, 164, 86))

    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player_bullets.append(PlayerBullet(player.x, player.y, mouse_x, mouse_y))


    keys = pygame.key.get_pressed()

    pygame.draw.rect(display, (255,255,255), (100-display_scroll[0], 100-display_scroll[1], 16, 16))

    #movement
    if keys[pygame.K_a]:
        display_scroll[0] -= 5
        for bullet in player_bullets:
            bullet.x += 5

    if keys[pygame.K_d]:
        display_scroll[0] += 5
        for bullet in player_bullets:
            bullet.x -= 5

    if keys[pygame.K_w]:
        display_scroll[1] -= 5
        for bullet in player_bullets:
            bullet.y += 5

    if keys[pygame.K_s]:
        display_scroll[1] += 5
        for bullet in player_bullets:
            bullet.y -= 5

    player.main(display)

    for bullet in player_bullets:
        bullet.main(display)

    clock.tick(60)
    pygame.display.update()