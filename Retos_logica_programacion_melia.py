
for number in range(15):
    if number % 3 ==0 and number % 5 == 0:
      print("el residuo es 0")

for lista_de_numeros in range(1,16):
   if lista_de_numeros % 2 == 0:
      print(f"el numero {lista_de_numeros} es PAR")
   else:
      print(f"el numero {lista_de_numeros} es IMPAR")

def evaluar_descuento(monto):
   if monto >=100:
     print("¡Felicidades! Tu compra incluye un producto de regalo.")
   else:
      print("Agrega más productos para obtener un regalo.")

evaluar_descuento(50)
evaluar_descuento(200)

def calcular_envio(monto):
   if monto <=50:
      print("Costo de envío estándar: $10")
   elif monto >=50 and monto <=100:
      print("Costo de envío rebajado: $5")
   else:
      print("¡Envío gratis! 🎉")

calcular_envio(40)
calcular_envio(96)
calcular_envio(120)

#Nivel 3: El sistema de beneficios por fidelidad (Entrevista técnica)
def cliente_fiel(historial_de_compras, monto_de_compra_Actual):
   if historial_de_compras >= 5 and monto_de_compra_Actual >50:
      print("¡Cliente VIP! Aplica 20% de descuento en el total.")
   elif historial_de_compras >=5 and monto_de_compra_Actual <=50:
      print("Cliente Frecuente. Aplica 10% de descuento.")
   else:
      print("Cliente Regular. Sin descuento especial.")
cliente_fiel(6,100)
cliente_fiel(7,40)
cliente_fiel(2,50)

#Nivel 4: El gestor de inventario y producción de Melia
def inventario_produccion(stock_actual,pedidos_pendientes):
   if stock_actual < pedidos_pendientes:
      print("¡Alerta roja! Faltan velas para los pedidos pendientes. 🚨")
   elif stock_actual >= pedidos_pendientes + 10:
      print("Stock óptimo. Producción en calma. ✨")
   else: 
      print("Stock ajustado. Se recomienda hornear un nuevo lote pronto. 🕯️")

inventario_produccion(4,10)
inventario_produccion(20,18)
inventario_produccion(3,0)

#Nivel 5: El auditor de calidad de Melia (Bucle + Condicionales)
def auditar_lote(lista_puntajes):
   for puntaje in lista_puntajes:
    if  puntaje >= 80:
      print(f" Vela con {puntaje} puntos: ¡Calidad Premium! ✨")
    elif puntaje >=50 and puntaje <=79:
       print(f"Vela con {puntaje} puntos: Calidad Estándar. 🕯️")
    else:
       print(f"Vela con {puntaje} puntos: ¡Rechazada, requiere revisión! 🚨")

auditar_lote([95, 65, 45,])

#Nivel 6: El control de ingresos diarios de Melia (Bucle + Condicionales)
def analizar_ventas(lista_ingresos):
   for ingreso in lista_ingresos:
      if ingreso >= 150.0:
         print(f" Ingreso de {ingreso}: Dia bendecido de ventas !")
      elif ingreso >=70.0 and ingreso <=149.0:
         print(f"Ingreso de: {ingreso} Día estable, buen movimiento. 📈")
      else:
         print(f"Ingreso de: {ingreso} Día bajo, hay que impulsar las redes sociales. 💡")
   
analizar_ventas([45.0, 120.0, 80.0, 200.0, 35.0, 150.0, 90.0])

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
lista_ingresos = [45.0, 120.0, 80.0, 200.0, 35.0, 150.0, 90.0]


def analizar_ventas_semana(dias, ingresos):
    # zip() empareja cada día con su respectivo ingreso en simultáneo
    for dia, ingreso in zip(dias, ingresos):
        if ingreso >= 150.0:
            print(f"{dia} - Ingreso de {ingreso}: ¡Día bendecido de ventas! 🚀")
        elif ingreso >= 70.0:
            print(f"{dia} - Ingreso de {ingreso}: Día estable, buen movimiento. 📈")
        else:
            print(f"{dia} - Ingreso de {ingreso}: Día bajo, hay que impulsar las redes sociales. 💡")

analizar_ventas_semana(dias_semana, lista_ingresos)


