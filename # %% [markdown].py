# %% [markdown]
# # Análisis Estadístico y Visualización de Datos
# 
# Este notebook presenta un análisis descriptivo de las respuestas obtenidas en la encuesta, junto con visualizaciones gráficas para comprender mejor los datos.
# 
# ---
# 
# ## 1. Estadística Descriptiva
# 
# ### 1.1 Distribución de Edades
# En esta sección, se analizan las edades de los participantes. Se calculan estadísticas descriptivas como media, mediana y desviación estándar, y se visualiza un histograma.
# 

# %%
# Importar las bibliotecas necesarias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
file_path = "Respuestas.xlsx"  # Ruta del archivo
df = pd.read_excel(file_path, sheet_name="Respuestas de formulario 1")

# Configurar el estilo de los gráficos
sns.set_style("whitegrid")

# Estadísticas descriptivas de la edad
print("Estadísticas de Edad:")
print(df['Edad'].describe().round(2))

# Histograma de edades
plt.figure(figsize=(10, 6))
plt.hist(df['Edad'], bins=10, edgecolor='black', alpha=0.7, color='skyblue')
plt.title("Distribución de Edades", fontsize=16, weight='bold')
plt.xlabel("Edad", fontsize=12)
plt.ylabel("Frecuencia", fontsize=12)
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()
plt.show()


# %% [markdown]
# ### Resultados:
# - **Media:** La media de las edades es `(valor que obtengas)`.
# - **Distribución:** El histograma muestra cómo están distribuidas las edades entre los participantes.
# 
# ---
# 
# ### 1.2 Distribución por Género
# Se analiza la proporción de géneros en la encuesta, representada en un gráfico circular.
# 

# %%
# Conteo por género
gender_counts = df['Genero'].value_counts()
print("Distribución por Género:")
print(gender_counts)

# Gráfico circular de género
plt.figure(figsize=(8, 6))
gender_counts.plot.pie(autopct='%1.1f%%', startangle=90, colors=['skyblue', 'pink', 'lightgreen'])
plt.title("Distribución de Género", fontsize=16, weight='bold')
plt.ylabel("")  # Ocultar etiqueta del eje Y
plt.tight_layout()
plt.show()


# %% [markdown]
# ### Observaciones:
# - Los géneros representados en la encuesta están distribuidos de la siguiente manera:
#   - Masculino: `(valor)`
#   - Femenino: `(valor)`
#   - Otros: `(valor)`
#   
# ---
# 
# ## 2. Niveles de Conocimiento
# 
# En esta sección, se analiza el nivel de conocimiento en diversas tecnologías como Blockchain, Criptomonedas, Inteligencia Artificial (IA), y Machine Learning (ML). Se genera un gráfico consolidado que muestra todas las tecnologías en un formato apilado.
# 

# %%
# Columnas de tecnologías
knowledge_columns = [
    '¿Cuál es tu nivel de conocimiento sobre Blockchain? ',
    '¿Cuál es tu nivel de conocimiento sobre Criptomonedas? ',
    '¿Cuál es tu nivel de conocimiento sobre Inteligencia Artificial (IA)? ',
    '¿Cuál es tu nivel de conocimiento sobre Machine Learning (ML)? '
]

# Datos de conocimiento
knowledge_data = df[knowledge_columns].apply(pd.Series.value_counts).fillna(0)

# Renombrar las columnas para mayor claridad
knowledge_data.columns = ['Blockchain', 'Criptomonedas', 'IA', 'ML']

# Gráfico consolidado
plt.figure(figsize=(12, 8))
knowledge_data.T.plot(kind='bar', stacked=True, colormap='viridis', edgecolor='black')

# Títulos y etiquetas
plt.title("Distribución Consolidada de Niveles de Conocimiento por Tecnología", fontsize=16, weight='bold')
plt.xlabel("Tecnología", fontsize=12)
plt.ylabel("Cantidad de Respuestas", fontsize=12)
plt.xticks(rotation=0, fontsize=10)

# Leyenda
plt.legend(title="Niveles de Conocimiento", bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)

# Ajustar márgenes
plt.tight_layout()
plt.show()


# %% [markdown]
# ### Observaciones:
# - Este gráfico muestra los niveles de conocimiento en cada tecnología.
# - **Tendencias Notables:**
#   - Blockchain tiene `(proporción)` de participantes con conocimiento avanzado.
#   - IA tiene una mayor proporción de conocimiento intermedio.
# 
# ---
# 
# ## 3. Relación entre Conocimiento y Percepción
# 
# ### 3.1 Percepción de Blockchain en Ciberseguridad
# Se analiza cómo los niveles de conocimiento en Blockchain afectan la percepción de su utilidad en ciberseguridad.
# 

# %%
# Cruce entre conocimiento de Blockchain y percepción de utilidad
blockchain_vs_security = pd.crosstab(
    df['¿Cuál es tu nivel de conocimiento sobre Blockchain? '],
    df['¿Consideras que el Blockchain es una tecnología útil para la ciberseguridad? ']
)

# Gráfico de áreas apiladas
blockchain_vs_security.plot(kind='area', figsize=(10, 6), colormap='plasma', alpha=0.8)
plt.title("Relación entre Conocimiento de Blockchain y Ciberseguridad", fontsize=16, weight='bold')
plt.xlabel("Niveles de Conocimiento de Blockchain", fontsize=12)
plt.ylabel("Cantidad de Respuestas", fontsize=12)
plt.tight_layout()
plt.show()


# %% [markdown]
# ### Observaciones:
# - La percepción de Blockchain como útil para la ciberseguridad está relacionada con niveles más altos de conocimiento.
# 
# ---
# 
# ## 4. Probabilidad Condicional
# 
# Se evalúa la probabilidad condicional de ciertos eventos, como tener conocimiento avanzado en IA dado que se tiene conocimiento avanzado en ML.
# 

# %%
# Filtrar participantes con conocimiento avanzado en ML
advanced_ml = df[df['¿Cuál es tu nivel de conocimiento sobre Machine Learning (ML)? '] == 'Avanzado']

# Evitar división por cero
if len(advanced_ml) > 0:
    prob_ia_given_ml = len(advanced_ml[advanced_ml['¿Cuál es tu nivel de conocimiento sobre Inteligencia Artificial (IA)? '] == 'Avanzado']) / len(advanced_ml)
    print(f"Probabilidad de tener conocimiento avanzado en IA dado ML avanzado: {prob_ia_given_ml:.2f}")
else:
    print("No hay participantes con conocimiento avanzado en Machine Learning (ML).")


# %% [markdown]
# ### Observaciones:
# - La probabilidad de que un participante tenga conocimiento avanzado en IA, dado que tiene conocimiento avanzado en ML, es de `0` ya que ningun encueastado al menos de la Universidad tecnologica de Panama en el centro regional mostro esto.
# 
# ---
# 
# ## Conclusión
# 
# Este análisis estadístico y visual presenta una visión clara de los datos de la encuesta, destacando tendencias clave y relaciones entre conocimiento y percepciones.
# 


