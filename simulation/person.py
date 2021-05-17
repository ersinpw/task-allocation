import pygame, sys, random, time, numpy as np
from .utils import helperfunctions, settings as s
from .agent import Agent

class Person(Agent):
    def __init__(self, pos, v, population, identifier):
        super(Person, self).__init__(pos, v)
        self.population = population
        self.identifier = identifier

    def neighbor_forces(self):
        align_force, cohesion_force, separate_force = np.zeros(2), np.zeros(2), np.zeros(2)
        neighbors = self.population.find_neighbors(self, s.RADIUS_VIEW)

        if neighbors:
            align_force = self.align(self.population.find_neighbor_velocity(neighbors))
            cohesion_force = self.cohesion(self.population.find_neighbor_center(neighbors))
            separate_force = self.population.find_neighbor_separation(self, neighbors)

        return align_force, cohesion_force, separate_force

    def align(self, neighbor_force):
        """
        Function to align the agent in accordance to neighbor velocity
        :param neighbor_force: np.array(x,y)
        """
        return helperfunctions.normalize(neighbor_force - self.v)

    def cohesion(self, neighbor_center):
        """
        Function to move the agent towards the center of mass of its neighbors
        :param neighbor_rotation: np.array(x,y)
        """
        force = neighbor_center - self.pos
        return helperfunctions.normalize(force - self.v)

    def update_actions(self, simulation):
        neighbors = self.population.find_neighbors(self, s.RADIUS_VIEW)
        try:
            grid_pos = helperfunctions.pos_to_grid(simulation.environment, self.pos[0], self.pos[1], simulation.camera.scroll)
            collision = simulation.environment.world[grid_pos[0]][grid_pos[1]]["collision"]
            base = simulation.environment.world[grid_pos[0]][grid_pos[1]]["base"]
            for tile in simulation.environment.world:
                if bool(collision):
                    self.max_speed = 1
                    self.avoid_obstacle()
                    self.health -= s.OBSTACLE_DAMAGE
                else:
                    self.max_speed = s.MAX_SPEED
        except:
            self.population.remove_agent(self)
            
        self.flee(simulation.enemies) if len(neighbors) < s.NEIGHBOR_THRESHOLD else self.eliminate_enemy(simulation.enemies)
        self.protect_base(simulation)
        
        if simulation.storage > 10:
            if self.energy < s.REST_THRESHOLD:
                self.return_to_base(simulation)
        else:
            if not self.food_delivery:
                self.forage_food(simulation)
            else:
                self.return_to_base(simulation)

            align_force, cohesion_force, separate_force = self.neighbor_forces()
            total_force = self.wander(s.WANDER_DIST, s.WANDER_RADIUS, s.WANDER_ANGLE) * s.WANDER_WEIGHT\
                    + align_force * s.ALIGNMENT_WEIGHT \
                    + cohesion_force * s.COHESION_WEIGHT\
                    + separate_force * s.SEPERATION_WEIGHT

            self.steering += helperfunctions.truncate(total_force / self.mass, s.MAX_FORCE)