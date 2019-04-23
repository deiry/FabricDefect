# FabricDefect

Cuerpo del proyecto
- main.py: Notebook principal, es el único notebook que se ejecutara para ver los resultados del entrenamiento.
- img_ids.csv: Archivo que contiene los nombre de las imágenes.
- fabric_data.py: Métodos encargados de extraer las imágenes de la nube


Contexto
En la industria textil es necesario la detección de defectos en tejidos, lo cual es importante para un
adecuado control de calidad. Esta detección se realiza generalmente de forma visual, teniendo de
este modo poca precisión para aplicaciones industriales [1]. Por ello en este proyecto se plantea
un método automatizado que detecte defectos en telas mediante un sistema de recuperación de
imágenes basada en contenido (CBIR). Su algoritmo consiste en primero extraer características de
una base de datos de imágenes de telas de algodón de diferentes prendas de vestir, y almacenar
estas características [2], por consiguiente, se calcula las características de una imagen consulta y
así reconstruir una imagen con las características más cercanas.





[1] Mei, S., Wang, Y., y Wen, G. (2018). Detección automática de defectos de la tela con un modelo de red de autoencoder de supresión convolucional de múltiples escalas. Sensores (Basilea, Suiza) , 18 (4), 1064. doi: 10.3390 / s18041064.


[2] https://blog.sicara.com/keras-tutorial-content-based-image-retrieval-convolutional-denoising-autoencoder-dc91450cc511


[3] Artem Babenko1,3 , Anton Slesarev1 , Alexandr Chigorin1 , Victor Lempitsky Neural Codes for Image Retrieval
