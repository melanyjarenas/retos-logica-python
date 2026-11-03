"""
Reto 3: Control de Calidad de Insumos (Cera de Soya)

Descripción del Problema
Módulo de auditoría de inventario para controlar y clasificar cajas de cera de soya según su peso en gramos (ligeras, estándar y grandes). 
Además de auditar cada caja individualmente, la función calcula y reporta el consolidado total de unidades procesadas.

Objetivos Técnicos
- Aplicar sintaxis pythonica de "fronteras dobles" para evaluar rangos continuos sin redundancia de código.
- Implementar acumuladores y contadores independientes para múltiples categorías de insumos.
- Realizar operaciones de agregación matemática directamente dentro de cadenas formateadas (`f-strings`).

Conceptos Aplicados
- **Fronteras Dobles (Encadenamiento de Operadores):** `50 <= peso_caja <= 150` para definir límites de forma visual y concisa.
- **Acumuladores y Contadores:** Manejo simultáneo de `cajas_ligeras`, `cajas_estandar` y `cajas_grandes`.
- **Expresiones en f-strings:** `{cajas_ligeras + cajas_estandar + cajas_grandes}` para computar el 
    total general directamente en la salida de consola.

"""
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
