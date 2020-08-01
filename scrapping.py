# -*- coding: utf-8 -*-
__author__ = 'Gerardo Mixteco'

from bs4 import BeautifulSoup
import requests

URL_BASE = "http://127.0.0.1:8000/"
MAX_PAGES = 20
counter = 0

for i in range(1, MAX_PAGES):

    # Construyo la URL
    if i > 1:
        url = "%spage/%d/" % (URL_BASE, i)
    else:
        url = URL_BASE

    # Realizamos la petición a la web
    req = requests.get(url)
    # Comprobamos que la petición nos devuelve un Status Code = 200
    statusCode = req.status_code
    if statusCode == 200:

        # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
        html = BeautifulSoup(req.text, "html.parser")

        # Obtenemos todos los divs donde estan las entradas
        entradas = html.find_all('div', {'class': 'col-md-6'})

        # Recorremos todas las entradas para extraer el título, autor y fecha
        for entrada in entradas:
            counter += 1
            Nombre = entrada.find('ul', {'class': 'list mb-3'}).getText()
            #precio = entrada.find('span', {'class': 'price price-has-discount'}).getText()
            #precio_real = entrada.find('span', {'class': 'regular-price'}).getText()

            # Imprimo el Título, Autor y Fecha de las entradas
            print "%d - %s " % (counter, Nombre)

    else:
        # Si ya no existe la página y me da un 400
        break