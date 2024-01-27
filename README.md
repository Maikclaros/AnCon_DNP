# **Análisis Contratos Electronicos (SECOP 2) - Departamento de Planeación Nacional "DNP"** 
## _INTRODUCCIÓN_
Uno de los propósitos de aplicar analítica en las bases de datos de contratos electrónicos en Colombia:

1. Observar tendencias y acciones que emprende una entidad pública para su funcionamiento.
2. Identificar incrementos o decrementos en contratos para cumplimiento de su quehacer institucional.
3. Determinar si la gestión administrativa es óptima de acuerdo con su andamiaje y contratación pública.
4. Identificar concentración de recursos por procesos de contratación y posibles cifras que afectan la tendencia de lo contratado por una entidad pública.

Lo anteriores numerales nos permite situar en que podemos enfocar esta revisión preliminar de los datos de contratación electrónica y siendo específicos en el Departamento Nacional de Planeación.

Es importante distinguir que la herramienta por excelencia en donde se puede extraer toda la información para lograr este análisis es el SECOP II: "Es la nueva versión del SECOP (Sistema Electrónico de Contratación Pública) para pasar de la simple publicidad a una plataforma transaccional que permite a Compradores y Proveedores realizar el Proceso de Contratación en línea.  

Desde su cuenta, las Entidades Estatales (Compradores) pueden crear y adjudicar Procesos de Contratación, registrar y hacer seguimiento a la ejecución contractual. Los Proveedores también pueden tener su propia cuenta, encontrar oportunidades de negocio, hacer seguimiento a los Procesos y enviar observaciones y Ofertas..."
De igual manera es importante resaltar que "asegura la trazabilidad y la transparencia de la Gestión contractual. Los proveedores son activos ya que deben registrarse y tener interacción con las Entidades Estatales a través del sistema y pueden solicitar informes acerca del proceso que les interesa y para esto cuentan con el clasificador de bienes y servicios"

Fuente: https://www.colombiacompra.gov.co/ciudadanos/preguntas-frecuentes/secop-ii

Dado el contexto, en que las entidades de orden público y que integran el Presupuesto General de la Nación, es decir que administran recursos públicos, es importante identificar que el registro de la información cumple con los requerimientos para todos los procesos contractuales y esto se identifican desde una correcta planificación en la elaboración del Plan Anual de Adquisiciones (PAA) - " es una oportunidad para empezar a implementar y hacer uso del SECOP II en su Entidad Estatal. Para el efecto, debe registrar la Entidad Estatal y los usuarios encargados de elaborar, aprobar y publicar el PAA.

La funcionalidad del PAA en el SECOP II permite hacer un seguimiento cercano a su planeación y ejecución, y tener visible las diferentes versiones del PAA para hacer seguimiento a los cambios realizados durante el año".

Fuente: https://www.colombiacompra.gov.co/plan-anual-de-adquisiciones/que-es-el-plan-anual-de-adquisiciones

Una vez, la acción de planificación correcta las entidades deben garantizar una correcta ejecución del PAA y un correcto diligenciamiento de los procesos contractuales.

Es por eso por lo que, en este análisis exploratorio, se debe accionar en revisión de datos incompletos, aproximación con otras variables para identificar número de contratos por año, concentración de contratos por modalidad y tipo y de igual manera utilizar medidas de tendencia central para distinguir procesos contractuales que estén por encima de la media y enfocarse en el ejercicio de transparencia y gestión administrativa del DNP.

Adicional al análisis que se puede enfocar por número de contratos, es indispensable identificar como los recursos públicos son manejados acorde a las situaciones de respuesta institucional y misional como lo es el Departamento Nacional de Planeación, es por esto que evidenciaremos la concentración de recursos por modalidad de contratación y su respectivo peso porcentual para identificar situaciones atípicas o evidenciar que corresponden los contratos con mayores recursos asignados. De igual manera, demostrar que las asignaciones presupuestales que tiene una entidad pública como el caso de recursos de funcionamiento e inversión puede ser limitados y no es necesario aplicar ejercicios de proyecciones, sino de priorización de gasto y cumplimiento institucional.

Dado lo anterior, se hará una serie de pasos que permita dar claridad de las acciones exploratorias y analíticas que se efectúan a los datos de los contratos de las vigencias 2020 a 2023.

## _OBJETIVO_
Aplicar un análisis exploratorio de la información de contratos existentes en el sistema electrónico de contratación para las vigencias 2020 al 2023 del Departamento Nacional de Planeación, el cual permitirá identificar concentración de número de contratos y recursos adjudicados para efectuar controles y evidenciar un control previo, durante y posterior al uso de los dineros públicos.

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