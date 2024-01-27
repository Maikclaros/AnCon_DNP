# **Análisis Contratos Electronicos (SECOP 2) - Departamento de Planeación Nacional "DNP"** 
## _DESCRIPCIÓN_
En el proyecto realizado, se pretende hacer un análisis de los contratos electrónicos en el SECOP II durante los años 2020 al 2023.


## _INSTALACIONES BÁSICAS_
1. Clona el repositorio: 'https://github.com/Maikclaros/AnCon_Mintic.git' y se selecciona 
    ```Python
   > ('../AnCon_DNP/codigo/preprocesamiento/Procesamiento.ipynb')
2. Instala la dependencia 'nbformat': 
    ```Python
    pip install --upgrade nbformat
3. Instala la dependencia 'plotly': 
    ```Python
    pip install plotly
## _EJECUCIÓN_
* Ejecute el script principal 'pre_procesamiento.ipynb'
* Importe las siguiente librerías:

    ```Python

   > import pandas as pd
   > import seaborn as sns
   > import matplotlib.pyplot as plt
   > import plotly.express as px
   > import nbformat

* Se definió el siguiente módulo de datos para el trabajo: 

    ```Python
    > DF_contratos = pd.read_csv('../AnCon_DNP/datos/Raw/contratos_dnp_2020.csv')

## _GRÁFICOS_
En el proceso pudimos encontrar la siguiente información con los gráficos adjuntos:
    
    1. Número de contratos por año
    2. Número de contratos por periodo
    3. Número de contratos por Estado y año
    4. Número de contratos por modalidad y año
    5. Número de contratos por tipo y año

## _MAYOR INFORMACIÓN_
Para mayor información sobre los contratos y proceso de adjudicación de los mismos:

* [Preguntas Frecuentes](https://www.colombiacompra.gov.co/ciudadanos/preguntas-frecuentes/secop-ii)
* [Plan Anual de Adquisiciones](https://www.colombiacompra.gov.co/ciudadanos/preguntas-frecuentes/secop-ii)

## _CRÉDITOS_

### Desarrolladores: 

- Michael Claros (@Maikclaros)
- Karen Henríquez (@karenhenriquez99)
- José Sebastián Cubillos (@SejeroCuco)
- Daniela Morales (@danimo92)

## _ESTADO DEL PROYECTO_
En desarrollo. Se aceptan contribuciones y sugerencias