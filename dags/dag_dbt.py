from airflow.decorators import task, dag
from airflow.providers.dbt.cloud.hooks.dbt import DbtCloudHook, DbtCloudJobRunStatus
from airflow.providers.dbt.cloud.operators.dbt import DbtCloudRunJobOperator
from datetime import datetime

DBT_CLOUD_CONN_ID = "dbt"
JOB_ID = "70471823480926"


@dag(
    start_date=datetime(2025, 7, 2),
    schedule='@daily',
    catchup=False
)

def run_dbt_cloud():
    rodar_dbt = DbtCloudRunJobOperator(
        task_id="dbt",
        dbt_cloud_conn_id=DBT_CLOUD_CONN_ID,
        job_id=JOB_ID,
        check_interval=60,
        timeout=360
    )
    
    rodar_dbt

run_dbt_cloud()