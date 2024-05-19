from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator


default_args = {
    "owner": "Prasun Patidar",
    "retries": 5,
    "retry_delay": timedelta(minutes=5),
}


def get_name(ti):
    ti.xcom_push(key="first_name", value="RAM")
    ti.xcom_push(key="second_name", value="RAGHAV")


def greet(age, ti):
    first_name = ti.xcom_pull(task_ids="get_name", key="first_name")
    second_name = ti.xcom_pull(task_ids="get_name", key="second_name")

    print(
        f"hello Prasun Patidar  "
        f"my name is  {first_name} {second_name} and my age is: {age}"
    )


with DAG(
    default_args=default_args,
    dag_id="Prasun_with_python_operator_Airflow",
    description="our first python operator DAG flow",
    start_date=datetime(2024, 5, 4),
    schedule_interval="@daily",
) as dag:
    task1 = PythonOperator(
        task_id="greet", python_callable=greet, op_kwargs={"age": 10000000000}
    )
    task2 = PythonOperator(task_id="get_name", python_callable=get_name)

    task2 >> task1
