# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 09:13:22 2020

@author: user
"""
#小挑戰:只有打到石頭才會變成金礦

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    hits = mc.events.pollBlockHits()
    
    if len(hits)>0:
        block = hits[0] 
        x,y,z = block.pos.x,block.pos.y,block.pos.z
        a = mc.getBlock(x,y,z)
        if a == 3:
            mc.setBlock(x,y,z,57)
        #mc.postToChat("你打到"+str(a))   
        #mc.setBlock(x,y,z,41)