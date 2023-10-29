import pandas as pd

data = {
    'name': ['John', 'Alice', 'Bob', 'Eve', 'Michael', 'Sarah', 'David'],
    'age': [25, 30, 22, 35, 28, 29, 24],
    'is_dead': [0, 1, 0, 1, 0, 0, 1],
    'gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male'],
    'smoker': ['No', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes']
}

df = pd.DataFrame(data)

tipos_de_datos = df.dtypes
print("Tipos de datos en cada columna:")
print(tipos_de_datos)

hombres_fumadores = df[(df['gender'] == 'Male') & (df['smoker'] == 'Yes')].shape[0]
mujeres_fumadoras = df[(df['gender'] == 'Female') & (df['smoker'] == 'Yes')].shape[0]

print("Cantidad de hombres fumadores:", hombres_fumadores)
print("Cantidad de mujeres fumadoras:", mujeres_fumadoras)
