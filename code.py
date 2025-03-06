import numpy as np
import pygame
import random

#first we have to set the number of squares present in the grid i.e. grid size
grid_size = 100
#next we have to set the size of each cell in the grid 
cell_size = 7


# width, height = 1024,768
width, height = grid_size * cell_size, grid_size * cell_size

# Colors
black_color = (0, 0, 0)
white_color = (255, 255, 255)
gray_color = (50, 50, 50)
red_color = (255, 0, 0)
blue_color = (0, 0, 255)

#this is the list of facings of the ants
facing=['u','r','d','l']
#this are the direction vectors for each facing coresspondingly
moves=[(0,-1),(1,0),(0,1),(-1,0)]

#this the base on which the ants move 
class ground_class:
    def __init__(self, grid_size):
        self.arr = np.zeros((grid_size, grid_size))  # Grid for colors
        self.pheromone = np.full((grid_size, grid_size), None)  # Pheromone tracking
        self.timer = np.zeros((grid_size, grid_size))  # Timer for pheromone decay

    def decay(self):
        #this function decrease the effectiveness of the Pheromone at the positions in which it is there
        self.timer[self.timer > 0] -= 1
        return
    def checker(self):
        #this function removes the pheromone once its time reaches 5 steps units 
        rows, cols = self.timer.shape
        for i in range(rows):
            for j in range(cols):
                if self.timer[i, j] == 0:
                    self.pheromone[i, j] = None 
        
# this i sthe class of the ant and this class contains all the ant properties
class Ant:
    def __init__(self, symbol):
        self.x = random.randint(20, grid_size - 20)  
        self.y = random.randint(20, grid_size - 20)
        self.facing = random.choice(facing)
        self.symbol = symbol

    def can_move(self):
        #this function returns true if ant can move and returns false if it cannot (if it is hitting the boundary of the ground)
        dx, dy = moves[facing.index(self.facing)]
        new_x = self.x + dx
        new_y = self.y + dy
        return (0 <= new_x < grid_size) and (0 <= new_y < grid_size)
    def turn_right(self):
        #this functions takes the right turn for the ant
        if self.facing=='u':
            return 'r'
        elif self.facing=='r':
            return 'd'
        elif self.facing=='d':
            return 'l'
        elif self.facing=='l':
            return 'u'
    def turn_left(self):
        #this functions takes the left turn for the ant
        if self.facing=='u':
            return 'l'
        elif self.facing=='l':
            return 'd'
        elif self.facing=='d':
            return 'r'
        elif self.facing=='r':
            return 'u'

    def standard_turing(self, ground):
       
        #this function cantains the logic for standard turning as given the problem statement
        if ground.arr[self.y, self.x] == 0:  
            ground.arr[self.y, self.x] = 1 #flipping the color of the current squares
            ground.pheromone[self.y, self.x] = self.symbol # releasing the pheromone
            ground.timer[self.x, self.y] = 5 #setting the timer for the pheromone
            self.facing = self.turn_left() 
        else:  
            ground.arr[self.y, self.x] = 0 #flipping the color of the current squares
            ground.pheromone[self.y, self.x] = self.symbol # releasing the pheromone
            ground.timer[self.x,self.y]=5 #setting the timer for the pheromone
            self.facing = self.turn_right()   

     
        if self.can_move():
            dx, dy = moves[facing.index(self.facing)]
            self.x += dx
            self.y += dy
      
    def straight(self):
        #this is defines the forword motion of the ant
        if self.can_move():
            dx, dy = moves[facing.index(self.facing)]
            self.x += dx
            self.y += dy

    def probability(self,ground):
        #80% chance to go straight, 20% chance to turn.
        return random.choices([0, 1], weights=[0.2+0.16*(5-ground.timer[self.x,self.y]), 0.8-0.16*(5-ground.timer[self.x,self.y])])[0]

    def probability_reverse(self,ground):
        #80% chance to turn, 20% chance to go straight.
        return random.choices([0, 1], weights=[0.8+0.05*(5-ground.timer[self.x,self.y]), 0.2-0.05*(5-ground.timer[self.x,self.y])])[0]

    def movement(self, ground):
        #decides movement based on pheromones and probability
        pheromone_at_cell = ground.pheromone[self.y, self.x]
        #if teh ant enter a position which has no pheromone yet
        if pheromone_at_cell is None:
            self.standard_turing(ground)
        #if the ant enters a position which has pheromone of itself
        elif pheromone_at_cell == self.symbol:  
            if self.probability(ground):
                self.straight()
            else:
                self.standard_turing(ground)
        #if the ant enters a position which has pheromone of another ant
        else: 
            if self.probability_reverse(ground):
                self.straight()
            else:
                self.standard_turing(ground)


pygame.init() #first we have intialize the pygame library
screen = pygame.display.set_mode((width, height)) # here we are setting up the window dimensions
pygame.display.set_caption("Task 1 : Langton’s Ants") # here we are setting up the title for our window
clock = pygame.time.Clock()

movement_counter = 0
# Create ground and ants with random starting positions
ground = ground_class(grid_size)
ants = [Ant('A'), Ant('B')]  # red_color and blue_color ants with random positions
font = pygame.font.SysFont('Arial', 20)
# this is the main loop for the simulation
running = True
while running:
    screen.fill(black_color)

    # this is the loop for drawing the f=grid in the ground
    for x in range(0, width, cell_size):
        pygame.draw.line(screen, gray_color, (x, 0), (x, height))
    for y in range(0, height, cell_size):
        pygame.draw.line(screen, gray_color, (0, y), (width, y))

    # drawing the white cells 
    for y in range(grid_size):
        for x in range(grid_size):
            if ground.arr[y, x] == 1:
                pygame.draw.rect(screen, white_color, (x * cell_size, y * cell_size, cell_size, cell_size))

    # moving the ants on the ground 
    for ant in ants:
        ant.movement(ground)
        color = red_color if ant.symbol == 'A' else blue_color
        pygame.draw.rect(screen, color, (ant.x * cell_size, ant.y * cell_size, cell_size, cell_size))
        movement_counter += 1
    # updating  Pheromones
    ground.decay()
    ground.checker()
    
    timer_text = font.render(f"counter: {movement_counter}", True, white_color)
    screen.blit(timer_text, (10, 10))
    #updating the window with new conditions
    pygame.display.flip()
    clock.tick(10)  # speed controling

    #closing the window if the close option is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    

pygame.quit()
