import pygame, sys, random, time
from .utils import displayfunctions, events, helperfunctions, logfunctions ,settings as s
from .environment import Environment
from .utils.camera import Camera
from .population import Population
from .food import Food
from .base import Base
from .enemy import Enemy

class Simulation:
    def __init__(self, screen):
        self.running = True
        self.iter = s.RUNTIME
        self.swarm = Population()
        self.num_agents = s.NUM_AGENTS
        self.to_update = pygame.sprite.Group()
        self.to_display = pygame.sprite.Group()
        self.base = None
        self.screen = screen
        self.width, self.height = self.screen.get_size()
        self.day, self.hour, self.minute = s.CLOCK
        self.food = Food()
        self.enemies = pygame.sprite.Group()
        self.home = Base()
        self.transit, self.storage = 0, 0
        
    def initialize(self):
        self.camera = Camera(self)
        self.environment = Environment()
        helperfunctions.initialize(self)
        self.swarm.initialize(self)
        self.to_update = pygame.sprite.Group(self.swarm)
        self.to_display = pygame.sprite.Group(self.to_update)
        helperfunctions.update_base(self)

    def update(self):
        self.camera.update()
        displayfunctions.camera_correction(self.camera, self.food.mushrooms)
        displayfunctions.camera_correction(self.camera, self.home.home)
        helperfunctions.update_base(self)
        self.to_update.update(self)
        helperfunctions.update_enemies(self)

    def draw(self):
        self.screen.fill((0, 0, 0))
        count, avg_health, avg_energy = self.environment.draw(self)
        
        text_list = [
            'Day {} = {}:{}'.format(self.day, self.hour, self.minute),
            'Swarm size = {}'.format(count),
            'Swarm health = {0:10.1f}'.format(avg_health),
            'Swarm energy = {0:10.1f}'.format(avg_energy),
            'Available food = {}'.format(len(self.food.mushrooms)),
            'Food in transit = {}'.format((self.transit)),
            'Food at base = {}'.format((self.storage)),
            'Number of enemies = {}'.format(len(self.enemies))
        ]
        
        displayfunctions.display_info(self.screen, text_list)
        pygame.display.flip()
        return count, avg_health, avg_energy

    def run(self):
        self.initialize()
        while self.running:
            for _ in range(self.iter):
                displayfunctions.update_world_clock(self)
                events.events(self)
                self.update()
                count, avg_health, avg_energy = self.draw()
                if count == 0:
                    self.running = False
                    logfunctions.get_list(self, count, avg_health, avg_energy)
                    pygame.quit()
                    sys.exit()
            self.running = False
            logfunctions.get_list(self, count, avg_health, avg_energy)
            pygame.quit()
            sys.exit()