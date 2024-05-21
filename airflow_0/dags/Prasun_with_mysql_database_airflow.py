from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.mysql.hooks.mysql import MySqlHook
from datetime import datetime, timedelta
from airflow.decorators import dag, task

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 5, 20),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

@dag(
        'Prasun_with_mysql_database_airflow',
    default_args=default_args,
    description='An example DAG using MySqlHook',
    schedule_interval='@once',
    catchup=False,
)
def Prasun_with_mysql_database_airflow_fn():


# dag = DAG(
#     'Prasun_with_mysql_database_airflow',
#     default_args=default_args,
#     description='An example DAG using MySqlHook',
#     schedule_interval=timedelta(days=1),
#     catchup=False,
# )

    @task(multiple_outputs=False)
    def execute_query():
    # Create a MySqlHook with a connection ID
        mysql_hook = MySqlHook(mysql_conn_id='mysql_localhost')
        conn = mysql_hook.get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * from my_airflow.jobExec je  WHERE  je.jobName = 'job10' and je.busDt ='2023-01-10';")
        result = list(cursor.fetchall())[0][0]
        
        return result
        # for row in result:
        #     print(row)

    @task()
    def execute_query_task(result):
         print(result)  
        #  for row in result:
        #     print(row)

    # execute_query_task = PythonOperator(
    # task_id='execute_query_task',
    # python_callable=execute_query,
    # dag=dag,
# )
    result =execute_query()
    execute_query_task(result)

Prasun_with_mysql_database_airflow_fn()
