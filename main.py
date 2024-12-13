#!/usr/bin/env python3

import pygame
import sys
import os
import logging
from typing import Dict, Optional

from game_manager import GameManager
from constants import WIDTH, HEIGHT, FPS, COLORS

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class Game:
    def __init__(self):
        self.screen = None
        self.game_manager = None
        self.clock = None
        self.running = False
        try:
            self.initialize_pygame()
            self.initialize_game_components()
            logger.info('Game initialized successfully')
        except Exception as e:
            logger.critical(f'Failed to initialize game: {e}')
            sys.exit(1)

    def initialize_pygame(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Artillery Game')
        self.clock = pygame.time.Clock()

    def initialize_game_components(self) -> None:
        self.game_manager = GameManager(self.screen)
        self.running = True

    def run(self) -> None:
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self) -> None:
        self.game_manager.update()

    def draw(self) -> None:
        self.game_manager.draw()
        pygame.display.flip()

if __name__ == '__main__':
    game = Game()
    game.run()