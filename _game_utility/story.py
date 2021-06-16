import pygame

text = """
Once upon a time there was a group of monsters wandering around.]]
One day the group of monsters met people.}}
But the people were angry and imprisoned the monsters.]]
The monsters managed to break out, but ran away in fear.}}
When they came across a place in the desert, very far away from the people, they decided to create a village.}}
Five years later a person came to the desert.}}
He ran and ran and then, suddenly he met the monsters.]]
He had no idea what was ahead of him.}}
That person is YOU.}}
Explore. Discover. Survive.]]
"""

font = pygame.font.Font("../assets/fonts/font.ttf")

groups = text.split("}}")

for i in range(len(groups)):
    groups[i] = groups[i].split("]]")

surfaces = []

for group in groups:
    toAppend = []
    for line in group:
        toAppend.append(font.render(line, True, (255, 255, 255)))

    surfaces.append(toAppend)


