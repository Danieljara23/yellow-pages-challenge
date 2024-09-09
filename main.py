people = {
  "Ana": "+4-651-928088",
  "Juan": "+23-698-536640",
  "Pedro": "+40-659-506848",
  "Luis": "+20-615-184747",
  "Maria": "+78-671-257932",
  "Sofia": "+30-611-770853",
  "Jose": "+27-669-616952",
  "Lucia": "+38-642-779107",
  "Carlos": "+19-665-202837",
  "Marta": "+38-691-898782",
  "Miguel": "+32-636-538868",
  "Laura": "+80-670-553129",
  "David": "+80-650-777691",
  "Paula": "+9-645-756359",
  "Andres": "+31-650-896836",
  "Elena": "+65-658-231873",
  "Jorge": "+35-638-631914",
  "Raul": "+54-631-199248",
  "Clara": "+94-642-663803",
  "Sara": "+48-657-677260"
}

while True:
    print("hola bienvenido a tus contactos")
    print("presiona 1 para mostrar tus contactos")
    print("presiona 2 para agregar un contacto a ala lista")
    print("presiona 3 para eliminar una de los contactos")
    
    user_in= int(input())
    
    if user_in==1:
        print(people)
        
    elif user_in==2:
        contacto=input("Agrega el nombre de contacto: ")
        telefono=input("agrega el numero de telefono: ")
        people[contacto]=telefono
        print(people)
        print(f"El elemento{contacto} ha sido agregado de la lista")
        
    elif user_in==3:
        la_peor=input("agrega el nobre de contacto a eliminar: ")
        if people.get(la_peor):
            people.pop(la_peor)
            print(people)
            print(f"El elemento{la_peor} ha sido eliminado de la lista")
        else: print("contacto no existente")
        
    else:
        print("pon un comando valido")
        break