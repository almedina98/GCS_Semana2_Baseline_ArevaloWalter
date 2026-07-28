import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.inventario import Inventario

inventario = Inventario()
inventario.agregar_producto("P001", "Teclado", 10, 25.00)

resultado = inventario.buscar_producto("P001")

assert resultado is not None
assert resultado["nombre"] == "Teclado"
assert inventario.actualizar_cantidad("P001", 15) is True
assert inventario.buscar_producto("P001")["cantidad"] == 15

print("Prueba básica ejecutada correctamente.")
