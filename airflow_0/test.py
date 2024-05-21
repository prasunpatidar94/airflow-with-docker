from airflow.decorators import dag, task
from datetime import datetime, timedelta
from airflow.providers.mysql.operators.mysql import MySqlOperator

default_args = {
    "owner": "Prasun_Patidar",
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}

@dag(
    dag_id="Prasun_with_mysql_database_airflow",
    default_args=default_args,
    start_date=datetime(2024, 5, 17),
    schedule_interval="@daily",
    catchup=False,
)
def sample_dag_example():

    @task
    def get_count():
        return 0

    @task
    def get_run_task_pipeline(count):
        if count > 0:
            print(f"Run the task because count is: {count}")
        else:
            print(f"Not run the task because count is: {count}")
        return count

    @task(multiple_outputs=True)
    def get_execId_and_date(count):
        execid = "RAM-SIYA-RAM"
        return {"count": count, "execId": execid}

    @task
    def end_flow(outputEnd, count_execId):
        print(
            f"These are the count {count_execId['count']} and execid is: {count_execId['execId']}"
        )
        print(f"End of the task with count: {outputEnd}")

    select_table_mysql_task = MySqlOperator(
        task_id="GET_COUNT_BY_SQL",
        mysql_conn_id="mysql_localhost",
        sql="SELECT * from jobExec je WHERE je.jobName = 'job10' and je.busDt ='2023-01-10'",
        dag=sample_dag_example,
    )
    
    count = get_count()
    run_task_output = get_run_task_pipeline(count)
    count_execId = get_execId_and_date(count)
    end_flow(run_task_output, count_execId)

    select_table_mysql_task >> count  # Setting the task dependency

instence = sample_dag_example()
