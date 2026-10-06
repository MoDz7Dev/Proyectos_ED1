"""Controlador de la aplicación.

Conecta la vista (Flet) con el modelo (estructuras y dominio) sin
que ninguno de los dos se conozca directamente.
"""

from __future__ import annotations

import flet as ft

from modelo.dominio.paquete import Paquete
from modelo.estructuras.cola import Cola, ColaVaciaError
from modelo.estructuras.cola_prioridad import ColaPrioridad
from modelo.estructuras.lista_doble import ListaDoblementeEnlazada
from modelo.estructuras.undo_redo import UndoRedoManager
from vista.vista_grafica import VistaGrafica


class AppController:
    """Coordina la interacción entre :class:`VistaGrafica` y el modelo.

    - Registra paquetes nuevos en la cola de despacho (FIFO).
    - Los paquetes urgentes van a la cola de prioridad.
    - Despacha primero lo urgente y después lo normal.
    - Mantiene el historial de despachos en una lista doble.
    - Gestiona deshacer/rehacer con :class:`UndoRedoManager`.
    """

    def __init__(self, page: ft.Page) -> None:
        """Inicializa el controlador con su vista y modelo.

        Args:
            page: Página de Flet donde se renderizará la interfaz.
        """
        self._vista = VistaGrafica(page)
        self._cola_despacho = Cola()
        self._cola_urgentes = ColaPrioridad()
        self._historial = ListaDoblementeEnlazada()
        self._undo_redo = UndoRedoManager()

    def iniciar(self) -> None:
        """Muestra la interfaz inicial y registra los manejadores."""
        self._vista.asignar_controlador(self)
        self._vista.construir()
        self.actualizar_vista()

    def registrar_paquete(self, destino: str, peso_txt: str,
                          urgente: bool) -> None:
        """Valida la entrada y registra un paquete en la cola.

        Args:
            destino: Ciudad o dirección de destino.
            peso_txt: Peso en kilogramos ingresado como texto.
            urgente: Si el paquete debe despacharse con prioridad.
        """
        destino = destino.strip()
        if not destino:
            self._vista.mostrar_mensaje(
                "Debe ingresar un destino válido.", ft.Colors.RED
            )
            return

        try:
            peso = float(peso_txt) if peso_txt.strip() else 0.0
            if peso < 0:
                raise ValueError
        except ValueError:
            self._vista.mostrar_mensaje(
                "El peso debe ser un número mayor o igual a 0.",
                ft.Colors.RED,
            )
            return

        paquete = Paquete(destino=destino, peso_kg=peso, urgente=urgente)
        if urgente:
            self._cola_urgentes.encolar(paquete, prioridad=5)
        else:
            self._cola_despacho.encolar(paquete)

        self._undo_redo.aplicar(("registrar", paquete.identificador))
        self._vista.mostrar_mensaje(
            f"Paquete {paquete.identificador} registrado hacia "
            f"{destino}.",
            ft.Colors.GREEN,
        )
        self.actualizar_vista()

    def despachar_siguiente(self) -> None:
        """Despacha primero los urgentes; después, los normales (FIFO)."""
        try:
            if not self._cola_urgentes.esta_vacia():
                paquete = self._cola_urgentes.desencolar()
            else:
                paquete = self._cola_despacho.desencolar()
        except ColaVaciaError:
            self._vista.mostrar_mensaje(
                "No hay paquetes pendientes de despacho.",
                ft.Colors.ORANGE,
            )
            return

        self._historial.insertar_final(paquete)
        self._undo_redo.aplicar(("despachar", paquete.identificador))
        self._vista.mostrar_mensaje(
            f"Despachado {paquete.identificador} hacia {paquete.destino}.",
            ft.Colors.GREEN,
        )
        self.actualizar_vista()

    def deshacer(self) -> None:
        """Deshace la última acción registrada."""
        accion = self._undo_redo.deshacer()
        if accion is None:
            self._vista.mostrar_mensaje(
                "No hay acciones para deshacer.", ft.Colors.ORANGE
            )
            return
        self._vista.mostrar_mensaje(
            f"Acción deshecha: {accion[0]} {accion[1]}.",
            ft.Colors.BLUE,
        )
        self.actualizar_vista()

    def rehacer(self) -> None:
        """Rehace la última acción deshecha."""
        accion = self._undo_redo.rehacer()
        if accion is None:
            self._vista.mostrar_mensaje(
                "No hay acciones para rehacer.", ft.Colors.ORANGE
            )
            return
        self._vista.mostrar_mensaje(
            f"Acción rehecha: {accion[0]} {accion[1]}.",
            ft.Colors.BLUE,
        )
        self.actualizar_vista()

    def actualizar_vista(self) -> None:
        """Refresca la vista con el estado actual del modelo."""
        urgentes = [d for d, _ in self._cola_urgentes.a_lista()]
        normales = self._cola_despacho.a_lista()
        self._vista.actualizar_estado(
            cola=urgentes + normales,
            historial=self._historial.a_lista_invertida(),
            pendientes=len(self._cola_urgentes)
            + len(self._cola_despacho),
            despachados=len(self._historial),
            puede_deshacer=self._undo_redo.puede_deshacer(),
            puede_rehacer=self._undo_redo.puede_rehacer(),
        )
