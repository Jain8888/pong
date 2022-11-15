############################
import pygame
pygame.init() # always have to initialize pygmae
############################
# Variables
# ALL CAPITALS MEANS CONSTANT
WIDTH, HEIGHT = 1024, 720
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pong")

FPS = 60

WHITE = (255,255,255)
BLACK = (0,0,0)

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
############################
class Paddle:
    
    COLOR = BLACK
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def draw(self,win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))
        
############################
def draw(win, paddles):
    win.fill(WHITE) # command 
    for paddle in paddles:
        paddle.draw(win)
        
    pygame.display.update() # update after every command so that it shows on window
############################
def main():
    run = True
    clock = pygame.time.Clock()  # framerate thats same for any system
    
    left_paddle = Paddle(10,HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    
    
    while run: # main loop that constantly runs
        clock.tick(FPS) # clock ticks by FPS each iteration
        draw(WIN, [left_paddle, right_paddle]) # every frame window resets and fills with draw 
        for event in pygame.event.get(): # getting all events like quitting starting etc.
            if event.type == pygame.QUIT:
                run = False
                break
            
    pygame.quit()
#############################
# if we import this file to another file main would not run 
if __name__=='__main__':
    main()
#############################
# paddle

# ball

# scoring

