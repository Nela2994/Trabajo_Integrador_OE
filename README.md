# README.md

# CHATBOT NORDEMAQ – GESTIÓN DE STOCK DE MAQUINARIAS

## Trabajo Práctico Integrador

**Tecnicatura Universitaria en Programación a Distancia**
**Materia:** Organización Empresarial

---

## Descripción del Proyecto

Chatbot Nordemaq es una aplicación desarrollada en Python que simula el funcionamiento de un chatbot administrativo orientado a la gestión del stock de maquinarias agrícolas y de construcción.

El sistema automatiza consultas que anteriormente eran realizadas de forma manual sobre una plantilla Excel, permitiendo optimizar tiempos, reducir errores y facilitar el acceso a la información del inventario.

La solución integra conceptos de modelado de procesos mediante BPMN 2.0, persistencia de datos y programación estructurada.

---

## Objetivos

* Automatizar la consulta del stock de maquinarias.
* Facilitar la búsqueda de unidades específicas.
* Simular reservas de equipos disponibles.
* Permitir la actualización de estados.
* Mantener sincronizada la información mediante una plantilla Excel.
* Aplicar conceptos de BPMN, persistencia y manejo de errores.

---

## Funcionalidades

El chatbot ofrece las siguientes opciones:

1. Ver maquinaria disponible.
2. Buscar maquinaria por modelo.
3. Buscar por línea.
4. Buscar por ubicación.
5. Buscar por año de fabricación.
6. Ver máquinas en tránsito.
7. Simular reserva.
8. Ver máquinas reservadas.
9. Ver máquinas vendidas.
10. Cambio de estado.
11. Ver stock completo.
12. Salir del sistema.

---

## Tecnologías Utilizadas

* Python 3.13
* Pandas
* OpenPyXL
* Visual Studio Code
* Microsoft Excel
* Git y GitHub

---

## Estructura del Proyecto

```text
Integrador/
│
├── TPI.py
├── STOCK DE AGRO Y CONST DE NEWW HOLLAND.xlsx
├── README.md
├── Documentación.pdf
└── Capturas IA/
```

### Descripción de archivos

**TPI.py**

Contiene el código fuente completo del chatbot.

**STOCK DE AGRO Y CONST DE NEWW HOLLAND.xlsx**

Plantilla Excel utilizada como base de datos simulada.

**README.md**

Documento con información general del proyecto.

**Documentación.pdf**

Informe académico del Trabajo Práctico Integrador.

**Capturas IA/**

Carpeta con evidencias del uso de herramientas de inteligencia artificial.

---

## Requisitos

Para ejecutar el proyecto es necesario disponer de:

* Python 3.13 o superior.
* Acceso al archivo Excel del stock.
* Terminal o Visual Studio Code.

---

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/USUARIO/chatbot-nordemaq.git
```

Ingresar a la carpeta del proyecto:

```bash
cd chatbot-nordemaq
```

Instalar las dependencias:

```bash
pip install pandas openpyxl
```

---

## Ejecución

Desde la terminal ejecutar:

```bash
python TPI.py
```

Si la carga es correcta aparecerá el siguiente mensaje:

```text
Base de datos cargada correctamente.
```

Luego se mostrará el menú principal del chatbot.

---

## Flujo General del Sistema

```text
Inicio
↓
Usuario selecciona opción
↓
Bot consulta Excel
↓
¿Existe información?
├─ No → Informar resultado negativo
└─ Sí → Mostrar información
        ↓
¿Modificar información?
├─ Sí → Actualizar Excel
└─ No
↓
Fin
```

---

## Persistencia de Datos

La aplicación utiliza una plantilla Excel como mecanismo de persistencia.

Los cambios realizados por el usuario se almacenan directamente en el archivo, incluyendo:

* Reservas.
* Cambios de estado.
* Actualizaciones del stock.

Para evitar errores de escritura, el archivo Excel debe permanecer cerrado mientras se ejecuta el programa.

---

## Manejo de Errores

El sistema contempla diversas situaciones excepcionales, entre ellas:

* Opciones inválidas del menú.
* Ingreso de texto cuando se esperan números.
* Modelos inexistentes.
* Líneas o ubicaciones sin registros.
* Chasis inexistentes.
* Reservas sobre unidades no disponibles.
* Imposibilidad de guardar cambios cuando el Excel está abierto.

---

## BPMN

El proceso fue modelado mediante BPMN 2.0, diferenciando claramente las tareas del usuario y las tareas automáticas del sistema.

Se desarrollaron los diagramas:

* Proceso actual (AS-IS).
* Proceso optimizado (TO-BE).

---

## Herramientas de Inteligencia Artificial Utilizadas

Durante el desarrollo del proyecto se utilizaron herramientas de inteligencia artificial como apoyo técnico y documental.

Se empleó ChatGPT para:

* Corrección y optimización del código.
* Generación de ejemplos BPMN.
* Elaboración de documentación.
* Identificación y resolución de errores.
* Generación de pruebas y casos de uso.

Las capturas correspondientes se incluyen dentro de la documentación del trabajo.

---

## Autor/es

Trabajo realizado por:

**Martín Alejandro Sánchez**

Tecnicatura Universitaria en Programación a Distancia.

Universidad Tecnológica Nacional.

---

## Conclusión

El Chatbot Nordemaq demuestra cómo la integración entre el análisis de procesos, la programación y la gestión de datos puede transformarse en una solución concreta para optimizar tareas administrativas. El proyecto permitió aplicar conocimientos interdisciplinarios y desarrollar una herramienta funcional orientada a resolver una problemática real dentro de una organización.

---
