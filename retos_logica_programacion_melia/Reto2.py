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
