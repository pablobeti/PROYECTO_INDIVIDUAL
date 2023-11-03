# <h1 align=center> **STEAM MACHINE LEARNING** </h1>
# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>
# <h1 align=center> **PABLO BETI** </h1>

<p align="center">
  <img src="src/steam.jpeg">
</p>

## Introducción

¡Bienvenidos a este proyecto de MLOPS de steam!, este trabajo se realizó en base al supuesto de que steam nos requiere un MVP para una creacion de un modelo de recomendacion de juegos. 

## Propuesta
Por medio de la disponibilizacion de datos a traves de un trabajo de ETL y un EDA se modelo un sistema de recomendacion en base a la similitud del coseno, utilizando la libreria scikit learn.
Dicho trabajo se puso a disposicion de consultas mediante una API subida en Render. Ademas de una serie de consultas solicitadas.

def PlayTimeGenre( genero : str ): Debe devolver año con mas horas jugadas para dicho género.

def UserForGenre( genero : str ): Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.

def UsersRecommend( año : int ): Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)

def UsersNotRecommend( año : int ): Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)

def sentiment_analysis( año : int ): Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.

def recomendacion_juego( id de producto ): Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.

def recomendacion_usuario( id de usuario ): Ingresando el id de un usuario, deberíamos recibir una lista con 5 juegos recomendados para dicho usuario.

# Conclusión

En este proyecto se posiciono y cumplio las funciones de un data Engine, realizando las limpiezas de los datasets provistos, dicha limpieza se encuentra en el notebook **ETL** y una descripcion de los datos y del desarrollo de la funcion de machine learning en el notebook de **EDA_ML**.

# LINKS
Dejo a disposicion el link del video en el que se muestra como quedo el servicio de consultas de la API subida a render 
Dejo video demostracion en el siguiente link .



## Tecnologias utilizadas:
**Python - Scikit Learn - Pandas - Fastapi - Render** 

<body>
  <div class="logo-container">
    <img class="logo" src="src/Python-logo-notext.svg.png" width="100" height="100">
  </div>
    <div class="logo-container">
    <img class="logo" src="src/fastapi.png" width="200" height="80">
  </div>
  <div class="logo-container">
    <img class="logo" src="src/pandas.png" width="200" height="100">
  </div>
  <div class="logo-container">
    <img class="logo" src="src/scikit.png" width="200" height="100">
  </div>
    <div class="logo-container">
    <img class="logo" src="src/render.png" width="200" height="100">
  </div>

</body>

##
### Gracias por visitar este proyecto.
##

# Datos de Contacto

## Pablo Raul Ricardo Beti
[LINKEDIN](https://www.linkedin.com/in/pablo-beti-714007265/)

[INSTAGRAM](https://www.instagram.com/pablo_beti/)

##

##