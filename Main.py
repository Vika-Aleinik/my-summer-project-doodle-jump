import pygame
import sys
from Config import *
from Logic import DoodleGame

def main() :
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    game = DoodleGame()
    
    running = True
    while running :
        clock.tick(FRAMES)
        
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False
                
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] :
            game.player_x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] :
            game.player_x += PLAYER_SPEED
            
        if game.player_x < 0 :
            game.player_x = 0
        if game.player_x > WIDTH - PLAYER_SIZE :
            game.player_x = WIDTH - PLAYER_SIZE
            
        game.update()
        
        screen.fill(WHITE)
        game.draw(screen)
        
        pygame.display.flip()
        
    pygame.quit()
    sys.exit()
    
if __name__ == "__main__" :
    main()