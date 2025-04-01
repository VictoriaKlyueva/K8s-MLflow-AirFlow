from airflow import DAG
from datetime import datetime, timedelta

from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

from train_model import train_and_log_model


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 4, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    "ml_pipeline",
    default_args=default_args,
    schedule="@weekly"
) as dag:
    # Тренировка модели
    train_task = PythonOperator(
        task_id='train_and_log_model',
        python_callable=train_and_log_model,
    )

    # Билд и пуш docker контейнера
    build_image_task = BashOperator(
        task_id='build_docker_image',
        bash_command="docker build -t iris-prediction:latest . && "
                     "docker tag vekosek3000/iris-prediction:latest iris-prediction:latest && "
                     "docker push vekosek3000/iris-prediction:latest"
    )

    # Деплой в k8s
    deploy_to_k8s_task = BashOperator(
        task_id='deploy_to_k8s',
        bash_command='kubectl apply -f deployment.yaml -n ml-svc && '
                     'kubectl apply -f service.yaml -n ml-svc && '
                     'kubectl apply -f ingress.yaml -n ml-svc'
    )

    train_task >> build_image_task >> deploy_to_k8s_task
