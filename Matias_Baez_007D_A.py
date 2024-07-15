
print("Programa de manejo de sueldos\n")

trabajadores= {'Juan Perez':0, "Maria Garcia":0, "Carlos Lopez":0, "ANa Martinez":0, 
               "Pedro Rodriguez":0, "Laura Hernandez":0, "Miguel Sanchez":0, "Isabel Gomez":0,
               "Francisco Diaz":0,"Elena Fernandez":0}




def asignar_sueldos():
   
   return

def clasificar_sueldos():
   
   return

def ver_estadisticas():
   
   return

def reporte_sueldos():
   
   return


def menu():

   while True:

      print("Menu de opcioones")
      print("1. Asignar Sueldos Aleatorios")
      print("2. Clasificar Sueldos")
      print("3. Ver estadisticas")
      print("4. Reporte de Sueldos")
      print("5. Salir del Programa\n")

      try:
         op=int(input("Seleccione numero de opcion: "))
         if op<=5 or op>=1:
            if op==1:
               print("\nAsignar sueldos aleatorios")
            elif op==2:
               print("Clasificar sueldos")
            elif op==3:
               print("Ver estadisticas")
            elif op==4:
               print("Reporte de Sueldos")
            elif op==5:
               print("Salir del programa")
               break
      except ValueError:
         print("\nLa opcion ingresanda no es valida\n")
      else:
         if op>5 and op<1:
            print("Ingrese una opcion valida")

if __name__ =="__main__":
   menu()

print ("Finalizando programa...")
print ("Desarrollado por Matias Baez")
print ("Rut: 19.537.544-5")
