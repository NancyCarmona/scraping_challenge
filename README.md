Parte 1:
El codigo de la parte 1 se encuentra en el archivo reto1.py.
Se requiere tener instalada la libreria requests, se encuentra en requirements_reto1.txt

Parte 2:
Ya que el sitio web tarda mucho en mostrar el listado completo de los productos, se usó Selenium para esperar y simular scrolling ya que
el sitio lo requeria para continuar mostrando productos.
Se indican las librerias necesarias en requirements.txt y tambien se incluye Dockerfile.
La url para obtener los datos es: http://172.17.0.2:5000/get_elements
Datos de prueba:
{
    "url":"https://www.tiendasjumbo.co/supermercado/despensa/aceite"
}

Respuesta de prueba:
{
    "products": [
        {
            "nombre": "Aceite Puroil vegetal x3000ml ",
            "price": "$ 20.890",
            "promo_price": "$ 20.890"
        },
        {
            "nombre": "Aceite Riquisimo garrafa x3000ml ",
            "price": "$ 29.450",
            "promo_price": "$ 21.840"
        },
        {
            "nombre": "Aceite Ybarra oliva extra virgen x1L ",
            "price": "$ 63.890",
            "promo_price": "$ 60.695"
        },
        {
            "nombre": "Aceite Cuisine&Co girasol x3L ",
            "price": "$ 39.490",
            "promo_price": "$ 37.515"
        },
        {
            "nombre": "Aceite Premier girasol x2700ml ",
            "price": "$ 52.290",
            "promo_price": "$ 52.290"
        },
        {
            "nombre": "Aceite Ybarra oliva extra virgen x3L ",
            "price": "$ 161.590",
            "promo_price": "$ 153.510"
        },
        {
            "nombre": "Aceite Bucatti oliva extra virgen x750ml ",
            "price": "$ 53.550",
            "promo_price": "$ 53.550"
        },
        {
            "nombre": "Aceite Premier girasol x900ml ",
            "price": "$ 18.450",
            "promo_price": "$ 18.450"
        },
        {
            "nombre": "Aceite Canola Life puro x3L ",
            "price": "$ 73.690",
            "promo_price": "$ 73.690"
        },
        {
            "nombre": "Aceite Oleocali garrafa x3000ml ",
            "price": "$ 30.500",
            "promo_price": "$ 21.840"
        },
        {
            "nombre": "Aceite Canola Life bajo en grasa saturada x1L ",
            "price": "$ 28.000",
            "promo_price": "$ 28.000"
        },
        {
            "nombre": "Aceite Diana vitaminas x3000ml ",
            "price": "$ 32.400",
            "promo_price": "$ 32.400"
        },
        {
            "nombre": "Aceite Gourmet Familia multiusos x900ml ",
            "price": "$ 19.860",
            "promo_price": "$ 19.860"
        },
        {
            "nombre": "Aceite Gourmet familia multiusos x2und x1800ml c-u ",
            "price": "$ 69.900",
            "promo_price": "$ 69.900"
        },
        {
            "nombre": "Aceite Canola Life bajo en grasa saturada x2L ",
            "price": "$ 53.200",
            "promo_price": "$ 53.200"
        }
    ],
    "url": "https://www.tiendasjumbo.co/supermercado/despensa/aceite"
}


comandos:
docker build -t scraping_challenge .

docker run  --rm -p 5000:5000 --name challenge_service scraping_challenge