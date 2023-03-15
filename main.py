from kubernetes import client, config

config.load_config()

v1 = client.CoreV1Api()
print("Listing pods with their IPs:")
list_pod = v1.list_pod_for_all_namespaces()

for pod in list_pod.items:
    if 'env' in pod.metadata.labels.keys() and pod.metadata.labels['env'] == 'test':
        print(pod.metadata.name, pod.metadata.labels)
    else:
        continue
