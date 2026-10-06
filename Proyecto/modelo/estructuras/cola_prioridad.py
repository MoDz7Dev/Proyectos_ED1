"""Cola de Prioridad — inserción ordenada por prioridad con nodos.

Los elementos se insertan en su posición correcta según la prioridad
(mayor número = mayor prioridad), por lo que ``desencolar`` siempre
entrega el elemento de mayor prioridad en **O(1)**.

Aplicación en el simulador: envíos urgentes que se despachan antes
que los normales.

Referencia: ``codigo_base_referencial.py`` adaptado a PEP 8.
"""

from __future__ import annotations

from typing import Any, Optional

from modelo.estructuras.nodo import Nodo


class ColaPrioridadVaciaError(Exception):
    """Se lanza al operar sobre una cola de prioridad vacía."""


class ColaPrioridad:
    """Cola de prioridad con nodos ordenados de mayor a menor.

    La inserción es **O(n)** porque debe ubicar el nodo en su
    posición; la extracción del elemento de mayor prioridad es
    **O(1)**.

    Ejemplo:
        >>> cola = ColaPrioridad()
        >>> cola.encolar("normal", prioridad=1)
        >>> cola.encolar("urgente", prioridad=5)
        >>> cola.desencolar()
        'urgente'
    """

    def __init__(self) -> None:
        """Crea una cola de prioridad vacía."""
        self._cabeza: Optional[Nodo] = None
        self._tamanio: int = 0

    @property
    def prioridad_maxima(self) -> Optional[int]:
        """Retorna la prioridad más alta en cola (o ``None``)."""
        if self._cabeza is None:
            return None
        return self._cabeza.dato["prioridad"]

    def encolar(self, dato: Any, prioridad: int) -> None:
        """Inserta un elemento ordenado por prioridad.

        Complejidad temporal: **O(n)**.

        Args:
            dato: Elemento a encolar.
            prioridad: Número entero; mayor = mayor prioridad.

        Raises:
            TypeError: Si ``prioridad`` no es un entero.
        """
        if not isinstance(prioridad, int):
            raise TypeError("La prioridad debe ser un entero")

        nuevo_nodo = Nodo({"dato": dato, "prioridad": prioridad})

        # Caso 1: cola vacía o prioridad máxima
        if self._cabeza is None or prioridad > self._cabeza.dato["prioridad"]:
            nuevo_nodo.siguiente = self._cabeza
            self._cabeza = nuevo_nodo
            self._tamanio += 1
            return

        # Caso 2: buscar la posición (manteniendo orden estable)
        actual = self._cabeza
        while (
            actual.siguiente is not None
            and actual.siguiente.dato["prioridad"] >= prioridad
        ):
            actual = actual.siguiente

        nuevo_nodo.siguiente = actual.siguiente
        actual.siguiente = nuevo_nodo
        self._tamanio += 1

    def desencolar(self) -> Any:
        """Elimina y retorna el elemento de mayor prioridad.

        Complejidad temporal: **O(1)**.

        Returns:
            El dato del elemento con mayor prioridad.

        Raises:
            ColaPrioridadVaciaError: Si la cola no tiene elementos.
        """
        if self.esta_vacia():
            raise ColaPrioridadVaciaError("La cola de prioridad está vacía")
        dato = self._cabeza.dato["dato"]
        self._cabeza = self._cabeza.siguiente
        self._tamanio -= 1
        return dato

    def ver_frente(self) -> Any:
        """Retorna el elemento de mayor prioridad sin quitarlo.

        Complejidad temporal: **O(1)**.

        Returns:
            El dato del elemento con mayor prioridad.

        Raises:
            ColaPrioridadVaciaError: Si la cola no tiene elementos.
        """
        if self.esta_vacia():
            raise ColaPrioridadVaciaError("La cola de prioridad está vacía")
        return self._cabeza.dato["dato"]

    def esta_vacia(self) -> bool:
        """Indica si la cola no contiene elementos.

        Returns:
            ``True`` si la cola está vacía.
        """
        return self._cabeza is None

    def a_lista(self) -> list:
        """Convierte la cola a lista de mayor a menor prioridad.

        Complejidad temporal: **O(n)**.

        Returns:
            Lista de tuplas ``(dato, prioridad)`` ordenada.
        """
        elementos = []
        actual = self._cabeza
        while actual is not None:
            elementos.append(
                (actual.dato["dato"], actual.dato["prioridad"])
            )
            actual = actual.siguiente
        return elementos

    def __len__(self) -> int:
        """Retorna la cantidad de elementos de la cola."""
        return self._tamanio

    def __str__(self) -> str:
        """Representación de la cola de prioridad de mayor a menor."""
        elementos = [
            f"{dato}(p={prio})"
            for dato, prio in self.a_lista()
        ]
        if not elementos:
            return "ColaPrioridad(vacía)"
        return "ColaPrioridad(mayor→ [" + ", ".join(elementos) + "])"
