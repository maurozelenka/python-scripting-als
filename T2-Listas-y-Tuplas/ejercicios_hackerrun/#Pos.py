#Pos

import math


class Pos:
    def __init__(self, x, y, z):
        self.coord = [x, y, z]
    ...
...

pos1 = Pos(11, 12, 13)
print(pos1.coord)   
#print(pos1.__coord)  
print(pos1.__dict__)

@property 
def x(self):
    return self.__coord[0]

@property
def y(self):
    return self.__coord[1]

@property
def z(self):
    return self.__coord[2]

class Pos:
    X = 0
    Y = 1
    Z = 2
    ORG = None
    #ORG = pos(0, 0, 0)     Error: NameError: name 'pos' is not defined
    def __init__(self, x, y, z):
        self.__coord = [x, y, z]

def __getitem__(self, item):
    return self.__coord[item]

def __len__(self):    # Metodo Dunder para len()
    return len(self.__coord)

def distance_to(self, other):
    delta_sq_y = (self.y - other.y) ** 2    
    delta_sq_x = (self.x - other.x) ** 2
    delta_sq_z = (self.z - other.z) ** 2    

    return math.sqrt(delta_sq_x + delta_sq_y + delta_sq_z)

def __str__(self):
    #return f"Pos({self.x}, {self.y}, {self.z})"
    #return "(" + str.join(", ", [str(x) for x in self.__coord]) + ")"
    return "(" + ", ".join([str(x) for x in self.__coord]) + ")"

# obj.f(5) <=> A(obj, 5) Es lo mismo 

@staticmethod
def org():
    if not POS.ORG:
        POS.ORG = Pos(0, 0, 0)

        return Pos.ORG

if __name__ == "__main__":
    pos1 = Pos(11, 12, 13)
    pos2 = Pos(21, 22, 23)
    
print(f"{Pos.org()=}")
print(f"{pos1.org()=}")
print(f"{pos1.x=}")
print(f"{str(pos1)=}")
print(f"{len(pos1)=}")
print(f"{pos1[Pos.X]=}")
print(f"{pos1[Pos.Y]=}")
print(f"{pos1[Pos.Z]=}")
print(f"{pos1 - pos2=}")
print(f"{pos1 - pos1=}")
print(f"{pos1 == pos1=}")
print(f"{pos1 != pos2=}")
print(f"{pos1 == pos2=}")
print(f"{pos1.distance_to(pos2)=}")
print(f"{Pos.distance_to(pos1, pos2)=}")




from pos import Pos

class OV: 
     def __init__(self, x, y, z):
         self.__pos = Pos(x, y, z)
     
     @property
     def pos(self):
            return self.__pos
     
     @property 
     def pos(self):
            return self.__pos
     
     @pos.setter
     def pos(self, v):
            self.__pos = v
     
     def __str__(self):
            return str(self.__pos)

class OVNI(OV):
     def __init__(self, x, y, z):
            super().__init__(x, y, z)
            OV.__init__(self, x, y, z)
if __name__ == "__main__":
    ov1 = OV(22, 33, 44)
    ov1.pos._Pos__coords[0] = 99
    print(ov1.pos)
    print(ov1)
     
class OVI(OV):
     def __init__(self, com, num_vuelo, x, y, z):
            super().__init__(x, y, z)
            self.com = com
            self.num_vuelo = num_vuelo

            @property
            def com(self):
                return self.__com
            return self.__com
            
            @property
            def num_vuelo(self):
                return self.__num_vuelo
            
            #Hacer ejercicicio
            def avisos_colision(self):
                 """Devuelve una lista de pares con los vuelos que estan 
                 entre si a una distancia menor de 500 m."""
                 return []
            
            def __str__(self):
                 return f"{self.com} {self.num_vuelo}/" + super().__str__()
            
            if __name__
            ov1 = OV(22, 33, 44)
            ov2 = OVNI(55, 66, 77)
            ob3 = OVI("Iberia", "IB1234", 88, 99, 111)
            ob4 = OVI("Air Europa", "AE4321", 88, 99, 111)
            print(ov2)
            print(ob3)
            print(ob4)

            

class Torre:
     def__init__(self):
     self.__vuelos = []

     def vuelos(self):
        return list(self.__vuelos)
     

     def __add__(self, vuelo):
         self.__vuelos.append(vuelo)
         return self

     def avisos_colision(self):
         """Devuelve una lista de pares con los vuelos que estan 
         entre si a una distancia menor de 500 m."""
            avisos = [] 
            for i in range(len(self.__vuelos)):
                for j in range(i + 1, len(self.__vuelos)):
                    vuelo1 = self.__vuelos[i]
                    vuelo2 = self.__vuelos[j]
                    if vuelo1.pos.distance_to(vuelo2.pos) < 500:
                        avisos.append((vuelo1, vuelo2)) 
         return avisos 
     
     def __str__(self):
          return ", ".join([str(vuelo) for vuelo in self.__vuelos])
     
     if __name__ == "__main__":
        torre = Torre()
        torre += ov2
        torre += ob3
        torre += ob4
        torre += OVNI(1,2,3)
        print(torre)