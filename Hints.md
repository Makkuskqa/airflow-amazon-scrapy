# Copy and set amazon scrapy package into airflow + scrapy



# Virtualenv for this project
python3 -m venv airflow-scrapy-venv
airflow-scrapy-venv/Scripts/activate
pip install requirements.txt

# run scrapy for testing
scrapy crawl amazon -s CLOSESPIDER_PAGECOUNT=3 -o test.csv


# No database with databse on local computer
    # Create docker-compose.yaml with postgres image
    docker-compose up --buid
## Migrate to vm-instance ip
    address: 35.238.68.178

    CREATE DATABASE airflow_locanwin;
    CREATE USER airflow_userlocal_win WITH PASSWORD 'airpass';
    GRANT ALL PRIVILEGES ON DATABASE airflow_locanwin TO airflow_userlocal_win;

    ------> one more
    ALTER DATABASE airflow_locanwin OWNER TO airflow_userlocal_win;
    GRANT ALL PRIVILEGES ON DATABASE airflow_locanwin TO airflow_userlocal_win;
    ALTER USER airflow_userlocal_win WITH SUPERUSER;

    \q
            psql -h 35.238.68.178 -p 5432 -U admin -d airflow_locanwin
            admin1

            GRANT ALL PRIVILEGES ON SCHEMA public TO airflow_userlocal_win;
            \q


# INSTALL AIRFLOW
    NO! pip install "apache-airflow[celery]==2.6.3" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.6.3/constraints-3.7.txt"
    NO! pip install apache-airflow-providers-postgresCollecting apache-airflow-providers-postgres

        pip install apache-airflow-providers-postgres

        mkdir airflow_project
        cd airflow_project
        $env:AIRFLOW_HOME="C:\Users\38097\Desktop\DevOps Arhitecture\Airflow_plus_scrapy\airflow-project"
        Get-ChildItem Env:

        airflow
        airflow.sfg
                             = LocalExacutor
            sql_alchemy_conn = postgresql+psycopg2://airflow_userlocal_win:airpass@35.238.68.178/airflow_locanwin
            core__load_examples = False
            webserver__base_url = http://localhost:8080

# check conn        
psql -h 35.238.68.178 -p 5432 -U airflow_userlocal_win -d airflow_locanwin
airpass

        airflow db init
!!!     airflow users create --username test1 --firstname m --lastname k --role Admin --email main_branch2023@outlook.com --password test1
        airflow users list


# RUN WSL Ubuntu 22.04.2 LTS 
cd ../mnt/c/Users/38097/Desktop/"DevOps Arhitecture"/Airflow_plus_scrapy
cd /mnt/c/Users/38097/Desktop/"DevOps Arhitecture"/Airflow_plus_scrapy

sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip
sudo pip3 install virtualenv
virtualenv -p python wsl-ubuntu-venv
source wsl-ubuntu-venv/bin/activate
sudo apt install postgresql-client-common
sudo pip3 install -r requirements.txt

mkdir airflow-project-ubuntu
cd airflow-project-ubuntu
export AIRFLOW_HOME='Arhitecture/Airflow_plus_scrapy/airflow-project-ubuntu'
export
airflow

cd /mnt/c/Users/38097/Desktop/"DevOps Arhitecture"/Airflow_plus_scrapy/airflow-project-ubuntu
nano airflow.cfg

sudo apt install python3-dev libpq-dev
pip3 install psycopg2

# !!!    airflow db init      ---> from folder, where was exported AIRFLOW HOME
airflow users create --username test1 --firstname m --lastname k --role Admin --email main_branch2023@outlook.com --password test1
airflow uers list


        airflow scheduler -D
        airflow webserver -D


gs://airflow-scrapy-amazon-storage/test.csv