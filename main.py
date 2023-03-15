from kubernetes import client, config
from datetime import datetime
import logging

FORMAT = '%(asctime)s - %(message)s'


def get_pod_age(pod_data):
    time_now = datetime.now()
    day_minutes = int(time_now.minute + ((time_now.hour - 1) * 60))
    pod_start_time = pod_data.status.start_time
    pod_start_time_in_minutes = int(pod_start_time.minute + (pod_start_time.hour * 60))
    return day_minutes - pod_start_time_in_minutes


def get_time_log(pod_data, log_format, age):
    logging.basicConfig(format=log_format, level=logging.INFO)
    logging.info(f'Name: {pod_data.metadata.name}, labels: {pod_data.metadata.labels}, AGE: {age}min;')


if __name__ == '__main__':
    config.load_config()
    v1 = client.CoreV1Api()
    list_pod = v1.list_pod_for_all_namespaces()

    for pod in list_pod.items:
        if 'env' in pod.metadata.labels.keys() and pod.metadata.labels['env'] == 'test':
            pod_age = get_pod_age(pod)
            get_time_log(pod, FORMAT, pod_age)
        continue
