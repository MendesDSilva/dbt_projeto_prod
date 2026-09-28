from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from datetime import datetime
import os


DBT_PROJECT_PATH = f"{os.environ['AIRFLOW_HOME']}/dags/dbt/projeto_prod"


my_dbt_dag = DbtDag(
    project_config=ProjectConfig(
        DBT_PROJECT_PATH
    ),

    profile_config=ProfileConfig(
        profile_name="projeto_prod",
        target_name="dev",
        profiles_yml_filepath=f"{DBT_PROJECT_PATH}/profiles.yml"
    ),

    execution_config=ExecutionConfig(
        dbt_executable_path=f"{os.environ['AIRFLOW_HOME']}/dbt_venv/bin/dbt"
    ),

    schedule="@daily",
    start_date=datetime(2026, 1, 1),
    catchup=False,
    dag_id="projeto_prod"
)