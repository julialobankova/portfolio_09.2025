from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash import BashOperator
from functions import pars_save_to_csv, copy_command
from params import  columns, name_file, your_table, delimiter, file_format, mean_header, USER, DBNAME, HOST, \
    PORT, PASSWORD
    
       

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 9, 16),
    'retries': False,
}

dag = DAG(
    'toys_parsing_dag',
    default_args=default_args,
    description='DAG для парсинга цен товаров в магазине игрушек',
    schedule_interval=None,
    catchup=False,
)

pars_save_task = PythonOperator(
    task_id='pars_save_task',
    python_callable=pars_save_to_csv,
    op_kwargs={
      'columns':columns,
      'name_file':name_file
      },
    provide_context=True,
    dag=dag,
)

copy_command = copy_command( USER, DBNAME, HOST,PORT,your_table,name_file,delimiter,file_format,mean_header)


load_data = BashOperator(
    task_id='load_data',
    bash_command=copy_command,
    env={
        'PGPASSWORD': PASSWORD,
    },
    dag=dag,
)

pars_save_task >> load_data
