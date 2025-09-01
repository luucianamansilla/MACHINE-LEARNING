import pandas as pd

#Crear el DataFrame con los datos de ejemplo
data = {
    'Usuario': ['user01', 'user02', 'user03', 'user04', 'user05'],
    'Accion': ['Combate', 'Exploracion', 'Interaccion social', 'Combate', 'Exploracion'],
    'Duracion': [120, 300, 180, 90, 240],
    'Resultado': ['Victoria', 'Descubrimiento', 'Mensaje enviado', 'Derrota', 'Sin hallazgos']
}
df = pd.DataFrame(data)

#Definir funcion que aplica las reglas de clasificacion
def reglas_de_clasificacion(fila):
    #Reglas basadas en el resultado (las mas especificas)
    if fila['Resultado'] in ['Victoria', 'Derrota']:
        return 'COMBATE'
    elif fila['Resultado'] == 'Mensaje enviado':
        return 'INTERACCION SOCIAL'
    elif fila['Resultado'] in ['Descubrimiento', 'Sin hallazgos']:
        return 'EXPLORACION'
    
    #Reglas basadas en la duracion (complementarias)
    elif fila['Duracion'] > 200:
        return 'EXPLORACION'
    elif fila['Duracion'] < 150:
        return 'COMBATE'
    
    #Si ninguna regla aplica
    else:
        return 'OTRA'

#Aplicar la funcion a cada fila del DataFrame para obtener la clasificacion final
df['Clasificacion_Final'] = df.apply(reglas_de_clasificacion, axis=1)

#Calcular la precision (accuracy)
accuracy = (df['Accion'].str.lower() == df['Clasificacion_Final'].str.lower()).mean()

#Mostrar resultados
print("DataFrame Original:")
print(df[['Usuario', 'Duracion', 'Resultado', 'Accion']])

print("\nDataFrame con Clasificacion Final:")
print(df[['Usuario', 'Clasificacion_Final']])

print(f"\nAccuracy (Precision) de las reglas: {accuracy:.2f}")