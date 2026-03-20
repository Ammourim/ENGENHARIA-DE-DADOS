#%%
import pandas
from limpeza import df
#%%
df_pacientes = df[['paciente_nome']].drop_duplicates().reset_index(drop=True)
df_pacientes.insert(0, 'id_paciente', df_pacientes.index)
df_pacientes
#%%
df_setores = df[['setor']].drop_duplicates().reset_index(drop=True)
df_setores.insert(0,'id_setor', df_setores.index)
df_setores
# %%
df = df.merge(df_pacientes, on='paciente_nome', how='left')
df = df.merge(df_setores, on='setor', how='left')
df
# %%
df_atendimentos = df[['id_atendimento',
                      'id_paciente',
                      'id_setor',
                      'tempo_espera_min',
                      'data_atendimento',
                      'eh_outlier']] 
df_atendimentos
# %%
# 1. nulos
print(df_atendimentos.isnull().sum())

# 2. duplicados
print(df_pacientes['id_paciente'].duplicated().sum())
print(df_setores['id_setor'].duplicated().sum())

# 3. amostra
print(df_pacientes.head())
print(df_setores.head())
print(df_atendimentos.head())

# 4. volume
print(len(df_pacientes), len(df_setores), len(df_atendimentos))