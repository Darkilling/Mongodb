db = con ()
coleccion = db.restaurants

building = input("ingrese numero del edificio: ")
coord_lat = input("ingrese latitud de la ubicacion: ")
coord_long = input("ingrese longitud de la ubicacion: ")
street = input("ingresa nombre de la calle: ")
zipcode = input("ingres codigo postal: ")
borough = input("ingrese la comuna del restaurante: ")
cuisine = input("ingrese el tipo de cosina: ")
name = input("ingrese el nombre del restaurante: ")
restaurant_id = input("ingrese el ID del restaurante: ")



nuevo_documento = {
    "address": {
        "building": building,
        "coord": [coord_lat,coord_long],
        "street": street,
        "zipcode": "10018"
    },
    "borough": "manhattan",
    "cuisine": "other",
    "grades": [],
    "name": "",
    "restaurant_id": restaurant_id
}

