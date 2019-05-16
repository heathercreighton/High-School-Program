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
rotate_degrees = 0
pygame.display.set_caption("Stick Figure")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# Speed in pixels per frame
x_speed = 0
y_speed = 0
 
# Current position
x_coord = 10
y_coord = 10

def draw_stick_figure(screen, x, y):
    # Draw a head
    pygame.draw.ellipse(screen, BLACK, [150 + x, 50 + y, 100, 100], 2)
    
    # Draw an arc as part of an ellipse.
    pygame.draw.arc(screen, BLACK, [170 + x, 70 + y, 60, 60], PI, 2 * PI, 4)
    
    # Draw a filled in ellipse, creating the eyes
    pygame.draw.ellipse(screen, BLACK, [180 + x, 70 + y, 10, 20])
    pygame.draw.ellipse(screen, BLACK, [210 + x, 70 + y, 10, 20])
    
    # Draw the body
    pygame.draw.line(screen, BLACK, [200 + x, 150 + y], [200 + x, 300 + y], 2)
    
    # Draw the arms 
    pygame.draw.line(screen, BLACK, [200 + x, 180 + y], [250 + x, 220 + y], 2)
    pygame.draw.line(screen, BLACK, [250 + x, 220 + y], [280 + x, 200 + y], 2)
    
    pygame.draw.line(screen, BLACK, [200 + x, 180 + y], [150 + x, 220 + y], 2)
    pygame.draw.line(screen, BLACK, [150 + x, 220 + y], [120 + x, 200 + y], 2)
    
    # Draw the legs 
    pygame.draw.line(screen, BLACK, [200 + x, 300 + y], [115 + x, 350 + y], 2)
    pygame.draw.line(screen, BLACK, [200 + x, 300 + y], [280 + x, 350 + y], 2)


# Loop as long as done == False
while not done:
    # User did something
    for event in pygame.event.get():  
        # If user clicked close
        if event.type == pygame.QUIT:  
            # Flag that we are done so we exit this loop
            done = True  
        
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
 
        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
    
    # --- Game Logic
 
    # Move the object according to the speed vector.
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed
    
    
    # All drawing code happens after the for loop and but
    # inside the main while not done loop.
    # Clear the screen and set the screen background
    screen.fill(WHITE)
    
    draw_stick_figure(screen, x_coord, y_coord)
    
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
    
    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

 
# Be IDLE friendly. If you forget this line, 
# the program will 'hang' on exit.
pygame.quit()