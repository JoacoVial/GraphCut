Las instrucciones para utilizar el software programado por el grupo FSOCIETY, en la
cual se segmentan las 3 imágenes seleccionadas por el grupo para las simulaciones, son las
siguientes:
01-. Asegurarse de tener todas las librerías de Python3 que utiliza el software,
las cuales se encuentran enumeradas en el archivo librerias.txt.
02-. Ejecutar el script flujo.py.
03-. Seleccionar 2 puntos de la imagen, estos serán las esquinas superior izquierda e
inferior derecha del recorte que se le hará a la imagen.
04-. Presionar el botón escape.
05-. Seleccionar los puntos del objeto a segmentar en el recorte que aparecerá en
pantalla.
06-. Presionar el botón escape.
07-. Seleccionar los puntos del fondo en el recorte que aparecerá en pantalla.
08-. Presionar el botón escape.
09-. Observar los resultados.
10-. Presionar el botón escape.
11-. Repetir los pasos 2 a 10 con las siguientes 2 imágenes.


Las funcionalidades de cada archivo se ven a continuación:

-Prob.py sirve para calcular la probabilidad de un pixel de pertenecer al objeto o al fondo.
-cap.py se utiliza para generar la ventana en donde el usuario debe seleccionar los pixeles.
-corte.py se utiliza para hacer el recorte a la imagen en la zona seleccionada por el usuario.
-flujo.py tiene la función para generar el grafo, ejecutar el algoritmo y encontrar el mínimo corte.
-pintar.py se encarga de pintar el mínimo corte con color rojo.
