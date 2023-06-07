#Prueba de proyecto 5

import pandas as pd

data = {
    'motor': ['V8', 'V6', '4 cilindros', 'V8', '4 cilindros', 'V6', 'V8'],
    'combustible': ['gasolina', 'gasolina', 'diésel', 'gasolina', 'híbrido', 'gasolina', 'diésel'],
    'modelo': ['Sedán', 'SUV', 'Hatchback', 'Coupé', 'Sedán', 'SUV', 'Pickup']
}

df = pd.DataFrame(data)
print(df)