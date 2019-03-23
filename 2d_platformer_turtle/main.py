from Player import *
from Obstacles import *
from Settings import *
import turtle

def obs_spawn(obss, amt):
    for i in range(amt):
        obst = Obstacle(SCREEN_WIDTH+10, 0)
        obss.append(obst)
        for obs in obss:
            obs.update()

player = Player(0, 0)
obss = []
obss = obs_spawn(obss, 3)
game = True

while game:
    player.update()
    for obs in obss:
        obss[obs].update()