import pandas as pd
from fastapi import FastAPI
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

# Definición de rutas y funciones de manejo aquí


# Carga el DataFrame desde el archivo CSV
consulta1 = pd.read_csv('dataset/consulta1.csv')
consulta2 = pd.read_csv('dataset/consulta2.csv')
steam_games = pd.read_csv('dataset/recomendacion.csv')

@app.get("/playtime_genre/{genero}")
def PlayTimeGenre(genero):
    ''' def PlayTimeGenre( genero : str ): Devuelve el año con mas horas jugadas para dicho género '''
    global consulta2  # Acceso a la variable global consulta2
    try:
        # Filtrar juegos por el género específico en el DataFrame unido
        filtered_games = consulta2[consulta2['genres'] == genero]

        if not filtered_games.empty:
            # Encontrar el año con más horas jugadas para el género dado
            year_with_most_hours_played = filtered_games.groupby('release_year')['playtime_forever'].sum().idxmax()

            return {"Año de lanzamiento con más horas jugadas para " + genero: int(year_with_most_hours_played)}
        else:
            return {"Error": "No se encontraron juegos para el género especificado."}
    except Exception as e:
        # Manejo de errores
        return {"Error": str(e)}




    
        

@app.get("/user_for_genre/{genero}")
def UserForGenre(genero):
    ''' def UserForGenre( genero : str ): Devuelve el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año '''
    global consulta1  # Acceso a la variable global consulta1
    try:
        # Filtrar juegos por el género específico
        filtered_df = consulta1[consulta1['genres'] == genero]

        if not filtered_df.empty:
            # Encontrar al usuario que acumula más horas jugadas
            max_playtime_user = filtered_df.groupby('user_id')['playtime_forever'].sum().idxmax()

            # Calcular la acumulación de horas jugadas por año
            hours_played_by_year = filtered_df.groupby('release_year')['playtime_forever'].sum().reset_index()

            # Crear la lista de años y horas jugadas
            years = hours_played_by_year['release_year'].tolist()
            hours = hours_played_by_year['playtime_forever'].tolist()

            # Crear el diccionario de resultados
            result = {
                "Usuario con más horas jugadas para " + genero: max_playtime_user,
                "Horas jugadas": [{"Año": year, "Horas": hour} for year, hour in zip(years, hours)]
            }
            return result
        else:
            return {"Error": "No se encontraron juegos para el género especificado."}
    except Exception as e:
        return {"Error": str(e)}


           

    
@app.get("/users_recommend/{año}")    
def UsersRecommend(anio: int): 
    ''' def UsersRecommend( año : int ): Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales) '''
    global consulta1  # Acceso a la variable global consulta1
    try:
        # Filtra el DataFrame para obtener solo las filas del año dado
        df_filtered = consulta1[consulta1['release_year'] == anio]

        if not df_filtered.empty:
            # Filtra las filas con recomendaciones positivas o neutrales
            df_filtered = df_filtered[df_filtered['recommend'] == 1.0]

            if not df_filtered.empty:
                # Ordena las filas por la cantidad de recomendaciones en orden descendente
                df_filtered = df_filtered.sort_values(by='recommend', ascending=False)

                # Selecciona las 3 primeras filas (los juegos más recomendados)
                top_3_recommendations = df_filtered.head(3)

                # Crea una lista con los resultados
                result = [{"Puesto " + str(i + 1): row['title']} for i, (_, row) in enumerate(top_3_recommendations.iterrows())]

                return result

        return {"Error": "No se encontraron juegos recomendados para el año especificado."}
    except Exception as e:
        return {"Error": str(e)}

            








@app.get("/users_not_recommend/{año}")        
def UsersNotRecommend(anio: int):
    '''def UsersNotRecommend( año : int ): Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)'''
    global consulta1  # Acceso a la variable global consulta1
    try:
        # Filtra el DataFrame para obtener solo las filas del año dado
        df_filtered = consulta1[consulta1['release_year'] == anio]

        if not df_filtered.empty:
            # Filtra las filas con recomendaciones negativas
            df_filtered = df_filtered[df_filtered['recommend'] == 0.0]

            if not df_filtered.empty:
                # Ordena las filas por la cantidad de recomendaciones en orden descendente
                df_filtered = df_filtered.sort_values(by='recommend', ascending=True)

                # Selecciona las 3 primeras filas (los juegos menos recomendados)
                top_3_not_recommendations = df_filtered.head(3)

                # Crea una lista con los resultados
                result = [{"Puesto " + str(i + 1): row['title']} for i, (_, row) in enumerate(top_3_not_recommendations.iterrows())]

                return result

        return {"Error": "No se encontraron juegos menos recomendados para el año especificado."}
    except Exception as e:
        return {"Error": str(e)}







    




