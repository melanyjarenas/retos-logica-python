# 🕯️ Reto 3: Control de Calidad de Insumos (Cera de Soya)

## 📌 Descripción del Problema
Módulo de auditoría de inventario para controlar y clasificar cajas de cera de soya según su peso en gramos (ligeras, estándar y grandes). Además de auditar cada caja individualmente, la función calcula y reporta el consolidado total de unidades procesadas.

## 🎯 Objetivos Técnicos
- Aplicar sintaxis pythonica de "fronteras dobles" para evaluar rangos continuos sin redundancia de código.
- Implementar acumuladores y contadores independientes para múltiples categorías de insumos.
- Realizar operaciones de agregación matemática directamente dentro de cadenas formateadas (`f-strings`).

## 🛠️ Conceptos Aplicados
- **Fronteras Dobles (Encadenamiento de Operadores):** `50 <= peso_caja <= 150` para definir límites de forma visual y concisa.
- **Acumuladores y Contadores:** Manejo simultáneo de `cajas_ligeras`, `cajas_estandar` y `cajas_grandes`.
- **Expresiones en f-strings:** `{cajas_ligeras + cajas_estandar + cajas_grandes}` para computar el total general directamente en la salida de consola.
