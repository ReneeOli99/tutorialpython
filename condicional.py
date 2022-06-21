#declaramos una variable
calificacion=input("Introduce tu calificacion de la Az-900: ")
calificacion=int(calificacion)

#preguntar si la calificacion es menor a 700
if calificacion < 700 :
    print("reprobado") #si es menor a 700 muestra esto
elif calificacion > 1000:
    print("mientes no piedes sacar mas de mil")
else: #si no se cumple el if anterior, pasa a esta linea
    print("Felicidades pasa por tu certificado") # se ejecuta si ninguno de los if se cumple


#verificador de mayoria de edad
edad=input("introduce tu edad: ")
edad=int(edad)

if edad >= 18 and edad <= 100:
    print("Bienvenido")
elif edad > 100:
    print("Si vienes acompañad@ de tus abuelitos, si te podemos fiar")
elif edad < 0:
    print("ni que fueras viaje@ del tiempo")
else :
    print("no puedes entrar")


#en python no hay switch case