#7: El balance semanal de aromas en Melia (Listas paralelas + zip)
nombre_de_aromas = ["Lavanda", "Vainilla", "Coco", "Eucalipto", "Canela"]
unidades_mas_vendidas = [12, 25, 4, 30, 18]
def analizar_aromas(aromas, cantidades):
   for aroma, cantidad in zip (aromas, cantidades):
      if cantidad >=25:
         print(f" el aroma {aroma} con cantidad de ({cantidad} unidades vendidas): ¡Éxito total! Aroma estrella de la semana. 🚀")
      elif cantidad >=10 and cantidad <=24:
         print(f"el aroma {aroma} con cantidad de ({cantidad} unidades vendidas) : Ventas estables, buen movimiento.")
      else:
         print(f"el aroma {aroma} con cantidad de  ({cantidad} unidades Vendidas): Baja rotación, requiere estrategia en redes. 💡")

analizar_aromas(nombre_de_aromas, unidades_mas_vendidas)

#Reto 1: Evaluación individual sin ayuda (Estilo Entrevista Técnica)

envios_por_entregar = ["Ruta_1", "Ruta_2", "Ruta_3", "Ruta_4", "Ruta_5", "Ruta_6"]
tiempo_de_entrega = [12.5, 48.0, 52.3, 24.0, 18.0, 72.0]
def evaluar_envios(envios, lista_tiempos):
   for envio, tiempo in zip(envios, lista_tiempos):
      if tiempo <24.0:
         print(f"la {envio} ha marcado un tiempo de {tiempo} horas : Entrega Express ⚡")
         print("-" * 40)
      elif tiempo >=24.0 and tiempo <=48.0:
         print(f"la {envio} ha marcado un tiempo de {tiempo} horas : Entrega Estándar 📦")
         print("-" * 40)
      else:
         print(f"La ruta {envio} ha marcado un tiempo de {tiempo} horas :Entrega Retrasada 🚨")
         print("-" * 40)
evaluar_envios(envios_por_entregar, tiempo_de_entrega)


#🥊 Reto 2: El acumulador y contador (El salto al ejercicio tipo foto)

def resumen_auditoria(lista_puntajes):
  aprobadas = 0
  rechazadas = 0
  for puntaje in lista_puntajes:
      if puntaje >=60 :
         aprobadas = aprobadas +1
      else:
         rechazadas = rechazadas +1
  print(f"Total de velas aprobadas: {aprobadas}")
  print("-" * 40)
  print(f"Total de velas Rechazadas: {rechazadas}")

resumen_auditoria([85, 42, 90, 55, 60, 30])

#🥊 Reto de Entrevista: Auditoría de Lotes Nocturnos en Melia

lista_de_codigos= [12, 45, 78, 34, 90, 22, 63]
def validacion_de_lotes(auditar_lotes):
   lotes_especiales = 0
   lotes_regulares = 0
   lotes_de_revision = 0 
   for auditar_lote in auditar_lotes:
      if auditar_lote % 3 ==0:
         print(f"lote {auditar_lote} : Lote especial de colección ✨")
         lotes_especiales = lotes_especiales +1
      elif auditar_lote % 3 !=0  and 50<= auditar_lote <=100:
         print(f"lote {auditar_lote} : Lote estándar de alta rotación 📦")
         lotes_regulares = lotes_regulares +1
      else:
         print(f"Lote {auditar_lote} : Lote requiere revisión técnica ⚠️")
         lotes_de_revision = lotes_de_revision +1 
   print("-" * 40)
   print(f"Total de Lotes Especiales: {lotes_especiales}")
   print(f"Total de Lotes Regulares: {lotes_regulares}")
   print(f"Total de Lotes de Revisión: {lotes_de_revision}")
validacion_de_lotes(lista_de_codigos)

print("-" * 40)  
print("-" * 40) 
print("-" * 40)  
#🥊 Nuevo Reto: Control de Calidad de Insumos para Melia
lista_peso_cera = [45, 120, 80, 200, 30, 150, 95]
def auditar_cera(pesos_cajas):
   cajas_ligeras = 0
   cajas_estandar = 0
   cajas_grandes = 0
   for peso_caja in pesos_cajas:
      if peso_caja <50:
         print(f"caja de {peso_caja} Caja ligera (ideal para muestras) 🕯️")
         cajas_ligeras +=1
      elif peso_caja  >= 50 and peso_caja <= 150:
         print(f"Caja de {peso_caja} Caja estándar (producción normal) 📦")
         cajas_estandar +=1
      else:
         print(f"Caja de {peso_caja} Caja grande (producción masiva) 🌟")
         cajas_grandes +=1
   print("-" * 40)
   print(f" Total de cajas ligeras: {cajas_ligeras}")
   print(f" Total de cajas estandar: {cajas_estandar}")
   print(f" Total de cajas grandes: {cajas_grandes}")
   print(f" TOTAL DE CAJAS AUDITADAS:  {cajas_ligeras + cajas_estandar + cajas_grandes}")
auditar_cera(lista_peso_cera)

