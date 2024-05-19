from email.policy import default
from pdb import run
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator
from airflow.decorators import dag,task


default_args = {
    "owner": "Prasun_Patidar",
    "retries": 5,
    "retry_delay": timedelta(minutes=5),
}

@dag(
    dag_id="Prasun_with_catchup_and_backfill_Airflow",
    default_args=default_args,
    start_date=datetime(2024, 5, 1),
    schedule_interval="@daily",
    catchup=False,
) 
def prasun_with_catchup_and_backfill_airflow_workflow():
    
    @task()
    def run_task():
        print(" tis floe run ho raha he ")

    run_task()

prasun_with_catchup_and_backfill_airflow_workflow()
