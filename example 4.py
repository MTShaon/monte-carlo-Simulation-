''''
name   : md. tanviir akter shaon
id     : 011 171 292
subject: Simulation & Modeling Laboratory(CSI 424)
section: A
date   : 14-03-2021
'''
import math
import numpy as np
import matplotlib.pyplot as plt
list=[100,1000,5000,10000,100000]  



for n in list: 
  hits=0                          # initial hits variable                  

  hits_x=[]                       # initial hits_x list for cordinate for x of hitting point inside the circle
  hits_y=[]                       # initial hits_y list for cordinate for x of hitting point inside the circle

  miss_hit_x=[]                   # initial miss_hits_x list for cordinate for x of miss hitting point inside the circle
  miss_hit_y=[]                   # initial miss_hits_x list for cordinate for x of miss hitting point inside the circle                                       
  for i in range(n):

    x=np.random.uniform(0,4)                   #get rendom x
    y=np.random.uniform(0,2)                   #get rendom x
    if x<=y:
      if y<=x:
        hits=hits+1                               # if dart hit under the curv then increase vaule of hits

        hits_x.append(x)                          # if dart hit under the curv then increase vaule of hits_x list for ploting
        hits_y.append(y)                          # if dart hit under the curv then increase vaule of hits_y list for ploting
      else:

        miss_hit_x.append(x)                       # if dart miss hit under the curv then increase vaule of miss_hits_x list for ploting
        miss_hit_y.append(y) 
    else:
       if y<=4-x:
        hits=hits+1                               # if dart hit under the curv then increase vaule of hits

        hits_x.append(x)                          # if dart hit under the curv then increase vaule of hits_x list for ploting
        hits_y.append(y)                          # if dart hit under the curv then increase vaule of hits_y list for ploting
       else:

        miss_hit_x.append(x)                       # if dart miss hit under the curv then increase vaule of miss_hits_x list for ploting
        miss_hit_y.append(y)

  
  print(f'\ntotal hit is {hits} for {n} trails')   # print total hit

 # print(f'value of pi is {PI} for {n} trails')     # print the value of PI
  plt.scatter(hits_x,hits_y,color="red",label="Hit Points")              #plot hitting inside circle
  plt.scatter(miss_hit_x,miss_hit_y,color="green",label="Miss Points")   #plot hitting inside rectangle but outside circle
  plt.title(f'plot for {n} trails')
  plt.legend()                                                          # show meaning of color
  plt.show()
