"""
Reto 2: Auditoría Nocturna de Lotes de Producción

Descripción del Problema
Desarrollo de un sistema de inspección lógica para lotes de producción. La función evalúa códigos numéricos para identificar lotes especiales de colección, lotes de alta rotación o aquellos que requieren revisión técnica inmediata por parte del equipo de calidad.

Objetivos Técnicos
- Validar múltiplos numéricos utilizando el operador módulo (`%`).
- Garantizar la correcta inicialización y alcance (*scope*) de variables locales para contadores.
- Construir un reporte de resumen global al finalizar el bucle principal.

Conceptos Aplicados
- **Operador Módulo:** `% 3 == 0` (lotes especiales) y `% 3 != 0` (validaciones secundarias).
- **Contadores Locales:** Inicialización dentro de la función y actualización mediante asignación explícita (`lotes_especiales += 1`).
- **Scope e Indentación:** Separación entre el procesamiento por elemento (dentro del `for`) y el resumen global del lote (fuera del `for`)."""

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
