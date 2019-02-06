'''
Created on Feb 4, 2019

@author: jfden
'''

import pygame
from pong.Paddle import Paddle
from pong.Config import Config
from pong.Ball import Ball
from builtins import str

class Game:
    
    def __init__(self, display):
        self.display = display
        
        
    def loop(self):
        
        clock = pygame.time.Clock()
        
        paddle = Paddle(self.display)
        ball = Ball(self.display)
        
        
        #Game scoreboard:
        pygame.font.init()                
        
        paddle2 = Paddle(self.display)
        paddle2.x_pos = Config['paddle']['startP2x']
        paddle2.y_pos = Config['paddle']['startP2y']
        
        #initial movement for ball
        ball.move(-1, 0)
        
        speed = Config['game']['speed']
        x_delta = 0
        y_delta = 0
        
        y_delta2 = 0
        
        while True:
                        
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    exit()
                    
                if event.type == pygame.KEYDOWN:            
                    
                    if event.key == pygame.K_i:
                        #move up                        
                        y_delta = -speed
                        paddle.direction = 'up'
                    elif event.key == pygame.K_k:
                        #move down                        
                        y_delta = speed
                        paddle.direction = 'down' 
                        
                    elif event.key == pygame.K_l:
                        y_delta = 0
                        
                    if event.key == pygame.K_w:
                        
                        y_delta2 = -speed
                        paddle2.direction = 'up'
                        
                    elif event.key == pygame.K_s:
                        
                        y_delta2 = speed
                        paddle2.direction = 'down'
                                       
            
                                
                  
            #Draw background first  
            self.display.fill(Config['colors']['black'])
            #move paddle
            paddle.move(y_delta)
            #draw paddle
            paddle.draw()
            
            #For player two
            paddle2.move(y_delta2)
            
            paddle2.draw()
            
            
            
            #initial ball movement
            #ball.move(-speed, 0)
            
            #Check collision for ball:
            if (ball.c_rect.colliderect(paddle.rec) or 
                ball.c_rect.colliderect(paddle2.rec)):
                
                #increase speed by one
        
                
                #assign movement direction
                if (ball.direction_x == 'left'):
                    x_delta = speed
                    ball.direction_x = 'right'
                elif (ball.direction_x == 'right'):
                    x_delta = speed
                    ball.direction_x = 'left'
                    
                #Now check where paddle was headed 
                #ONLY DURING COLLISION IS CHECK
                if (paddle.direction == 'up' or 
                    paddle2.direction == 'up'):
                    y_delta = speed
                    ball.direction_y = 'up'
                    
                elif (paddle.direction == 'down' or 
                      paddle2.direction == 'down'):
                    y_delta = speed
                    ball.direction_y = 'down'
                
                else:
                    y_delta = 0
                    
                                                               
                                                               
                ball.move(x_delta, y_delta)
                
            #No collision detected
            else:
                ball.move(speed, speed)
                
                
            
            #draw the ball
            ball.draw()
            
            
            clock.tick(30)
            
            #Scoreboard
            myfont = pygame.font.SysFont('Comic Sans MS', 30)
            
        
            left_score = str(ball.score_l)
            right_score = str(ball.score_r)
            texts = myfont.render(left_score + ':' + right_score, True, Config['colors']['white'])
        
            self.display.blit(texts, (275, 50))

            
            
            pygame.display.update()
        
        
        
        
        