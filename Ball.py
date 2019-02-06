'''
Created on Feb 4, 2019

@author: jfden
'''
import pygame
from pong.Config import Config
class Ball:
    
    def __init__(self, display):
        self.display = display
        self.x_pos = 300
        self.y_pos = 300 
        
        self.c_rect = pygame.Rect(self.x_pos, self.y_pos, 1, 1)
        
        self.direction_x = 'left'
        self.direction_y = None
        
        self.score_l = 0
        self.score_r = 0
        
        
    def draw(self):
        
        self.c_rect = pygame.Rect(self.x_pos, self.y_pos, 2, 2)
        
        pygame.draw.rect(self.display, Config['colors']['white'], self.c_rect) 
        pygame.draw.circle(self.display, Config['colors']['white'],
                           (self.x_pos, self.y_pos), 5)
        
        
    
    def move(self, x_delta, y_delta):
        
        if (self.direction_x == 'left'):
            
            #SCORE! Reset
            if (self.x_pos < 0):
                self.x_pos = 300
                self.y_pos = 300
                #Right gets point
                self.score_r += 1
                self.direction_y = None
                return 0
            elif(self.x_pos > 600):
                self.x_pos = 300
                self.y_pos = 300
                #Left gets point
                self.score_l += 1
                self.direction_y = None
                return 0
                                
            self.x_pos -= x_delta
        else:
            
            #SCORE! Reset
            if (self.x_pos < 0):
                self.x_pos = 300
                self.y_pos = 300
                #Right gets point
                self.score_r += 1
                self.direction_y = None
                return 0
            elif(self.x_pos > 600):
                self.x_pos = 300
                self.y_pos = 300
                #Left gets point
                self.score_l += 1
                self.direction_y = None
                return 0
            
            
            self.x_pos += x_delta
            
        #for y-axis
        if(self.direction_y == 'up'):
            
            if(self.y_pos > Config['game']['height'] - 5 or
               self.y_pos < 5):
                self.y_pos += y_delta            
                self.direction_y = 'down'
                return 0         
                                
            self.y_pos -= y_delta                    
            
        elif(self.direction_y == 'down'):
            
            if(self.y_pos > Config['game']['height'] - 5 or
               self.y_pos < 5):
                self.y_pos -= y_delta               
                self.direction_y = 'up'
                return 0
            
            
            self.y_pos += y_delta
            
        else:
            self.y_pos = self.y_pos                            
        
        
    
        