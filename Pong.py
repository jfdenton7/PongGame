'''
Created on Feb 4, 2019

@author: jfden
'''
import pygame

from pong.Game import Game
from pong.Config import Config


def main():
    
    display = pygame.display.set_mode((Config['game']['height'], 
                                       Config['game']['width']))
                                      
    pygame.display.set_caption('Pong with Friends')
    
    game = Game(display)
    game.loop()
    
if __name__ == '__main__':
    main()