from itertools import count
from xml.etree.ElementInclude import default_loader
from airflow.decorators import dag, task
from datetime import datetime,timedelta


default_args={
    "owner":"Prasun_Patidar",
    "retries":2,
    "retry_delay":timedelta(minutes=5),
    "":"",
    "":"",
    "":"",
}

@dag(dag_id="Prasun_with_task_flow_api_airflow",
     default_args=default_args,
     start_date=datetime(2024,5,17),
     schedule_interval='@daily')
def sample_dag_example():
    @task
    def get_count():
        return 0
     
    @task
    def get_run_task_pipline(count):
        if(count>0):
            print(f'run the task because count is :{count}')
        else:
            print(f'Not run the task because count is :{count}')
        return count
    
    @task(multiple_outputs=True)
    def get_execId_and_date(count):
        execid="RAM-SIYA-RAM"
        return{
            "count":count,
            "execId":execid
        }
    
    @task
    def end_flow(outputEnd,count_execId):
        print(f"this are the count {count_execId['count']} and execid is : {count_execId['execId']}")
        print(f"end if the task with count :{outputEnd}")


    count=get_count()
    outputEnd=get_run_task_pipline(count)
    count_execId=get_execId_and_date(count)
    end_flow(outputEnd,count_execId)

instence =sample_dag_example()

# h*#652473859#























# from datetime import datetime, timedelta
# from airflow.decorators import dag, task
# from flask.scaffold import F
# from more_itertools import first

# default_args = {
#     "owner": "Prasun Patidar",
#     "retries": 5,
#     "retry_delay": timedelta(minutes=5),
# }


# @dag(
#     dag_id="Prasun_with_task_flow_api_airflow",
#     default_args=default_args,
#     description="Our first Python Operator DAG flow",
#     start_date=datetime(2024, 5, 4),
#     schedule_interval="@daily",
# )
# def hello_world_etl():

#     @task(multiple_outputs=True)
#     def get_name():
#         return {"first_name": "Prasun", "last_name": "Patidar"}

#     @task()
#     def get_age():
#         return 27

#     @task()
#     def greet(name1, name2, age):
#         return(f"Hi Prasun, my name is: {name1} {name2} and age is: {age}")

#     @task()
#     def my_idea(arg):
#         print(f"my argument is {arg}")
#     # Call the tasks inside the DAG function
#     name_dict = get_name()
#     age = get_age()
#     input1 =greet(name1=name_dict["first_name"], name2=name_dict["last_name"], age=age)
#     my_idea(arg=input1)


# greet_dag = hello_world_etl()

# # greet_dag = hello_world_etl()
