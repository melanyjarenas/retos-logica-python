# 🌙 Reto 2: Auditoría Nocturna de Lotes de Producción

## 📌 Descripción del Problema
Desarrollo de un sistema de inspección lógica para lotes de producción. La función evalúa códigos numéricos para identificar lotes especiales de colección, lotes de alta rotación o aquellos que requieren revisión técnica inmediata por parte del equipo de calidad.

## 🎯 Objetivos Técnicos
- Validar múltiplos numéricos utilizando el operador módulo (`%`).
- Garantizar la correcta inicialización y alcance (*scope*) de variables locales para contadores.
- Construir un reporte de resumen global al finalizar el bucle principal.

## 🛠️ Conceptos Aplicados
- **Operador Módulo:** `% 3 == 0` (lotes especiales) y `% 3 != 0` (validaciones secundarias).
- **Contadores Locales:** Inicialización dentro de la función y actualización mediante asignación explícita (`lotes_especiales += 1`).
- **Scope e Indentación:** Separación entre el procesamiento por elemento (dentro del `for`) y el resumen global del lote (fuera del `for`).
