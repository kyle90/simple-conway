#Simple Conway's Game of Life Program-----------------------------------------#
#August 20, 2013--------------------------------------------------------------#
#By Kyle Buchanan-------------------------------------------------------------#
#-----------------------------------------------------------------------------#


#You know the drill-----------------------------------------------------------#
import time
import math
import pygame
import random
#-----------------------------------------------------------------------------#


#Just making some simple functions to do obvious things, for readability------#
def erase():
	screen.fill(black)
	pygame.display.flip()
	
def pixel_draw(position,colour):
	screen.set_at(position,colour)
	pygame.display.flip()
	
def pixel_change(position,colour):
	screen.set_at(position,colour)
#-----------------------------------------------------------------------------#


#Draws a square of the desired colour in the correct position-----------------#
def cell_draw(position,colour):
	for y in range(zoom):
		for x in range(zoom):
			pixel_change((position[0]*zoom+x,position[1]*zoom+y),colour)
#-----------------------------------------------------------------------------#

	
#I know the math library has a modulo function but I wanted to write my own---#
def mod(a,b):
	if b < 1:
		print("What the hell are you playing at?")
		return -1
	while a >= b:
		a -= b
	while a < 0:
		a += b
	return a
#-----------------------------------------------------------------------------#


#Just some colours to use-----------------------------------------------------#
black=(0,0,0)
white=(255,255,255)
grey=(127,127,127)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
cyan=(0,255,255)
magenta=(255,0,255)
yellow=(255,255,0)
pink=(255,127,127)
indigo=(63,0,127)
purple=(127,63,255)
#-----------------------------------------------------------------------------#


#Initializing the grid via user input-----------------------------------------#
cells_x = int(input("Enter the width of the grid: "))
cells_y = int(input("Enter the height of the grid: "))
zoom = int(input("Enter the zoom level: "))
generations = int(input("Enter the number of generations (0 to run forever): "))
#-----------------------------------------------------------------------------#


#Draw the window--------------------------------------------------------------#
screen=pygame.display.set_mode((cells_x*zoom,cells_y*zoom))
#-----------------------------------------------------------------------------#


#Making the arrays that hold the cell states----------------------------------#
grid = [[random.randint(0,1) for y in range(cells_y)] for x in range(cells_x)]
tempgrid = [[0 for y in range(cells_y)] for x in range(cells_x)]
#-----------------------------------------------------------------------------#


#Just a hack so that it goes into the while loop if it's set to run forever---#
current_gen = -1
#-----------------------------------------------------------------------------#


#Alright now we're doing things-----------------------------------------------#
while(current_gen < generations):


	#Increment the counter if the number of generations has been set----------#
	if generations > 0:
		current_gen += 1
	#-------------------------------------------------------------------------#
	
	
	#Iterate over each cell in the grid---------------------------------------#
	for y in range(cells_y):
		for x in range(cells_x):
		
		
			#This checks how many neighbouring cells are alive by adding up---#
			#their values. '1' is alive and '0' is dead. Sorry it's a mess.---#
			#The modulo function allows the grid edges to wrap around.--------#
			cells = grid[mod(x-1,cells_x)][mod(y-1,cells_y)]+grid[x][mod(y-1,cells_y)]+grid[mod(x+1,cells_x)][mod(y-1,cells_y)]+grid[mod(x-1,cells_x)][y]+grid[mod(x+1,cells_x)][y]+grid[mod(x-1,cells_x)][mod(y+1,cells_y)]+grid[x][mod(y+1,cells_y)]+grid[mod(x+1,cells_x)][mod(y+1,cells_y)]
			#-----------------------------------------------------------------#

			
			#Depending on the states of the cell and its neighbours, set the--#
			#state of the cell in the temporary grid array.-------------------#
			#-----------------------------------------------------------------#
			#GAME OF LIFE RULES:----------------------------------------------#
			#If a cell is alive and has 2-3 living neighbours, it stays alive.#
			#If a dead cell has exactly 3 living neighbours, it becomes alive.#
			#Otherwise a cell dies or stays dead.-----------------------------#
			if grid[x][y] == 0 and cells == 3:
				tempgrid[x][y] = 1
			elif grid[x][y] == 1 and cells < 2:
				tempgrid[x][y] = 0
			elif grid[x][y] == 1 and cells > 3:
				tempgrid[x][y] = 0
			elif grid[x][y] == 1:
				tempgrid[x][y] = 1
			else:
				tempgrid[x][y] = 0
			#-----------------------------------------------------------------#
			
			
			#Draws the cells on the screen. Note that this draws the previous-#
			#generation because the new generation is stored in 'tempgrid'----#
			if grid[x][y] == 1:
				cell_draw((x,y),white)
			else:
				cell_draw((x,y),black)
			#-----------------------------------------------------------------#

			
	#Update the screen after all the new cells have been calculated and drawn-#
	pygame.display.flip()
	#-------------------------------------------------------------------------#
	
	
	#Move the contents of 'tempgrid' to 'grid', and reset 'tempgrid' to zero--#
	for y in range(cells_y):
		for x in range(cells_x):
			grid[x][y] = tempgrid[x][y]
			tempgrid[x][y] = 0
	#-------------------------------------------------------------------------#


#Pauses for five seconds------------------------------------------------------#
time.sleep(5)
#-----------------------------------------------------------------------------#
