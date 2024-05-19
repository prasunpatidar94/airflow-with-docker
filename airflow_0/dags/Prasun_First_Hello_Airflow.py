from airflow import DAG
from datetime import datetime, timedelta 
from airflow.operators.bash_operator import BashOperator

default_args={
    "owner":"Prasun_Patidar",
    "retries":5,
    "retry_delay":timedelta(minutes=2) 
}
with DAG(
    dag_id="Prasun_First_Hello_Airflow_001",
    default_args=default_args,
    description="This is my first dag to say hello world",
    start_date=datetime(2024, 5, 3, 2),
    schedule_interval='@daily'

) as dag:

    task1 = BashOperator(
        task_id="first_task",
        bash_command="echo hello prasun 1  !!"
    )
    task2= BashOperator(
        task_id="second_task",
        bash_command="echo this is the secnd  2 task on flow ...! !!"
    )
    task3= BashOperator(
        task_id="three_task",
        bash_command="echo this is the three 3  task on flow ...! !!"
    )
# method 1
    # task1.set_downstream(task2)  
    # task1.set_downstream(task3)
# method 2
    # task1 >> task2 
    # task1 >> task3 
# method 3
    task1 >> [task2 , task3]