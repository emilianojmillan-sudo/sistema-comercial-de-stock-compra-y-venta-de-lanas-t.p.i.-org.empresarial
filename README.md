
# 🧶 Hebra: Lanas y Tejidos — Sistema Integrado de Gestión y Control de Inventario

Este repositorio contiene el proyecto del sistema de registro de mercadería a presentar como Trabajo Práctico Integrador de la materia Organización Empresarial del primer semestre de la Tecnicatura Universitaria en Programación a Distancia (TUPaD) de la Universidad Tecnológica Nacional (UTN) del año 2026.

**Asignatura:** Organización Empresarial 

**Carrera:** Tecnicatura Universitaria en Programación a Distancia (TUP AD) — Universidad Tecnológica Nacional (UTN)

**Alumno:** Emiliano José Millan

**Docentes:** Prof. Gabriela Martínez (Titular), Prof. Mario Raúl López, Prof. Roberto Fabián Regner

## 📌 Descripción General del Proyecto 

**Hebra: Lanas y Tejidos** es una empresa comercial dedicada a la venta de lanas, hilados e insumos para tejido, además de la organización de talleres presenciales.

El objetivo de este sistema de información es **automatizar y centralizar la gestión operativa del comercio**, resolviendo la sincronización de inventario en tiempo real a través de tres pilares fundamentales.

1. **Punto de Venta e Integración con Balanza Digital:** Registro automatizado del pesaje de lanas en gramaje exacto e integración con el cálculo de precios por kilo.
2. **Sincronización Multicanal:** Control unificado de stock entre la tienda física, el e-commerce web y el catálogo de WhatsApp, evitando sobreventas y emitiendo alertas de reposición crítica a fábrica.
3. **Gestión de Reservas para Talleres:** Planificación y reserva anticipada de insumos para clases presenciales de tejido con alertas preventivas de re-stock.

## Estructura del Repositorio

Carpeta:

## Requisitos de Entorno

*Para ejectuar este proyecto se necesita:*
- Editor como VSCode
- Librería de funciones del programa:
```bash
  from paquete_tpi_org_empre import funciones
```

## 🤖 Declaración de Transparencia en el Uso de Inteligencia Artificial 

De acuerdo con las pautas de transparencia y responsabilidad académica fijadas por la cátedra.

> **Nota de Transparencia:** Para la estructuración técnica de la documentación de este proyecto (organigrama formal, diseño preliminar del diccionario de datos y formato del repositorio en GitHub) se utilizó la asistencia interactiva de la herramienta de IA Generativa **Gemini Notebook** como soporte de co-creación.
> **Criterio y Responsabilidad Humana:** La herramienta fue empleada mediante prompts específicos para la maquetación y validación de formatos según normativas (IRAM/AFNOR). Todo el análisis conceptual del dominio del negocio, la lógica de la balanza digital, la definición de las reglas comerciales de *Hebra* y la revisión crítica del contenido generado son de responsabilidad exclusiva del estudiante.

## 📊 Diccionario de Datos 
El sistema de información está estructurado sobre tres entidades principales que soportan la sincronización de inventario, el registro de ventas por balanza digital y la reserva de insumos para talleres. 

---

### 1. Entidad: `PRODUCTO_LANA` 
**Propósito:** Almacena los metadatos de cada tipo de lana comercializada, sirviendo de base de datos para la sincronización entre la báscula digital, la página web y el catálogo de WhatsApp.

| Nombre del Campo | Tipo de Dato | Descripción Funcional | 
| :--- | :--- | :--- |
| `id_producto` | `INTEGER` | Identificador único de cada producto en la base de datos. |
| `nombre_hilado` | `VARCHAR` / `STRING` | Nombre comercial de la lana. | 
| `codigo_marca_color` | `VARCHAR` / `STRING` | Variable de doble funcionalidad que registra marca y color. |
| `precio_por_kilo` | `FLOAT` | Valor monetario por kilo (utilizado para calcular el precio tras el pesaje). |
| `stock_disponible_gramos` | `FLOAT` | Cantidad (por peso) disponible en el local para evitar sobreventas en web. |
| `stock_minimo_critico` | `FLOAT` | Stock mínimo (por peso) que activa la alerta de reposición a fábrica. |

---

### 2. Entidad: `REGISTRO_PESAJE` 
**Propósito:** Registra en tiempo real los eventos de pesaje recibidos a través del puerto de la báscula digital conectada al ordenador del local.
| Nombre del Campo | Tipo de Dato | Descripción Funcional | 
| :--- | :--- | :--- |
| `id_pesaje` | `INTEGER` | Identificador único de cada pesaje. | 
| `id_producto` | `INTEGER` | Clave foránea al producto asociado (obtenido tras ingresar marca y color). |
| `peso_gramos` | `FLOAT` | Cantidad exacta de gramos enviada por la báscula al programa. |
| `precio_total` | `FLOAT` | Importe total calculado (`precio_por_kilo` * `peso_gramos`). |
| `fecha_hora_operacion` | `DATETIME` | Fecha y hora de la operación para control al finalizar la jornada. |
| `canal_venta` | `INTEGER` | Origen de la transacción (`1`: Tienda física, `2`: Tienda web). |

---

### 3. Entidad: `RESERVA_TALLER`
**Propósito:** Controla los materiales reservados para las clases presenciales de tejido, garantizando el abastecimiento previo
| Nombre del Campo | Tipo de Dato | Descripción Funcional | 
| :--- | :--- | :--- |
| `id_reserva` | `INTEGER` | Identificador único del material asignado para el taller presencial. |
| `id_producto` | `INTEGER` | Clave foránea al producto en la base de datos. |
| `fecha_taller` | `DATETIME` | Fecha en la que se dictará la clase de tejido. |
| `peso_gramos_requerido` | `FLOAT` | Cantidad de gramos necesarios para el desarrollo del taller. |
| `alerta_48hs_previas` | `BOOLEAN` | Indicador booleano que alerta si se requiere re-stock antes del taller. |




