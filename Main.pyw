import pygame, sys, random
from _game_utility.rooms import ROOM_ID_LIST
from _game_utility.rooms import ROOM_IMAGES
from _game_utility.rooms import ROOM_CONFIGS
from _game_utility.input import getKeyMovement
from _game_utility.common import InventoryItem
from _game_utility.gui import drawMenu

#from _game_utility.input import playerInteract
#from _game_utility.common import gameLoad

pygame.init()

screen = pygame.display.set_mode((400, 300), pygame.NOFRAME)

screen.blit(pygame.transform.smoothscale(pygame.image.load("assets/startbg.png"), (400, 300)), (0, 0))

pygame.display.update()

pygame.time.wait(3000)

pygame.quit()


pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("The Monster City")

pygame.display.set_icon(pygame.image.load("assets/icon.png"))


def terminate():
    pygame.quit()
    sys.exit()


clock = pygame.time.Clock()


FONT2 = pygame.font.Font("assets/font.ttf", 24)

pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

pygame.time.wait(100)

if random.choice((True, False)):
    pygame.mixer.music.load("assets/sounds/music_bg_game.mp3")

else:
    pygame.mixer.music.load("assets/sounds/music_bg_game2.mp3")

pygame.mixer.music.play(-1, 0.0)

currentRoomIndex = 0

currentRoom = ROOM_CONFIGS[currentRoomIndex]

currentRoomImage = ROOM_IMAGES[currentRoomIndex]

playerImages = {}

playerSpritesheet = pygame.image.load("assets/player.png")

playerImages["story"] = playerSpritesheet.subsurface((0, 0, 32, 32))

playerImages["dead"] = playerSpritesheet.subsurface((32, 32, 32, 32))

playerImages["red"] = playerSpritesheet.subsurface((32, 0, 32, 32))

playerImages["blue"] = playerSpritesheet.subsurface((0, 32, 32, 32))

currentPlayerImage = playerImages["story"]

playerRect = currentPlayerImage.get_rect()

playerRect.topleft = (130, 250)

pygame.key.set_repeat(1, 30)

PLAYER_SPEED = 3

SCREENRECT = pygame.Rect(0, 0, 800, 600)

quitting = False

quit_time = 0

QUITSURF = FONT2.render("- Quitting game...", False, (255, 255, 255))

quit_alpha = 0

quit_alpha_dir = -25

current_volume = 1

volume_before_mute = 0

intro_step = 0

INTRO_IMAGES = [pygame.image.load("assets/intro/intro1.png"), pygame.image.load("assets/intro/intro2.png")]

inventory = [InventoryItem("Test Item"), InventoryItem("Test Item 2"), InventoryItem("Test Item 3")]

menu_open = False


while True:
    screen.fill((0, 0, 0))
    playerRect.clamp_ip(SCREENRECT)
    for door in currentRoom["doors"]:
        if pygame.Rect(door["x"], door["y"], door["w"], door["h"]).colliderect(playerRect):
            currentRoomIndex = door["to"]
            currentRoom = ROOM_CONFIGS[currentRoomIndex]
            currentRoomImage = ROOM_IMAGES[currentRoomIndex]
            if door["w"] > door["h"]:
                if door["y"] == 0:
                    playerRect.y = 580 - (door["h"] * 2)

                else:
                    playerRect.y = (door["h"] + 5)

            else:
                if door["x"] == 0:
                    playerRect.x = 780 - (door["w"] * 2)

                else:
                    playerRect.x = (door["w"] + 5)
                    
            break

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quitting = True
                quit_time += 1
                QUITSURF = FONT2.render("- Quitting game...", False, (255, 255, 255))
                QUITSURF.set_alpha(quit_alpha)
                if quit_time > 100:
                    pygame.quit()
                    sys.exit()

                quit_alpha += quit_alpha_dir
                if (quit_alpha > 255) and (quit_alpha_dir == 25):
                    quit_alpha_dir = -25
                    quit_alpha -= 25

                elif (quit_alpha < 0) and (quit_alpha_dir == -25):
                    quit_alpha_dir = 25
                    quit_alpha += 25

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                quitting = False
                quit_time = 0

            elif event.key == pygame.K_F2:
                current_volume = max(current_volume - 0.1, 0)
                pygame.mixer.music.set_volume(current_volume)

            elif event.key == pygame.K_F3:
                current_volume = min(current_volume + 0.1, 1)
                pygame.mixer.music.set_volume(current_volume)

            elif event.key == pygame.K_F1:
                if current_volume == 0:
                    current_volume = volume_before_mute

                else:
                    volume_before_mute = current_volume
                    current_volume = 0
                
                pygame.mixer.music.set_volume(current_volume)

            elif event.key == pygame.K_RETURN:
                intro_step += 1

            elif event.key == pygame.K_SPACE:
                menu_open = not menu_open

    keys_pressed = pygame.key.get_pressed()

    toMove = getKeyMovement(keys_pressed, PLAYER_SPEED)

    playerRect.x += toMove[0]

    playerRect.y += toMove[1]

    screen.blit(currentRoomImage, (0, 0))
    screen.blit(currentPlayerImage, playerRect)
    if not (intro_step == 2):
        screen.blit(INTRO_IMAGES[intro_step], (0, 0))

    
        
    if quitting:
        screen.blit(QUITSURF.convert_alpha(), (10, 10))

    if menu_open:
        drawMenu(screen, inventory)

    pygame.display.update()
    clock.tick(60)
