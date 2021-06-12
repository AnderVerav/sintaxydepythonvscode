class condicion:                 #class es un cojunto de metodos y atributos
  contador=0   #variable de class 
  def __init__(self,nume1=0,nume2=0):
      self.numero1=nume1       #variable de instancia 
      self.numero2=nume2
      #numero = nume1+nume2
      self.numer3 = nume1 

  def usoIf(self):
      if self.numero1 == self.numero2:
          print("numero1:{}, numero2:{}: son iguales".format(self.numero1,self.numero2))
      elif self.numero1 == self.numer3:
           print("numero1:{}, numero3:{}: son iguales".format(self.numero1,self.numer3))
      else:
          print("Son diferentes")   
    
# cond1 = condicion()
# print(cond1.numero1)      
# print(cond1.numero2)   

cond2 = condicion(34,30)
cond2.usoIf() #llama a un metdode la class
print(cond2.numero1) #llama a un atributo de la class


      

 