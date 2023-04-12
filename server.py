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
  api = client.CoreV1Api()

  # Define the container spec
  container_spec = client.V1Container(
      name='my-container',
      image='nginx:latest'
  )

  # Define the pod spec
  pod_spec = client.V1PodSpec(
      containers=[container_spec]
  )

  # Define the pod object
  pod = client.V1Pod(
      metadata=client.V1ObjectMeta(
          name='my-pod-'+str(i)
      ),
      spec=pod_spec
  )

  # Create the pod
  api.create_namespaced_pod(namespace='default', body=pod)
  return 'Click.'


    
if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')