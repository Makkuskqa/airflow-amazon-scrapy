from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'mksm',
    'depends_on_past': True,   # which means the execution of each instance of this DAG doesn't rely on the success of the previous run
    'start_date': datetime(2023, 8, 9),
    'retries': 0,              # If the task fails, Airflow will try to run it zero more time
}

dag = DAG(
    'scrapy_spider',
    default_args=default_args,
    description='Run Scrapy Spider',
    schedule_interval='*/10 * * * *',  # This means every x minutes
    catchup=False,
)

run_spider = BashOperator(
    task_id='run_scrapy_spider',
    bash_command = r'''
        cd "/mnt/c/Users/38097/Desktop/DevOps Arhitecture/Airflow_plus_scrapy/amazon-python-scrapy-scraper" && 
        source "/mnt/c/Users/38097/Desktop/DevOps Arhitecture/Airflow_plus_scrapy/wsl-ubuntu-venv/bin/activate" &&
        scrapy crawl amazon -s CLOSESPIDER_PAGECOUNT=3 -o test.csv
        ''',
    dag=dag,
)


