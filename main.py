import pygame
print("Setup start")
pygame.init()

window = pygame.display.set_mode((500, 500))
print("Setup end")

print("Loop start")
while True:
    # Check for all events
    for event in pygame.event.get():
        # If the event is a quit event, exit the loop
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
