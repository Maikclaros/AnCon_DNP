from flask import Flask, jsonify, render_template
import base64
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

# Cargar los datos
def load_data(file_path):
    return pd.read_csv(file_path)

# Preprocesamiento de datos
def preprocess_data(df):
    df['fecha_de_firma'] = pd.to_datetime(df['fecha_de_firma'], errors='coerce')
    df['fecha_de_firma_ano'] = df['fecha_de_firma'].dt.year.astype(str)
    df['fecha_de_firma_periodo'] = df['fecha_de_firma'].dt.to_period('M').astype(str)
    df = df[df['valor_del_contrato'] != 2870993010534] # Filtrar valores específicos
    return df

# Definir el pipeline
def define_pipeline(clustering_algorithm):
    pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='mean')),  # Imputar valores faltantes
        ('scaler', StandardScaler()),  # Preprocesamiento: Normalizar los datos
        ('clustering', clustering_algorithm),  # Algoritmo de clustering
    ])
    return pipeline

# Visualización de los clusters
def visualize_clusters(data, cluster_labels):
    plt.figure(figsize=(10, 6))
    for cluster_id in range(len(np.unique(cluster_labels))):
        cluster_data = data[cluster_labels == cluster_id]
        plt.scatter(cluster_data['valor_del_contrato'], cluster_data['tipo_de_contrato'], label=f'Cluster {cluster_id}')
    plt.xlabel('Valor del Contrato')
    plt.ylabel('Tipo de Contrato')
    plt.title('Clustering de contratos')
    plt.legend()
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return img

## Mostrar estadísticas descriptivas para cada cluster
def cluster_statistics(data, selected_columns, cluster_labels):
   stats = {}
   for cluster_id in range(len(np.unique(cluster_labels))):
       cluster_data = data[cluster_labels == cluster_id]
       stats[f'Cluster {cluster_id}'] = cluster_data[selected_columns].describe().to_dict()
   return stats
# Modifica la función cluster_statistics para reformatear los datos
# def cluster_statistics(data, selected_columns, cluster_labels):
#     stats = {}
#     for cluster_id in range(len(np.unique(cluster_labels))):
#         cluster_data = data[cluster_labels == cluster_id]
#         cluster_stats = cluster_data[selected_columns].describe().to_dict()
#         # Reformatear los datos para hacerlos más legibles
#         formatted_stats = {k: round(v, 2) for k, v in cluster_stats.items() if k in ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']}
#         stats[f'Cluster {cluster_id}'] = formatted_stats
#     return stats


# Main function
def cluster():
    # Cargar datos
    file_path = 'datos/Raw/contratos_dnp_2020_v1.csv'
    df_contratos_v1 = load_data(file_path)

    # Preprocesar datos
    df_contratos_v1 = preprocess_data(df_contratos_v1)

    # Definir el algoritmo de clustering
    clustering_algorithm = AgglomerativeClustering(n_clusters=5, linkage='average')

    # Definir el pipeline
    pipeline = define_pipeline(clustering_algorithm)

    # Entrenar el pipeline y obtener las etiquetas de cluster
    cluster_labels = pipeline.fit_predict(df_contratos_v1[['valor_del_contrato']])

    # Agregar las etiquetas de los clusters al DataFrame
    df_contratos_v1['cluster'] = cluster_labels

    # Visualizar los clusters y convertir la imagen a bytes
    img = visualize_clusters(df_contratos_v1, cluster_labels)

    # Mostrar estadísticas descriptivas para cada cluster
    stats = cluster_statistics(df_contratos_v1, ['valor_del_contrato'], cluster_labels)

    return render_template('index.html', image=base64.b64encode(img.getvalue()).decode('ascii'), statistics=stats)

# Endpoint para mostrar los resultados del clúster
@app.route('/')
def show_cluster_results():
    return cluster()

if __name__ == "__main__":
    app.run(debug=True)
