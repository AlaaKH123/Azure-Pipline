
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
}

dag = DAG(
    'example_job_dag',
    default_args=default_args,
    description='DAG for job example_job',
    schedule_interval='0 30 12 * * 1,3,5',
    start_date=days_ago(1),
    catchup=False,
)

start = DummyOperator(
    task_id='start',
    dag=dag,
)

run_job = BashOperator(
    task_id='run_job',
    bash_command='docker run example_image',
    dag=dag,
)

end = DummyOperator(
    task_id='end',
    dag=dag,
)

start >> run_job >> end
