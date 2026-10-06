"""Undo/Redo Manager — gestor de deshacer/rehacer con doble pila.

Dos pilas acopladas:

- **Pila de deshacer**: guarda el estado anterior del sistema.
- **Pila de rehacer**: guarda los estados que se deshicieron y que
  pueden volver a aplicarse.

Flujo:

    accion aplicada ──▶ pila_deshacer
    deshacer         ──▶ pila_deshacer.pop() ──▶ pila_rehacer.push()
    rehacer          ──▶ pila_rehacer.pop() ──▶ pila_deshacer.push()
"""

from __future__ import annotations

from typing import Any, Optional

from modelo.estructuras.pila import Pila


class UndoRedoManager:
    """Gestor de deshacer/rehacer basado en dos pilas acopladas.

    La pila ``_deshacer`` contiene las acciones ya aplicadas, la más
    reciente en el tope. La pila ``_rehacer`` contiene las acciones
    deshechas, listas para re-aplicarse.

    Ejemplo:
        >>> gestor = UndoRedoManager()
        >>> gestor.aplicar("mover_paquete_A")
        >>> gestor.puede_deshacer()
        True
        >>> gestor.deshacer()
        'mover_paquete_A'
        >>> gestor.puede_rehacer()
        True
    """

    def __init__(self) -> None:
        """Crea el gestor con ambas pilas vacías."""
        self._deshacer = Pila()
        self._rehacer = Pila()

    def aplicar(self, accion: Any) -> None:
        """Registra una acción recién aplicada.

        Al aplicar una acción nueva se limpia la pila de rehacer
        (no se puede rehacer algo que ya fue deshecho y reemplazado).

        Complejidad temporal: **O(1)**.

        Args:
            accion: Acción o estado a registrar en el historial.
        """
        self._deshacer.apilar(accion)
        self._limpiar_rehacer()

    def deshacer(self) -> Optional[Any]:
        """Deshace la última acción y la mueve a la pila de rehacer.

        Complejidad temporal: **O(1)**.

        Returns:
            La acción deshecha, o ``None`` si no hay nada que deshacer.
        """
        if not self.puede_deshacer():
            return None
        accion = self._deshacer.desapilar()
        self._rehacer.apilar(accion)
        return accion

    def rehacer(self) -> Optional[Any]:
        """Rehace la última acción deshecha y la devuelve a deshacer.

        Complejidad temporal: **O(1)**.

        Returns:
            La acción re-hecha, o ``None`` si no hay nada que rehacer.
        """
        if not self.puede_rehacer():
            return None
        accion = self._rehacer.desapilar()
        self._deshacer.apilar(accion)
        return accion

    def puede_deshacer(self) -> bool:
        """Indica si hay acciones disponibles para deshacer.

        Returns:
            ``True`` si la pila de deshacer no está vacía.
        """
        return not self._deshacer.esta_vacia()

    def puede_rehacer(self) -> bool:
        """Indica si hay acciones disponibles para rehacer.

        Returns:
            ``True`` si la pila de rehacer no está vacía.
        """
        return not self._rehacer.esta_vacia()

    @property
    def historial_deshacer(self) -> Pila:
        """Retorna la pila de deshacer (solo lectura)."""
        return self._deshacer

    @property
    def historial_rehacer(self) -> Pila:
        """Retorna la pila de rehacer (solo lectura)."""
        return self._rehacer

    def reiniciar(self) -> None:
        """Vacía ambos historiales."""
        while not self._deshacer.esta_vacia():
            self._deshacer.desapilar()
        while not self._rehacer.esta_vacia():
            self._rehacer.desapilar()

    def _limpiar_rehacer(self) -> None:
        """Vacía la pila de rehacer (acción nueva invalida el redo)."""
        while not self._rehacer.esta_vacia():
            self._rehacer.desapilar()

    def __len__(self) -> int:
        """Retorna la cantidad de acciones en la pila de deshacer."""
        return len(self._deshacer)

    def __str__(self) -> str:
        """Representación legible del gestor."""
        return (
            f"UndoRedoManager(deshacer={len(self._deshacer)}, "
            f"rehacer={len(self._rehacer)})"
        )
