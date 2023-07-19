kubectl port-forward  --address localhost,192.168.184.129  -n kubeflow svc/ml-pipeline-ui 8889:80 >> ./logs/pipeui.out &
kubectl port-forward   --address localhost,192.168.184.129 -n kubeflow svc/ml-pipeline 8888:8888 >> ./logs/pipe.out &
kubectl port-forward  --address localhost,192.168.184.129 -n kubeflow svc/minio-service 9000:9000 >> ./logs/minio.out &
kubectl port-forward  --address localhost,192.168.184.129  -n kubeflow svc/mlflow-ui  5000:5000 >> ./logs/mlflow.out &

#kubectl port-forward  --address localhost,192.168.184.129  -n kubernetes-dashboard svc/dashboard-kubernetes-dashboard  8443:443 >> ./logs/kubernetes-dashboard.out &
#kubectl port-forward  --address localhost,192.168.184.129  -n default svc/php-svc  8989:8000 >> ./logs/php.out &


 
