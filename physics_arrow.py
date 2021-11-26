import math
from numpy import sqrt


# write mass as a function of the area (workout the correlation which is approx 5)
# work out height as a function of 

class Arrow():
    def _init_(self, mass, velocity, position):
        self.mass = mass
        self.velocity = velocity
        self.momentum = self.mass*self.velocity
        self.position = position

    def _updateMomentum_(self):
        self.momentum = self.mass*self.velocity

    def _updatePosition_(self, time):
        self.position = self.position+self.velocity*time

areas = [0.0004, 0.0016, 0.0036, 0.0064, 0.01]

C = 1.17 # coefficient of drag for square flat plane
rho = 1.225 # density of air as a fluid, liquid constant
g = -9.81 # gravity
v0 = math.sqrt(0.50/0.0069) # finding velocity derived from the finding the newton metre of the arrow by using the smart cart

for A in areas:

    arrow = Arrow()
    arrow.mass = 0.0069
    arrow.velocity = v0
    arrow.momentum = arrow.mass*arrow.velocity
    arrow.position = 1
    t = 0
    dt = 0.0001

    while arrow.position >= 1:
        arrow.velocity = arrow.momentum/arrow.mass        #mass cancels out to get us back to velocity
        F = arrow.mass*g-.5*rho*A*C*(arrow.velocity)**2   #we have the force of drag
        arrow.momentum = arrow.momentum+F*dt              #updating momentum to include air resistance per time interval
        arrow.position = arrow.position+arrow.momentum*dt/arrow.mass   # old + velocity * time interval
        t = t+dt

        if arrow.velocity < 0.001 and arrow.velocity > -0.001:
            print(arrow.position-1)   # inital position is 1
            break


# logger pro plot negative natural log
