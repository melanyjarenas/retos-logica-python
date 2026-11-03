"""
 Reto 1: Clasificación de Tiempos Logísticos

 Descripción del Problema
Este módulo resuelve la automatización y evaluación de tiempos de entrega y procesamiento en rutas logísticas. 
El objetivo principal es iterar sobre dos listas paralelas (nombres de rutas y sus tiempos correspondientes) 
para clasificar cada ruta en categorías de eficiencia.

 Objetivos Técnicos
- Utilizar la función integrada `zip()` para iterar sobre múltiples secuencias en paralelo de forma limpia.
- Aplicar condicionales `if/elif/else` para clasificar tiempos en umbrales de rendimiento.
- Imprimir un reporte individual estructurado para cada ruta evaluada.

 Conceptos Aplicados
- **Iteración paralela:** `zip(rutas, tiempos)`
- **Estructuras de control:** Condicionales para evaluación de límites numéricos.
- **Formateo de cadenas:** `f-strings` para salidas claras en consola.
"""


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
