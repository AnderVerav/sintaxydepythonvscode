# ''' # num=48
# # if type(num) == int: #type me ayuda a saber tipo es la variable
# #     print("repuesta: ",num*2)
    
# # else:
# #     print("El dato no es numerico")

# # def mensaje(men):  #toda función se empiesa con def+nombre
# #     print(men)


# # mensaje("Mi primer mensaje")
# # mensaje("Segundo mensaje")
    
#  '''


class Practica:                 #class es un cojunto de metodos y atributos
  instancia=0   #variable de class 
  def __init__(self,dato="Inicializacion"):
      self.frase=dato         #variable de instancia 
      #sintaxis.instancia = sintaxis.instancia+1

  def usoVariables(self):
       Edad, _peso = 22, 80.3
       nombre= 'Anderson Vera'
       genero = 'M'
       civil = True

      #tuplas = () son colecciones de datos de cualquier tipoinmutables  
       usuario=()
       usuario = ('Gcarlosf', 4567, 'carlosf@gmail.com', True)
       #listas = [] colecciones mutables
       materias = ['Diseño web', 'Fundamentos', 'POO']
       materias[1]="Redes"
       materias.append("Validacion") #para agg una materia adicionl
       #diccionario = {} colecciones de objetps clave:valor tipo json
       alumno = {'nombre': 'Carlos', 'Edad': 22, 'facu': 'FACI'}
       alumno['nombre']="Alexander"
       alumno['carrera']="Software"
       #presentacion con format
       print("""Mi nombre es {}, tengo {}
                años""".format(nombre, Edad))
     #presentacion de una coleccion en forma global 
       #print(usuario,materias,alumno)
       #print(usuario,usuario[0],usuario[0:2],usuario[-1])
       #print(materias,materias[2:],materias[:1],materias[::],materias[-2:])
       print(alumno,alumno['nombre'])
        
    

ejer1 = Practica() #se crea un objeto que es una instancia de la class
ejer1.usoVariables()
# print(ejer1.frase)

