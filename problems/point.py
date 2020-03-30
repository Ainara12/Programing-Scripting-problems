import math

class Point3d():#Sintax to create a class , name, brackets and variables 

    x = 0
    y = 0
    z = 0
    def distance(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)



p1 = Point3d()
p1.x = 5.1
p1.y = 3.4
p1.z = 2.0

print(p1.distance())

p2 = Point3d()
p2.x = 6.5
p2.y = 7.6
p2.z = 3.7

print (p2.distance())
