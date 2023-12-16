from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator
import datetime as dt


args = {
    "owner": "admin",
    "start_date": dt.datetime(2022, 12, 1),
    "retries": 1,
    "retry_delays": dt.timedelta(minutes=1),
    "depends_on_past": False
}

with DAG(
    dag_id='competition',
    default_args=args,
    schedule_interval=None,
    tags=['competition', 'score']
) as dag:
    p = 'python3 /home/vlad/MLOps3/scripts/'
    get_data = BashOperator(task_id='get_data',
                            bash_command=p+"get_data.py",
                            dag=dag)
    process_data = BashOperator(task_id='process_data',
                                bash_command=p+"process_data.py",
                                dag=dag)
    train_test_split_data = BashOperator(task_id='train_test_splits',
                                         bash_command=p+"train_test_split.py",
                                         dag=dag)
    train_model = BashOperator(task_id='train_model',
                               bash_command=p+"train_model.py",
                               dag=dag)
    test_model = BashOperator(task_id='test_model',
                              bash_command=p+"test_model.py",
                              dag=dag)

    get_data >> process_data >> train_test_split_data >> train_model >> \
        test_model