@app.get("/sentiment_analysis/{año}")
def sentiment_analysis(anio: int):
    '''
    def sentiment_analysis( año : int ): Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.
    '''
    try:
        # Filtra las filas del DataFrame para el año especificado
        filtered_data = consulta1[consulta1['release_year'] == anio]
        
        # Mapea los valores numéricos a las categorías deseadas
        sentiment_map = {0.0: 'Negative', 1.0: 'Neutral', 2.0: 'Positive'}
        filtered_data['sentiment_analysis'] = filtered_data['sentiment_analysis'].map(sentiment_map)
        
        # Cuenta la cantidad de registros en cada categoría de análisis de sentimiento
        sentiment_counts = filtered_data['sentiment_analysis'].value_counts()
        
        # Convierte el resultado en un diccionario
        sentiment_dict = sentiment_counts.to_dict()
        
        return sentiment_dict
    except Exception as e:
        # Manejo de errores
        return {"Error": str(e)}
    
año_deseado = 2012  # Reemplaza con el año que desees
resultados = sentiment_analysis(año_deseado)
print(resultados)











# Creamos una instancia de la clase CountVectorizer
vector = CountVectorizer(tokenizer= lambda x: x.split(', '))
# Dividimos cada cadena de descripción en palabras individuales y se crea una matriz de conteo 'matriz_descripcion' que representa cuántas veces aparece cada género en cada videojuego.
matriz_descripcion = vector.fit_transform(steam_games['description'])

@app.get("/juegos_recomendados/{id_producto}")
def recomendacion_juego(id_producto: int):
    '''
    def recomendacion_juego( id de producto ): Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado
    
    '''
    # Si el id ingresado no se encuentra en la columna de id de la tabla 'steam_games' se le pide al usuario que intente con otro id
    if id_producto not in steam_games['item_id'].values:
        return 'El ID no existe, intente con otro'
    else:
        # buscamos el índice del id ingresado
        index = steam_games.index[steam_games['item_id']==id_producto][0]

        # De la matriz de conteo, tomamos el array de descripciones con índice igual a 'index'
        description_index = matriz_descripcion[index]

        # Calculamos la similitud coseno entre la descripción de entrada y la descripción de las demás filas: cosine_similarity(description_index, matriz_descripcion)
        # Obtenemos los índices de las mayores similitudes mediante el método argsort() y las similitudes ordenadas de manera descendente
        # Tomamos los índices del 1 al 6 [0, 1:6] ya que el índice 0 es el mismo índice de entrada
        indices_maximos = np.argsort(-cosine_similarity(description_index, matriz_descripcion))[0, 1:6]

        # Construimos la lista
        recomendaciones = []
        for i in indices_maximos:
            recomendaciones.append(steam_games['title'][i])
        
        return recomendaciones





@app.get("/recomendacion_usuario/{usuario_id}")
def recomendacion_usuario(usuario_id):
    '''
    def recomendacion_usuario( id de usuario ): Ingresando el id de un usuario, recibimos una lista con 5 juegos recomendados para dicho usuario
    '''
    global consulta1  # Acceso a la variable global consulta1

    # Filtrar las reseñas del usuario actual
    num_recomendaciones=5
    reseñas_usuario = consulta1[consulta1['user_id'] == usuario_id]

    # Encontrar usuarios similares
    usuarios_similares = consulta1[consulta1['user_id'] != usuario_id]  # Excluir al usuario actual
    usuarios_similares = usuarios_similares.groupby('user_id')['recommend'].mean().reset_index()

    # Ordenar usuarios similares por su similitud (recomendación promedio)
    usuarios_similares = usuarios_similares.sort_values(by='recommend', ascending=False)

    # Inicializar una lista para almacenar las recomendaciones
    recomendaciones = []

    # Iterar sobre los usuarios similares y encontrar juegos recomendados por ellos
    for i, row in usuarios_similares.iterrows():
        usuario_similar_id = row['user_id']
        juegos_recomendados = consulta1[(consulta1['user_id'] == usuario_similar_id) & (consulta1['recommend'] == 1)]['title'].tolist()

        # Evitar juegos que el usuario ya haya revisado
        juegos_recomendados = [juego for juego in juegos_recomendados if juego not in reseñas_usuario['title'].tolist()]

        recomendaciones.extend(juegos_recomendados)

        # Detener la búsqueda cuando se alcance el número deseado de recomendaciones
        if len(recomendaciones) >= num_recomendaciones:
            break

    # Tomar las primeras 'num_recomendaciones' recomendaciones
    recomendaciones = recomendaciones[:num_recomendaciones]

    return recomendaciones