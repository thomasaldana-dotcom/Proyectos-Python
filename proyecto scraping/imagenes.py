import bs4
import requests

resultado = requests.get("https://www.escueladirecta.com/blog/260007/encapsulamiento")

sopa = bs4.BeautifulSoup(resultado.text, "lxml")

imagenes = sopa.select(".course-box-image")[0]["src"]

imagen_curso = requests.get(imagenes)


f = open("imagen_curso.jpg", "wb")
f.write(imagen_curso.content)
f.close()






