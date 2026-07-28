class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, codigo, nombre, cantidad, precio):
        producto = {
            "codigo": codigo,
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio,
        }
        self.productos.append(producto)
        return producto

    def listar_productos(self):
        return self.productos

    def buscar_producto(self, codigo):
        for producto in self.productos:
            if producto["codigo"] == codigo:
                return producto
        return None

    def actualizar_cantidad(self, codigo, nueva_cantidad):
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False
        producto["cantidad"] = nueva_cantidad
        return True


def main():
    inventario = Inventario()
    inventario.agregar_producto("P001", "Teclado", 10, 25.00)
    print("Hello baseline")
    print("Productos registrados:")
    print(inventario.listar_productos())


if __name__ == "__main__":
    main()
