# Sistema de Gestión Académica - UADE (TPO Programación 1)

Sistema en consola desarrollado en Python para la gestión integral de datos académicos de alumnos. Permite realizar altas, bajas, modificaciones, consultas avanzadas y procesamiento estadístico.

## Integrantes - Grupo 7
* Bramuglia, Máximo
* González Colman, Delfina
* Manno, Santino
* Rodriguez Janicki, Ludmila

---

## Estructura del Proyecto

* **"datos.py"**: Contiene las listas y matrices con los datos iniciales, además de las listas fijas de turnos y estados académicos.
* **"validaciones.py"**: Funciones encargadas de validar que los ingresos del usuario sean correctos (códigos numéricos, rangos, texto, promedios y existencia de legajos).
* **"crud.py"**: Funciones para el alta de nuevos alumnos, modificación de datos de registros existentes y eliminación.
* **"consultas.py"**: Funciones para buscar alumnos por código, filtrar por turno/condición y dar formato de tabla alineada a los datos.
* **"estadisticas.py"**: Cálculos del total de registros, alumnos por turno, alumnos por estado académico y alumno con mayor promedio.
* **"menu.py"**: Interfaz visual en consola para desplegar las opciones del sistema y capturar la entrada del usuario.
* **"principal.py"**: Archivo principal que integra los módulos y coordina el flujo general del programa.

---

## Cómo Ejecutar el Programa

1. Asegurate de tener instalado Python 3.
2. Abrí una terminal o consola de comandos en la carpeta del proyecto.
3. Ejecutá el siguiente comando:

```bash
python principal.py
```
