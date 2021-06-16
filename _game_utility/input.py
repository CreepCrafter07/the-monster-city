from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN

def getKeyMovement(keys, speed):
    moveX, moveY = 0, 0
    if keys[K_LEFT]:
        moveX -= speed

    if keys[K_RIGHT]:
        moveX += speed

    if keys[K_UP]:
        moveY -= speed

    if keys[K_DOWN]:
        moveY += speed

    return (moveX, moveY)
