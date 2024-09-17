class informacion:

    def mi_lista(self):
        lista_nombreperros=["betoben", "Toby", "deysi"]
        for x in lista_nombreperros:
            print(x)

    
    def mi_tupla(self):
        tupla_nombreperros=("betoben", "Toby", "deysi")
        print(tupla_nombreperros)
        for x in tupla_nombreperros:
            print(x)

    
    def mi_conjunto(self):
        conjunto_nombreperros={"betoben", "Toby", "deysi"}
        print(conjunto_nombreperros)
        for x in conjunto_nombreperros:
            print(x)


    def mi_diccionario(self):
        diccionario_nombreperros={
            "nombre: ": "betoben",
            "edad": 6,
            "raza: ": "pitbull"
        }
        print(diccionario_nombreperros)
        for x,y in diccionario_nombreperros.items():
            print(x,y)

#creando el objeto 
datos=informacion()
print("listado de nombre de perro")
datos.mi_lista() 

print("-------------------------------------")

print("tupla de nombre de perro")
datos.mi_tupla()

print("-----------------------------------------")

print("conjunto de nombre de perro")
datos.mi_conjunto()

print("-------------------------------------------")

print("diccionario de nombre de perro")
datos.mi_diccionario()

