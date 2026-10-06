"""Interfaces abstractas (ABC) para las estructuras lineales del curso.

Define el contrato común que deben cumplir todas las estructuras
de datos lineales del simulador: Pila, Cola, Cola de Prioridad,
Cola Circular y Listas Enlazadas.

Referencia: Unidad 0 — Clases abstractas con ``abc``.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class EstructuraLineal(ABC):
    """Interfaz base para todas las estructuras lineales.

    Obliga a cada estructura concreta a implementar las operaciones
    fundamentales de inserción, eliminación y consulta.
    """

    @abstractmethod
    def insertar(self, dato: Any) -> None:
        """Inserta un elemento en la estructura."""

    @abstractmethod
    def eliminar(self) -> Any:
        """Elimina y retorna el elemento según la política."""

    @abstractmethod
    def ver(self) -> Any:
        """Retorna el elemento según la política sin eliminarlo."""

    @abstractmethod
    def esta_vacia(self) -> bool:
        """Indica si la estructura no contiene elementos."""

    @abstractmethod
    def __len__(self) -> int:
        """Retorna la cantidad de elementos."""

    def __bool__(self) -> bool:
        """Permite usar la estructura en condiciones ``if``."""
        return not self.esta_vacia()

    def __str__(self) -> str:
        """Representación legible de la estructura."""
        return f"{type(self).__name__}(tamaño={len(self)})"
