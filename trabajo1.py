import pandas as pd

data = {
    'name': ['John', 'Alice', 'Bob', 'Eve', 'Michael', 'Sarah', 'David'],
    'age': [25, 30, 22, 35, 28, 29, 24],
    'is_dead': [0, 1, 0, 1, 0, 0, 1]
}

df = pd.DataFrame(data)

df_perecidos = df[df['is_dead'] == 1]
df_no_perecidos = df[df['is_dead'] == 0]

promedio_edades_perecidos = df_perecidos['age'].mean()
promedio_edades_no_perecidos = df_no_perecidos['age'].mean()

print("Promedio de edades de personas que perecieron:", promedio_edades_perecidos)
print("Promedio de edades de personas que no perecieron:", promedio_edades_no_perecidos)
