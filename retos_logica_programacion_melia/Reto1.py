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
