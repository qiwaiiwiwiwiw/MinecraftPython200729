# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:11:19 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random

pos = mc.player.getPos()
while True:
    pos = mc.player.getPos()
    x = pos.x+random.uniform(-20,20)
    z = pos.z+random.uniform(-20,20)
    y = pos.y+30
    mc.spawnEntity(x,y,z,20)
    
    