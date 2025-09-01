# MACHINE-LEARNING
Aprendizaje Automático Supervisado-b) Actividad: Clasificación de Acciones de Usuarios en una Plataforma de Videojuegos

-Resumen del Clasificador de Acciones de Videojuegos

clasificador_simple.py es un ejemplo de aprendizaje automático supervisado que clasifica acciones de usuarios en un videojuego. El objetivo es entender cómo se pueden usar reglas para categorizar el comportamiento de los jugadores. El programa usa un conjunto de datos de ejemplo y aplica una serie de reglas lógicas para determinar el tipo de acción (como Combate, Exploración o Interacción social). Las reglas más importantes se basan en el resultado de la acción, como "Victoria", "Derrota" o "Mensaje enviado". Si el resultado no es suficiente, el programa usa reglas complementarias basadas en la duración de la acción. El código muestra que este enfoque funciona para el pequeño conjunto de datos, logrando una alta precisión. Sin embargo, tiene limitaciones importantes:

-NO GENERALIZA: Las reglas no pueden clasificar acciones o resultados que no se hayan definido previamente. -NO APRENDE: El sistema no mejora por sí mismo y solo sigue las reglas que se le han dado. -DIFICIL MANTENIMIENTO: A medida que la cantidad de datos y acciones aumentan, mantener las reglas a mano se vuelve muy complicado.

Para mejorar y crear un sistema más robusto, se sugiere usar modelos de aprendizaje automático más avanzados, como el Árbol de Decisión o k-Nearest Neighbors (k-NN). Estos modelos aprenden automáticamente de los datos y pueden identificar patrones más complejos para clasificar nuevas acciones de manera más efectiva.
