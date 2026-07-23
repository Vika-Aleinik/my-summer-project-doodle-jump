import pygame
import random
from Config import *

class DoodleGame :
    def __init__(self):
        self.player_x = WIDTH // 2
        self.player_y = HEIGHT - 100
        self.speed = 0
        self.platforms = []
        self._create_platforms()
    
    def _create_platforms(self) :
        self.platforms.clear()
        for i in range(NUM_PLATFORM) :
            plat_x = random.randint(0, WIDTH - PLATFORM_WIDTH)
            plat_y= i * 100 + 100
            rect = pygame.Rect(plat_x, plat_y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
            self.platforms.append(rect)
            
    def update(self):
        self.speed += GRAVITY
        self.player_y += self.speed
        
        player_rect = pygame.Rect(self.player_x, self.player_y, PLAYER_SIZE, PLAYER_SIZE)
        
        for plat in self.platforms :
            if player_rect.collidedict(plat) :
                if self.speed > 0 and player_rect.bottom <= plat.top + 10 :
                    self.speed = JUMP_SPEED
                    break
                
            if self.player > HEIGHT :
                self.player = HEIGHT - 100
                self.speed = 0
    
    def draw(self, screen) :
        for plat in self.platforms :
            pygame.draw.rect(screen, GREEN, plat)
            
            player_rect = pygame.Rect(self.player_x, self.player_y, PLAYER_SIZE, PLAYER_SIZE)
            pygame.draw.rect(screen, RED, player_rect)
            
            
        
