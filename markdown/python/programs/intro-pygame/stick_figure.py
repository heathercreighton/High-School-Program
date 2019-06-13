# Import a library of functions called 'pygame'
import pygame
 
# Initialize the game engine
pygame.init()

# Define some colors
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PI = 3.141592653
 
# Set the height and width of the screen
size = (400, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Stick Figure")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# Loop as long as done == False
while not done:
    # User did something
    for event in pygame.event.get():  
        # If user clicked close
        if event.type == pygame.QUIT:  
            # Flag that we are done so we exit this loop
            done = True  
    # All drawing code happens after the for loop and but
    # inside the main while not done loop.
    
    # Clear the screen and set the screen background
    screen.fill(WHITE)
    
    # Draw a head
    pygame.draw.ellipse(screen, BLACK, [150, 50, 100, 100], 2)
    
    # Draw an arc as part of an ellipse.
    pygame.draw.arc(screen, BLACK, [170, 70, 60, 60], PI, 2 * PI, 4)
    
    # Draw a filled in ellipse, creating the eyes
    pygame.draw.ellipse(screen, BLACK, [180, 70, 10, 20])
    pygame.draw.ellipse(screen, BLACK, [210, 70, 10, 20])
    
    # Draw the body
    pygame.draw.line(screen, BLACK, [200, 150], [200, 300], 2)
    
    # Draw the arms 
    pygame.draw.line(screen, BLACK, [200, 180], [250, 220], 2)
    pygame.draw.line(screen, BLACK, [250, 220], [280, 200], 2)
    
    pygame.draw.line(screen, BLACK, [200, 180], [150, 220], 2)
    pygame.draw.line(screen, BLACK, [150, 220], [120, 200], 2)
    
    # Draw the legs 
    pygame.draw.line(screen, BLACK, [200, 300], [115, 350], 2)
    pygame.draw.line(screen, BLACK, [200, 300], [280, 350], 2)
    
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
    
    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

 
# Be IDLE friendly. If you forget this line, 
# the program will 'hang' on exit.
pygame.quit()