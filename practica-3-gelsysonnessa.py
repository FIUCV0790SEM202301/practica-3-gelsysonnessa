# PRÁCTICA-3: Carrera de Aquiles vs Tortuga.

Xtor = float(input("Ingresa los metros de ventaja que tendrá la tortuguita (m): "))
Vtor = float(input("Ingresa la velocidad de la tortuguita (m/h): "))

# TIEMPO DE ENCUENTRO ENTRE AQUILES Y LA TORTUGA:

while Vtor == 0:

    print("Usuario, por favor ingresa una velocidad (Vtor) diferente de 0") 
    Vtor = float(input("Ingresa la velocidad de la tortuguita (m/h): "))

tiempo_encuentro_h = (Xtor) / (Vtor*9)
posicion_aquiles = round(10 * Vtor * tiempo_encuentro_h, 3)

parte_entera_th = int(tiempo_encuentro_h)

tiempo_encuentro_m = (tiempo_encuentro_h - parte_entera_th) * 60
parte_entera_tm = int(tiempo_encuentro_m) 

tiempo_encuentro_s = (tiempo_encuentro_m - parte_entera_tm) * 60
parte_entera_ts = round(tiempo_encuentro_s) 

print("El tiempo que tarda Aquiles en alcanzar a la tortuga es:", parte_entera_th,"horas :", parte_entera_tm,"minutos :", parte_entera_ts,"segundos")
print("Aquiles y la tortuga se encuentran a", posicion_aquiles, "metros")
print("")

# COORDENADAS: DISTANCIA, TIEMPO

t1 = tiempo_encuentro_h / 7.6
t2 = tiempo_encuentro_h / 6
t3 = tiempo_encuentro_h / 4.5
t4 = tiempo_encuentro_h / 3
t5 = tiempo_encuentro_h / 1.2

print("A continuación se muestran 5 coordenadas (tiempo,posición) de Aquiles hasta alcanzar a la tortuguita:")
print("")

for i in (t1,t2,t3,t4,t5):
    parte_entera_th = int(i)
    tiempo_encuentro_m = (i - parte_entera_th) * 60
    parte_entera_tm = int(tiempo_encuentro_m) 
    tiempo_encuentro_s = (tiempo_encuentro_m - parte_entera_tm) * 60
    parte_entera_ts = round(tiempo_encuentro_s) 
    posición_aquiles = round(10 * Vtor * i, 3)
    print("        TIEMPO ----------------------- POSICIÓN  ")
    print(parte_entera_th, "horas :", parte_entera_tm, "minutos :", parte_entera_ts, "segundos", "  ", posición_aquiles, "metros")
    print(" ")
   














