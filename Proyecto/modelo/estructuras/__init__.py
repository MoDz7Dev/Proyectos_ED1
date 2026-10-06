"""Estructuras de datos implementadas manualmente con nodos.

Todas las estructuras evitan depender de las colecciones nativas de
Python (list, dict, deque) como contenedor principal de sus elementos.
"""

from modelo.estructuras.base import EstructuraLineal
from modelo.estructuras.nodo import Nodo
from modelo.estructuras.pila import Pila, PilaVaciaError
from modelo.estructuras.cola import Cola, ColaVaciaError
from modelo.estructuras.lista_doble import ListaDoblementeEnlazada
from modelo.estructuras.cola_prioridad import (
    ColaPrioridad,
    ColaPrioridadVaciaError,
)
from modelo.estructuras.cola_circular import (
    ColaCircular,
    ColaCircularVaciaError,
    ColaCircularLlenaError,
)
from modelo.estructuras.undo_redo import UndoRedoManager

__all__ = [
    "EstructuraLineal",
    "Nodo",
    "Pila",
    "PilaVaciaError",
    "Cola",
    "ColaVaciaError",
    "ListaDoblementeEnlazada",
    "ColaPrioridad",
    "ColaPrioridadVaciaError",
    "ColaCircular",
    "ColaCircularVaciaError",
    "ColaCircularLlenaError",
    "UndoRedoManager",
]

