# keyword arguments
def get_product(**datos):
    print(datos)
    print(datos["id"], datos["name"])


get_product(id="2344675422345799",
            name="iPhone",
            desc="Telefono inteligente")
