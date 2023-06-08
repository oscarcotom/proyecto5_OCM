#Prueba de proyecto 5

import pandas as pd

data = {
    'motor': ['V8', 'V6', '4 cilindros', 'V8', '4 cilindros', 'V6', 'V8'],
    'combustible': ['gasolina', 'gasolina', 'diésel', 'gasolina', 'híbrido', 'gasolina', 'diésel'],
    'modelo': ['Sedán', 'SUV', 'Hatchback', 'Coupé', 'Sedán', 'SUV', 'Pickup']
}

df = pd.DataFrame(data)
print(df)

# Observaciones adicionales JMH
jenny = {
    'motor': ['4 cilindros', 'V6', 'V8'],
    'combustible': ['diésel', 'gasolina', 'gasolina'],
    'modelo': ['Pickup', 'Sedán', 'SUV']
}

df_jenny = pd.DataFrame(jenny)

# Agregar las nuevas observaciones al DataFrame existente
df = df.append(df_jenny, ignore_index=True)

print(df)