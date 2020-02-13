#!/usr/bin/env python3
# utf-8 tab space:2  
#%matplotlib inline
import matplotlib.pyplot as plt
import math
import numpy as np

def draw_circle(p,x,y,r):
  wx,wy=[],[]

  for _x in np.linspace(-180,180,360):
    wx.append(r*math.sin(math.radians(_x))+x)
    wy.append(r*math.cos(math.radians(_x))+y)
  
  p.plot(wx,wy,color="tab:blue")
  
  return

def draw_cross(p,x,y,r):
  wx,wy=[],[]

  for _x in np.linspace(-1,1,2):
    wx.append(r*_x+x)
    wy.append(r*_x+y)
  
  p.plot(wx,wy,color="tab:red")
  
  wx,wy=[],[]
  
  for _x in np.linspace(-1,1,2):
    wx.append(r*_x+x)
    wy.append(-r*_x+y)
      
  p.plot(wx,wy,color="tab:red")
  
  return

def draw_board(fig,max_x,max_y,no,data):
  ax = fig.add_subplot(max_x, max_y, no)
  
  ax.axis([-3, 3, 3, -3])
  ax.set_aspect('equal')
  ax.tick_params(labelbottom=False, labelleft=False, labelright=False, labeltop=False)
  ax.tick_params(bottom=False, left=False, right=False, top=False)
  
  work = data
  for i in range(9):
    work2 = math.floor(work/(3**(9-i-1)))
    if work2==1 : draw_circle(ax,2*math.floor(i%3)-2,2*math.floor(i/3)-2,1)
    elif work2==2 : draw_cross(ax,2*math.floor(i%3)-2,2*math.floor(i/3)-2,0.8)
    work = work % (3**(9-i-1))
  return

if __name__ == '__main__':
  fig = plt.figure(figsize=(4,4),dpi=50)

  draw_board(fig,4,4,1,1*3**0)
  draw_board(fig,4,4,2,1*3**6)
  draw_board(fig,4,4,3,1*3**8)
  draw_board(fig,4,4,4,1*3**2)

  draw_board(fig,4,4,5,2*3**1)
  draw_board(fig,4,4,8,2*3**5)
  draw_board(fig,4,4,7,2*3**7)
  draw_board(fig,4,4,6,2*3**3)

  plt.show()