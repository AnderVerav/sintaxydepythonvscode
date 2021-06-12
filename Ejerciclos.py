class Ciclos:                
  contador=0    
  def __init__(self,nume1=5):
      self.numero=nume1
  def usowhile(self):
      car = input ("Ingresar una vocal: ")
      car = car.lower()   
      while car not in('a','e','i','o','u'):
          car = input ("Ingresar una vocal: ").lower()
          print("El caracter:{} es correcto".format(car))

ciclo1 =Ciclos()
ciclo1.usowhile()
      