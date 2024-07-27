import json


def cargar_catalogo():
    with open('catalogo_autos.json', 'r') as file:
        return json.load(file)


def imprimir_catalogo(catalogo):
    for auto in catalogo:
        print(
            f"Marca: {auto['Marca']}, Modelo: {auto['Modelo']}, Año: {auto['Año']}, Precio: {auto['Precio']}, Color: {auto['Color']}"
        )


def buscar_por_marca(catalogo, marca):
    return [
        auto for auto in catalogo if auto['Marca'].lower() == marca.lower()
    ]


def buscar_por_rango_precio(catalogo, precio_min, precio_max):
    return [
        auto for auto in catalogo if precio_min <= auto['Precio'] <= precio_max
    ]


if __name__ == "__main__":
    catalogo_autos = cargar_catalogo()

    print("Catálogo completo de autos:")
    imprimir_catalogo(catalogo_autos)

    print("\nBuscar autos por marca (Toyota):")
    autos_toyota = buscar_por_marca(catalogo_autos, "Toyota")
    imprimir_catalogo(autos_toyota)

    print("\nBuscar autos por rango de precio (20000 a 40000):")
    autos_precio_rango = buscar_por_rango_precio(catalogo_autos, 20000, 40000)
    imprimir_catalogo(autos_precio_rango)
