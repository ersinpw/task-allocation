import pygame, sys, time, random
from simulation.simulation import Simulation
from simulation.utils import settings as s

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    demo = Simulation(screen)
    demo.run()