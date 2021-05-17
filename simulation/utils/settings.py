# Simulation: gameplay
RUNTIME = 7200

# Swarm
NUM_AGENTS = 10
AGENT_IMAGE = "simulation/utils/assets/lemmings.png"

# Health bar
HEALTH_X, HEALTH_Y = 25, 25

# Energy bar
ENERGY_X, ENERGY_Y = 25, 40

# Environment
TILE_SIZE = 64
ISO_X = 20
ISO_Y = 20
PERLIN_SCALE = ISO_X / 2
PERLIN_UPPER = 15
PERLIN_LOWER = -35
GRASS_SURFACE = ISO_X * TILE_SIZE * 2, ISO_Y * TILE_SIZE + 2 * TILE_SIZE
OBSTACLE_DAMAGE = 0.005
REST_THRESHOLD = 20
NEIGHBOR_THRESHOLD = 2
CLOCK = [1, 0, 0]

# Food
FOOD_IMAGE = "simulation/utils/assets/food.png"
FOOD_SCALE = [500, 1000]

# Enemy
SNAKE_IMAGE = "simulation/utils/assets/snake.png"
SNAKE_WIDTH = 75
SNAKE_HEIGHT = 50

# Objects
BASE_IMAGE = "simulation/utils/assets/base.png"
BOUNDS = 73

# Agent
MAX_HEALTH = 100
MAX_ENERGY = 100
MIN_HEALTH = 0
MIN_ENERGY = 0
WIDTH = 20
HEIGHT = 20
dT = 0.2 

#agents mass
MASS = 50
SNAKE_MASS = 100
AVOIDANCE_VELOCITY = 0.5

#agent maximum speed and 'duration'
MAX_SPEED = 4.
MIN_SPEED = 4.
MAX_FORCE = 0.6
RADIUS_VIEW = TILE_SIZE

#wandering definition
WANDER_RADIUS = 3.0
WANDER_DIST = 0.5
WANDER_ANGLE = 2.0

#weights for velocity forces
COHESION_WEIGHT = 2.
ALIGNMENT_WEIGHT = 2.
SEPERATION_WEIGHT = 5.
WANDER_WEIGHT = 0.01

# Camera
CAMERA_BOUND = 0.97
CAMERA_DXDY = [0, 0]
CAMERA_SPEED = 5
CAMERA_INIT = -ISO_X / 2 * TILE_SIZE, -ISO_Y / 2 * TILE_SIZE / 2

# Colours
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# TEXT
TEXT_OFFSET = 10
TEXT_SIZE = 25
TEXT_DY = 20