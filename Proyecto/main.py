"""Punto de entrada del Simulador de Centro Logístico (arquitectura MVC).

Ejecutar con:
    python main.py
"""

import flet as ft

from controlador.app_controller import AppController


def main(page: ft.Page) -> None:
    """Configura la página e inicializa el controlador principal."""
    AppController(page).iniciar()


if __name__ == "__main__":
    ft.run(main)
