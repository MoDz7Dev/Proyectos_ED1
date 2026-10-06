"""Cola Circular — buffer acotado con índices que dan la vuelta.

A diferencia de la cola enlazada, esta cola usa un **array de tamaño
fijo** con dos punteros (``_frente`` y ``_fondo``) que avanzan con
aritmética módulo, reutilizando las posiciones vacadas. Esto evita
"desperdiciar" espacio al desencolar.

Aplicación en el simulador: rutas de despacho cíclicas que parten y
regresan al almacén.
"""

from __future__ import annotations

from typing import Any, Optional


class ColaCircularVaciaError(Exception):
    """Se lanza al intentar desencolar una cola circular vacía."""


class ColaCircularLlenaError(Exception):
    """Se lanza al intentar encolar con el buffer lleno."""


class ColaCircular:
    """Cola circular estática con buffer acotado y punteros modulares.

    Los punteros ``_frente`` y ``_fondo`` avanzan con ``% capacidad``,
    por lo que al llegar al final del array vuelven al inicio.

    Todas las operaciones son **O(1)**. La capacidad es fija.

    Ejemplo:
        >>> cola = ColaCircular(3)
        >>> cola.encolar(10)
        >>> cola.encolar(20)
        >>> cola.desencolar()
        10
        >>> cola.encolar(30)   # reutiliza la posición del 10
    """

    def __init__(self, capacidad: int) -> None:
        """Crea una cola circular con capacidad fija.

        Args:
            capacidad: Tamaño máximo del buffer (debe ser > 0).

        Raises:
            ValueError: Si la capacidad no es mayor a cero.
        """
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor a 0")
        self._datos: list = [None] * capacidad
        self._capacidad: int = capacidad
        self._frente: int = 0
        self._fondo: int = 0
        self._tamanio: int = 0

    @property
    def capacidad(self) -> int:
        """Retorna la capacidad máxima de la cola."""
        return self._capacidad

    def encolar(self, dato: Any) -> None:
        """Agrega un elemento al fondo; el índice da la vuelta.

        Complejidad temporal: **O(1)**.

        Args:
            dato: Elemento a encolar.

        Raises:
            ColaCircularLlenaError: Si el buffer está lleno.
        """
        if self.esta_llena():
            raise ColaCircularLlenaError(
                f"Cola circular llena (capacidad={self._capacidad})"
            )
        self._datos[self._fondo] = dato
        self._fondo = (self._fondo + 1) % self._capacidad
        self._tamanio += 1

    def desencolar(self) -> Any:
        """Elimina y retorna el elemento del frente.

        Complejidad temporal: **O(1)**.

        Returns:
            El dato al frente de la cola.

        Raises:
            ColaCircularVaciaError: Si la cola no tiene elementos.
        """
        if self.esta_vacia():
            raise ColaCircularVaciaError("La cola circular está vacía")
        dato = self._datos[self._frente]
        self._datos[self._frente] = None  # libera la referencia
        self._frente = (self._frente + 1) % self._capacidad
        self._tamanio -= 1
        return dato

    def ver_frente(self) -> Any:
        """Retorna el elemento del frente sin quitarlo.

        Complejidad temporal: **O(1)**.

        Returns:
            El dato al frente de la cola.

        Raises:
            ColaCircularVaciaError: Si la cola no tiene elementos.
        """
        if self.esta_vacia():
            raise ColaCircularVaciaError("La cola circular está vacía")
        return self._datos[self._frente]

    def esta_vacia(self) -> bool:
        """Indica si la cola no contiene elementos.

        Returns:
            ``True`` si la cola está vacía.
        """
        return self._tamanio == 0

    def esta_llena(self) -> bool:
        """Indica si el buffer está lleno.

        Returns:
            ``True`` si no cabe ningún elemento más.
        """
        return self._tamanio == self._capacidad

    def a_lista(self) -> list:
        """Convierte la cola a lista de frente a fondo.

        Complejidad temporal: **O(n)**.

        Returns:
            Los elementos en orden de atención.
        """
        elementos = []
        indice = self._frente
        for _ in range(self._tamanio):
            elementos.append(self._datos[indice])
            indice = (indice + 1) % self._capacidad
        return elementos

    def __len__(self) -> int:
        """Retorna la cantidad de elementos de la cola."""
        return self._tamanio

    def __str__(self) -> str:
        """Representación de la cola circular de frente a fondo."""
        elementos = [str(dato) for dato in self.a_lista()]
        if not elementos:
            return "ColaCircular(vacía)"
        return (
            "ColaCircular(frente→ [" + ", ".join(elementos)
            + f"] ←fondo, cap={self._capacidad})"
        )
