#%%
import pandas as pd
# importando csv 
df = pd.read_csv('data/raw/atendimentos.csv', 
                 sep = ',', 
                 encoding='utf-8',
                 parse_dates=['data_atendimento'])
df
#%%
# excluindo linhas com valores nulos, da coluna paciente_nome (obrigatório)
df.dropna(subset=['paciente_nome'], inplace=True)
df
# %%
# analisando o tipo de coluna (verificando se não é string)
df['tempo_espera_min'].describe
# %%
# extraindo a mediana da coluna
mediana = df['tempo_espera_min'].median(axis=0)
mediana
# %%
# tratando valores nulos, substituindo pela mediana
df['tempo_espera_min'] = df['tempo_espera_min'].fillna(mediana)
df
# %%
# tratando valores negativos, substituindo pela mediana
df.loc[df['tempo_espera_min'] < 0, 'tempo_espera_min'] = mediana
df
# %%
# padronizando a coluna setor para minusculo
df['setor'] = df['setor'].str.lower()
df
# %%
# eliminando duplicatas
comparacao_colunas = df.columns.drop('id_atendimento')
df = df.drop_duplicates(subset=comparacao_colunas, ignore_index=True)
df
# %%
# tratando outliers (substituindo outliers pela mediana)
# usando o .describe temos que 75% = 60
df['tempo_espera_min'].describe()
df.loc[df['tempo_espera_min'] > 60, 'tempo_espera_min'] = mediana
df
# %%
# conferindo tipos de coluna
df.info()
# %%
df