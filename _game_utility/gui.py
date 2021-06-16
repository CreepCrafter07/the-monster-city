import pygame
#from common import InventoryItem

pygame.init()

MENU_OUTLINE_RECT = pygame.Rect(10, 10, 250, 450)
MENU_INNER_RECT = pygame.Rect(15, 15, 240, 440)

FONT2 = pygame.font.SysFont("Fixedsys", 24)

font_height = FONT2.get_linesize()

def drawMenu(surface, inventory):
    pygame.draw.rect(surface, (255, 255, 255), MENU_OUTLINE_RECT)
    pygame.draw.rect(surface, (0, 0, 0), MENU_INNER_RECT)
    i = 0
    for item in inventory:
        toRender = item.title
        toRenderY = 20 + (i * (font_height + 5))
        surface.blit(FONT2.render(toRender, True, (255, 255, 255)), (20, toRenderY))
        i += 1
