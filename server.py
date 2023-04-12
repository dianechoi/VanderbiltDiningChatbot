from flask import Flask, render_template, url_for, request
from kubernetes import client, config

app = Flask(__name__)
i = 0
@app.route('/')
def index():
  return render_template('index.html', name="")

@app.route('/my-link/')
def my_link():
  global i
  i += 1
  print ('I got clicked!')

  # Load the Kubernetes configuration from the service account
  config.load_incluster_config()

  # Create a Kubernetes API client
  #api = client.CoreV1Api()

  # # Define the container spec
  # container_spec = client.V1Container(
  #     name='my-container',
  #     image='nginx:latest'
  # )

  # # Define the pod spec
  # pod_spec = client.V1PodSpec(
  #     containers=[container_spec]
  # )

  # # Define the pod object
  # pod = client.V1Pod(
  #     metadata=client.V1ObjectMeta(
  #         name='my-pod-'+str(i)
  #     ),
  #     spec=pod_spec
  # )
  deployment = client.V1Deployment()
  deployment.api_version = "apps/v1"
  deployment.kind = "Deployment"
  deployment.metadata = client.V1ObjectMeta(name="nginx-deployment-" + str(i))
  deployment.spec = client.V1DeploymentSpec(
      replicas=1,
      selector=client.V1LabelSelector(
          match_labels={"app": "nginx-" + str(i)}
      ),
      template=client.V1PodTemplateSpec(
          metadata=client.V1ObjectMeta(
              labels={"app": "nginx-" + str(i)}
          ),
          spec=client.V1PodSpec(
              containers=[
                  client.V1Container(
                      name="nginx-" + str(i),
                      image="nginx:latest",
                      ports=[client.V1ContainerPort(container_port=80)]
                  )
              ]
          )
      )
  )

  # Create the deployment
  api_instance = client.AppsV1Api()
  api_instance.create_namespaced_deployment(
      body=deployment,
      namespace="default"
  )

  # Define the service specification
  service = client.V1Service()
  service.api_version = "v1"
  service.kind = "Service"
  serviceName = "nginx-service-" + str(i)
  service.metadata = client.V1ObjectMeta(name=serviceName + str(i))
  service.spec = client.V1ServiceSpec(
      selector={"app": "nginx-" + str(i)},
      ports=[client.V1ServicePort(port=80, target_port=80,)],
      type="NodePort"
  )

  # Create the service
  api_instance = client.CoreV1Api()
  api_instance.create_namespaced_service(
      body=service,
      namespace="default"
  )
  # Create a Kubernetes API client
  api = client.CoreV1Api()

  # Retrieve the Service object by name and namespace
  service = api.read_namespaced_service(name=serviceName, namespace='default')

  # Get the nodePort of the Service
  for port in service.spec.ports:
      return port.node_port

  # Create the pod
  #api.create_namespaced_pod(namespace='default', body=pod)
  return 'Click.'


    
if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')