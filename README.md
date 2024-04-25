# Análisis Contratos Electrónicos (SECOP 2) - Departamento de Planeación Nacional "DNP"

## INTRODUCCIÓN

Uno de los propósitos de aplicar analítica en las bases de datos de contratos electrónicos en Colombia es observar tendencias y acciones que emprende una entidad pública para su funcionamiento, identificar incrementos o decrementos en contratos para cumplimiento de su quehacer institucional, determinar si la gestión administrativa es óptima de acuerdo con su andamiaje y contratación pública, y identificar concentración de recursos por procesos de contratación y posibles cifras que afectan la tendencia de lo contratado por una entidad pública.

Es importante distinguir que la herramienta por excelencia en donde se puede extraer toda la información para lograr este análisis es el SECOP II, el cual permite a compradores y proveedores realizar el proceso de contratación en línea, asegurando la trazabilidad y la transparencia de la gestión contractual.

Dado el contexto, en que las entidades de orden público y que integran el Presupuesto General de la Nación, es decir que administran recursos públicos, es importante identificar que el registro de la información cumple con los requerimientos para todos los procesos contractuales y esto se identifican desde una correcta planificación en la elaboración del Plan Anual de Adquisiciones (PAA).

## OBJETIVO

Aplicar un análisis exploratorio de la información de contratos existentes en el sistema electrónico de contratación para las vigencias 2020 al 2023 del Departamento Nacional de Planeación, el cual permitirá identificar concentración de número de contratos y recursos adjudicados para efectuar controles y evidenciar un control previo, durante y posterior al uso de los dineros públicos, esto brindará un enfoque analítico por clusters al aplicar desarrollos como aplicaciones y/o estándares de programación para analizar un volumen de datos como lo son los contratos públicos en el sistema de contratación estatal en Colombia.

## INSTALACIONES BÁSICAS

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tu_usuario/tu_proyecto.git
    ```

2. Instala las dependencias:
    
   ```bash
    pip install -r requirements.txt
    ```

## EJECUCIÓN

### Ejecución de la API

Para ejecutar la API, sigue estos pasos:

1. Dirígete a la carpeta `app`.
2. Ejecuta el archivo `main.py`.
3. Abre tu navegador web y navega a la dirección `http://127.0.0.1:5000`.
4. Ingresa los datos solicitados en la interfaz de la API.

### Ejecución del Pipeline

Para ejecutar el Pipeline, sigue estos pasos:

1. Dirígete a la carpeta `codigo/modelado`.
2. Abre el archivo `Pipeline.ipynb`.
    - Este cuaderno ejecuta un procesamiento de los datos, transformaciones, entrenamiento del modelo, y proporciona gráficos y estadísticas.
3. Ejecuta todo el cuaderno para realizar el proceso completo.

### Ejecución del Test

Para verificar el funcionamiento del Pipeline, sigue estos pasos:

1. Abre el archivo `test.ipynb`.
2. Proporciona los datos solicitados para ejecutar el test.

### Proyecto de Modelado y Preprocesamiento de Datos

El proyecto se estructura en las siguientes carpetas principales:

- `app`: Contiene el código para la aplicación desarrollada.
- `código`: Dividido en secciones de `Modelado` y `Preprocesamiento`.
  - **Modelado**: Contiene el código para construir el pipeline y realizar pruebas sobre el modelo. Incluye la generación de clusters para segmentar la información de los contratos.
  - **Preprocesamiento**: Incluye archivos para la descarga, preprocesamiento y procesamiento de los datos.
- `datos`: Contiene el modelo entrenado y todos los archivos generados durante el trabajo.
- `documentación`: Aquí se encuentra el informe final del proyecto, que incluye todas las observaciones, análisis y conclusiones obtenidas a lo largo del trabajo realizado.

---

## GRÁFICOS

En el proceso pudimos encontrar la siguiente información con los gráficos adjuntos:
    
1. Número de contratos por año.
2. Número de contratos por periodo.
3. Número de contratos por Estado y año.
4. Número de contratos por modalidad y año.
5. Número de contratos por tipo y año.

Estos gráficos se encuentran disponibles en la carpeta `documentación/graficas` del proyecto.

## MAYOR INFORMACIÓN

Para mayor información sobre los contratos y proceso de adjudicación de los mismos, puedes consultar las siguientes fuentes:

* [Preguntas Frecuentes](https://www.colombiacompra.gov.co/ciudadanos/preguntas-frecuentes/secop-ii)
* [Plan Anual de Adquisiciones](https://www.colombiacompra.gov.co/ciudadanos/preguntas-frecuentes/secop-ii)

## CRÉDITOS

### Desarrolladores

- Michael Claros (@Maikclaros)
- José Sebastián Cubillos (@SejeroCuco)
- Karen Henríquez (@karenhenriquez99)
- Daniela Morales (@danimo92)
