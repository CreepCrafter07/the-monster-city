import pygame, json

ROOM_COUNT = 2
ROOM_ID_LIST = [0, 1]
ROOM_IMAGES = [pygame.image.load("assets/rooms/room%i.png" % ROOM_ID_LIST[room_index]) for room_index in range(ROOM_COUNT)]

ROOM_CONFIGS = []
c_filename = ""
fi = ""
for i in range(ROOM_COUNT):
    c_filename = "assets/rooms/room%iconfig.json" % i
    with open(c_filename) as f:
        fi = f.read()

    ROOM_CONFIGS.append(json.loads(fi))
