from flask import Flask, render_template, url_for, request, redirect
from kubernetes import client, config
import time

app = Flask(__name__)
i = 0


@app.route('/')
def index():
    return render_template('index.html', name="")


@app.route('/my-link/')
def my_link():
    global i
    i += 1
    print('I got clicked!')

    config.load_incluster_config()

    deployment = client.V1Deployment()
    deployment.api_version = "apps/v1"
    deployment.kind = "Deployment"
    deployment.metadata = client.V1ObjectMeta(name="bot-deployment-" + str(i))
    deployment.spec = client.V1DeploymentSpec(
        replicas=1,
        selector=client.V1LabelSelector(
            match_labels={"app": "bot-" + str(i)}
        ),
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(
                labels={"app": "bot-" + str(i)}
            ),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="bot-" + str(i),
                        image="etot/bot-docker:0.1",
                        ports=[client.V1ContainerPort(container_port=5000)]
                    )
                ]
            )
        )
    )

    api_instance = client.AppsV1Api()
    api_instance.create_namespaced_deployment(
        body=deployment,
        namespace="default"
    )

    service = client.V1Service()
    service.api_version = "v1"
    service.kind = "Service"
    serviceName = "bot-service-" + str(i)
    service.metadata = client.V1ObjectMeta(name=serviceName)
    service.spec = client.V1ServiceSpec(
        selector={"app": "bot-" + str(i)},
        ports=[client.V1ServicePort(port=5000, target_port=5000, )],
        type="NodePort"
    )

    api_instance = client.CoreV1Api()
    api_instance.create_namespaced_service(
        body=service,
        namespace="default"
    )
    api = client.CoreV1Api()
    time.sleep(0.1)
    service = api.read_namespaced_service(name=serviceName, namespace='default')

    # Get the nodePort of the Service
    for port in service.spec.ports:
        return redirect(f'http://129.114.26.125:{port.node_port}', code=302)


    return "Something went wrong. Please try again!"


if __name__ == '__main__':
    app.static_folder = 'static'
    app.run(debug=True, host='0.0.0.0')
