print("clases vercion 2 el constructor")
class perro:
    #funcion constructor 
    def __init__(self,color,edad):
        self.color=color
        self.edad=edad

        #funciones creadas por el usuario
    def muerde(self):
        print("chale el perro me mordio")

    def chatperro(self, mensaje):
        print(f"chat perro: {mensaje}")

    def chatperra(self,mensajep):
        print(f"chat perra: {mensajep}")

    def datos(self):
        print(f"color: {self.color} edad: {self.edad}")
#crear el objeto

chihuas=perro("negro", 2)

#llamadas a funciones

chihuas.datos()
chihuas.muerde()
chihuas.chatperro("hola perrita")
chihuas.chatperra("hola betoben")
chihuas .chatperro("quieres ser mi gugguu")
chihuas.chatperra("grrrru....")