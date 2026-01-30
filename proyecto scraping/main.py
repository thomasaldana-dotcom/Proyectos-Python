import bs4
import requests

#crear url sin numnero de pagina
url = "https://books.toscrape.com/catalogue/page-{}.html"

#lista de libros con 4 o 5 estrellas
libros_rating_4 = []
libros_rating_5 = []

#iterar en las paginas que tienen los libros 

for pagina in range(1, 21):
    #crear sopa en cada pagina
    url_pagina = url.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, "lxml")

    #seleccionar datos de libros
    libros = sopa.select(".product_pod")

    #iterar libros
    for libro in libros:
        #chquear si tiene 4 o 5 estrellas
        if len(libro.select(".star-rating.Four")) != 0:
            #guardar titutlo en variable
            titulo_libro = libro.select("a")[1]["title"]
            libros_rating_4.append(titulo_libro)

            print("Libros con 4 estrellas\n")
            
            for n,m in enumerate(libros_rating_4):
                print(n,m)
        
        elif len(libro.select(".star-rating.Five")) != 0:
            titulo_libro = libro.select("a")[1]["title"]
            libros_rating_5.append(titulo_libro)

            print("Libros con 5 estrellas\n")

            for n,m in enumerate(libros_rating_5):
                print(n,m)

