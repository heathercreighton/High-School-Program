import pygame
 
# Initialize the game engine
pygame.init()
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PI = 3.141592653
TEXT_OUTPUT = 'Number times button clicked: '
BLUE_COLOR = 0
RED_COLOR = 0
 
# Set the height and width of the screen
size = (400, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Rotate Text")
 
# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
num_clicks = 0 
text_rotate_degrees = 0

 
# Loop as long as done == False
while not done:
	keys = pygame.key.get_pressed()
	if keys[pygame.K_0]:
		BLUE_COLOR = ((BLUE_COLOR + 1) % 255)
		num_clicks += 1
		print(f"BLUE VALUE: {BLUE_COLOR}")

	if keys[pygame.K_1]:
		RED_COLOR = ((RED_COLOR + 1) % 255)
		num_clicks += 1
		print(f"RED VALUE: {RED_COLOR}")
		
	for event in pygame.event.get():  # User did something
		if event.type == pygame.QUIT:  # If user clicked close
			done = True  # Flag that we are done so we exit this loop

	# All drawing code happens after the for loop and but
	# inside the main while not done loop.
	# Clear the screen and set the screen background
	screen.fill(WHITE)
	# Select the font to use, size, bold, italics
	font = pygame.font.SysFont('Calibri', 25, True, False)

	# Animated rotation

	temp = TEXT_OUTPUT + str(num_clicks)
	text = font.render(temp, True, (RED_COLOR, 0, BLUE_COLOR))
	text = pygame.transform.rotate(text, text_rotate_degrees)
	text_rotate_degrees += 1
	screen.blit(text, [100, 50])
	# Go ahead and update the screen with what we've drawn.
	# This MUST happen after all the other drawing commands.
	pygame.display.flip()
	# This limits the while loop to a max of 60 times per second.
	# Leave this out and we will use all CPU we can.
	clock.tick(60)

# Be IDLE friendly
pygame.quit()
