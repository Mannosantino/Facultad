from validaciones import validar_rango
from rich.console import Console
from rich.panel import Panel

console = Console()


# funcion que imprime las opciones del menu principal
def menu_principal():
    opciones = (
        "[bold]1.[/bold] Dar de alta un alumno\n"
        "[bold]2.[/bold] Consultar un alumno por código\n"
        "[bold]3.[/bold] Modificar un alumno\n"
        "[bold]4.[/bold] Eliminar un alumno\n"
        "[bold]5.[/bold] Mostrar todos los alumnos\n"
        "[bold]6.[/bold] Consultar alumnos por turno\n"
        "[bold]7.[/bold] Ver datos estadísticos\n"
        "[bold]8.[/bold] Salir"
    )

    console.print(Panel(
        opciones,
        title="[bold cyan]SISTEMA DE GESTIÓN ACADÉMICA - UADE[/bold cyan]",
        border_style="cyan"
    ))

    return validar_rango(1, 8)
