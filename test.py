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
nuevas_observaciones = {
    'motor': ['4 cilindros', 'V6', 'V8'],
    'combustible': ['diésel', 'gasolina', 'gasolina'],
    'modelo': ['Pickup', 'Sedán', 'SUV']
}

df_nuevas_observaciones = pd.DataFrame(nuevas_observaciones)

# Agregar las nuevas observaciones al DataFrame existente
df = df.append(df_nuevas_observaciones, ignore_index=True)

print(df)

##########
##Marco###
##########
nuevos_datos = {
    'motor': ['V10', 'V12', 'V5'],
    'combustible': ['gasolina', 'gasolina', 'disel'],
    'modelo': ['SUV', 'pickup', 'SUV']
    }
act=pd.concat([df,pd.DataFrame(nuevos_datos)],ignore_index=True)
print(act)