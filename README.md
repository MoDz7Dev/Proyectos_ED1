# 📚 Proyectos_ED1 — Estructura de Datos I

> Repositorio de proyectos del curso **Estructura de Datos I — R1**

| | |
|---|---|
| **Estudiante** | Arancibia Añez Raúl Javier |
| **Registro** | 223041556 |
| **Materia** | Estructura de Datos I — R1 |
| **Docente** | Prof. Juan Carlos Peinado |
| **Repositorio** | [MoDz7Dev/Proyectos_ED1](https://github.com/MoDz7Dev/Proyectos_ED1) |

---

## 🎯 Descripción

Este repositorio reúne las entregas y avances de los proyectos del curso de
Estructura de Datos I, aplicando los contenidos de las unidades:

- **Unidad 0** — Estándares y buenas prácticas de codificación (PEP 8)
- **Unidad I** — Modelos de representación de datos
- **Unidad II** — ADT Polinomio, Conjuntos y Matriz Dispersa
- **Unidad III** — Estructuras lineales: listas, pilas, colas y bicolas
- **Unidad IV** — Algoritmos: recorridos y manipulación de estructuras

## 📂 Contenido del repositorio

| Carpeta | Descripción | Estado |
|---|---|---|
| [`Proyecto/`](./Proyecto/) | **Simulador de Centro Logístico de Distribución y Rutas de Despacho** — proyecto integrador con Flet y arquitectura MVC | 🟡 En desarrollo (1er avance) |
| [`Tareas/`](./Tareas/) | Ejercicios prácticos por unidad (listas enlazadas, etc.) | 🟢 Continuo |

## 📦 Proyecto principal: Simulador Logístico

Aplicación multiplataforma construida con **Flet** y arquitectura **MVC**
(Modelo-Vista-Controlador) que simula la operación de un centro logístico,
implementando manualmente (con nodos y referencias, sin colecciones nativas
de Python) las estructuras de datos del curso:

| Estructura | Política | Uso en el simulador | Estado |
|---|---|---|---|
| Cola | FIFO | Despacho de paquetes | ✅ |
| Pila | LIFO | Deshacer / Rehacer (Undo/Redo) | 🟡 |
| Lista doblemente enlazada | Acceso bidireccional | Historial de despachos | ✅ |
| Cola de prioridad | Prioridad | Envíos urgentes | ⏳ |
| Lista circular | Bucle circular | Rutas de despacho | ⏳ |

Para más detalles, instrucciones de ejecución y estructura interna, ver el
[README del proyecto](./Proyecto/README.md).

## ⚙️ Requisitos

- Python 3.10 o superior
- [Flet](https://flet.dev) 1.0 o superior

```bash
pip install flet
```

### Ejecutar el proyecto

```bash
cd Proyecto
python main.py
```

## 🗂️ Estructura general

```
Proyectos_ED1/
├── README.md                 # Este archivo
├── Proyecto/                 # Simulador Logístico (Flet + MVC)
│   ├── main.py
│   ├── modelo/               # Estructuras de datos y dominio
│   ├── vista/                # Interfaz Flet
│   ├── controlador/          # Coordina vista y modelo
│   ├── datos/                # Persistencia (pendiente)
│   └── tests/                # Pruebas (pendiente)
└── Tareas/                   # Ejercicios prácticos
```

## 📈 Estado general

- [x] Repositorio inicializado y vinculado a GitHub
- [x] Estructura MVC del proyecto principal
- [x] Pila, Cola y Lista doblemente enlazada con nodos manuales
- [ ] Cola de prioridad y lista circular
- [ ] Undo/Redo con doble pila
- [ ] Persistencia JSON
- [ ] Pruebas unitarias

## 📚 Referencias

- Repositorio del curso: [profjcp/INF220-EstructurasDatos1](https://github.com/profjcp/INF220-EstructurasDatos1)
- Guía de estilo: [PEP 8](https://peps.python.org/pep-0008/)
- Documentación de Flet: [flet.dev](https://flet.dev/docs/)

---

> **Autor:** Arancibia Añez Raúl Javier · **Registro:** 223041556
> **Materia:** Estructura de Datos I — R1 · 2026
