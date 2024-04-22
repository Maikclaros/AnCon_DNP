from flask import Flask, jsonify, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Cargar el modelo y realizar predicciones
def predict_clusters(data):
    # Cargar el modelo previamente entrenado
    model_path = 'app\modelo_cluster.pkl'
    pipeline = joblib.load(model_path)

    # Obtener las etiquetas de cluster
    cluster_labels = pipeline.predict(data)

    return cluster_labels

# Main function
def cluster(data):
    # Implementa el preprocesamiento según sea necesario
    processed_data = data

    # Realizar predicciones
    cluster_labels = predict_clusters(processed_data)

    # Crear un diccionario con el mensaje del cluster
    cluster_message = f"Los nuevos datos pertenecen al cluster {cluster_labels[0]}"

    return render_template('result.html', cluster_message=cluster_message)

# Endpoint para mostrar el formulario
@app.route('/')
def show_form():
    return render_template('form.html')

# Endpoint para procesar el formulario
@app.route('/process', methods=['POST'])
def process_form():
    # Obtener los datos del formulario
    data = {
        'ciudad': request.form['ciudad'],
        'tipo_de_contrato': request.form['tipo_contrato'],
        'estado_contrato': request.form['estado_contrato'],
        'modalidad_de_contratacion': request.form['modalidad_contratacion'],
        'fecha_de_firma_month': int(request.form['fecha_firma_month']),
        'duracion_contrato_dias': int(request.form['duracion_contrato_dias']),
        'valor_del_contrato': float(request.form['valor_contrato']),
        'valor_contrato_por_dia': float(request.form['valor_contrato_por_dia'])
    }

    # Crear un DataFrame con los datos ingresados por el usuario
    user_data = pd.DataFrame(data, index=[0])

    # Generar los resultados del clustering y mostrarlos
    return cluster(user_data)

if __name__ == "__main__":
    app.run(debug=True)
