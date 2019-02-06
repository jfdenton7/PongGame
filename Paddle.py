"""

Josiah Denton

"""
import pygame
from pong.Config import Config

class Paddle:
    
    def __init__(self, display):
        
        self.display = display
        self.x_pos = Config['paddle']['startP1x']
        self.y_pos = Config['paddle']['startP1y']
        
        self.rec = pygame.Rect(self.x_pos, self.y_pos, 5, 100)
        
        self.direction = None
        
        
    def draw(self):
        
        color = Config['colors']['white']
        
        
        self.rec = pygame.Rect(self.x_pos, self.y_pos, Config['paddle']['width'], Config['paddle']['height'])
        
        
        pygame.draw.rect(self.display, color, self.rec)
        
        
    def move(self, y_delta):            
           
        if(self.y_pos + y_delta > Config['game']['height'] - 110 or 
           self.y_pos + y_delta < 10):
            self.y_pos = self.y_pos   
            return 0   
                
        self.y_pos += y_delta
        
        
        
        
        
        