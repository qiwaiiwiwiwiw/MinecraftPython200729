# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:45:10 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
#小挑戰:斜的道路
x,y,z = mc.player.getTilePos()
for i in range(20):
    mc.setBlock(x+i,y-1,z+i,46)
    mc.setBlock(x+i+1,y-1,z+i,46)