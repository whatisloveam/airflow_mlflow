# Airflow и Mlflow
В качестве примера взят датасет [соревнования на Kaggle](https://www.kaggle.com/competitions/tabular-playground-series-jan-2022 ), метрика - MAPE
# Воспроизводимость

1. Создание виртуального окружение

   ```
   mkdir MLOps3
   cd MLOps3
   python -m venv MLOps3_venv
   source MLOps3_venv/bin/activate
   ```

2. Установка, настройка и запуск airflow

   ```
   AIRFLOW_VERSION=2.7.3
   PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
   CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
   pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
   
   export AIRFLOW_HOME=/home/vlad/MLOps3/airflow
   airflow db init
   airflow users  create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin
   airflow webserver -p 8081
   ```
   Планировщик запускаем через другой терминал
   ```
   export AIRFLOW_HOME=/home/vlad/MLOps3/airflow
   airflow scheduler
   ```
4. Установка и запуск mlflow

   ```
   pip install mlflow
   export MLFLOW_REGISTRY_URI=mlflow
   mlflow ui
   ```

6. Доступ к Airflow web interface в браузере по адресу: http://localhost:8081.
7. Доступ к mlflow  web interface в браузере по адресу: http://localhost:5000.
   
8. Запускаем нужный пайплайн и кайфуем.
9. Результаты
   ![image](images/airflow.png)
   ![image](images/mlflow.png)
   
