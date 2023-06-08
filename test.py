#Prueba de proyecto 5

###################
# Import modules  # 
####################

import pandas as pd
import numpy as numpy

#########################
#  Inicio: Oscar Coto
#########################

data = {
    'motor': ['V8', 'V6', '4 cilindros', 'V8', '4 cilindros', 'V6', 'V8'],
    'combustible': ['gasolina', 'gasolina', 'diésel', 'gasolina', 'híbrido', 'gasolina', 'diésel'],
    'modelo': ['Sedán', 'SUV', 'Hatchback', 'Coupé', 'Sedán', 'SUV', 'Pickup']
}

df = pd.DataFrame(data)
print(df)

####################################
# Observaciones adicionales JMH   #
#####################################
nuevas_observaciones = {
    'motor': ['4 cilindros', 'V6', 'V8'],
    'combustible': ['diésel', 'gasolina', 'gasolina'],
    'modelo': ['Pickup', 'Sedán', 'SUV']
}

df_nuevas_observaciones = pd.DataFrame(nuevas_observaciones)

# Agregar las nuevas observaciones al DataFrame existente
df = df.append(df_nuevas_observaciones, ignore_index=True)

# print(df)


####################################
# Observaciones adicionales OCM   #
#####################################

df_OCM = {
    'motor': ['8 cab', '6 cab', '4 cab'],
    'combustible': ['gas', 'gas', 'gas'],
    'modelo': ['Fortuner', 'Defender', 'Discovery']
}

df_OCM = pd.DataFrame(df_OCM)

# Agregar las nuevas observaciones al DataFrame iniciado por Óscar Coto Morales

df = df.append(df_OCM, ignore_index=True)
# print(df)