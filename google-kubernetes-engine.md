# Google Kubernetes Engine

## Preparation

1. Install [Google Cloud SDK](https://cloud.google.com/sdk/docs/quickstarts)

2. Install Kubernetes command line tool  
  `gcloud components install kubectl`

3. Set project id and compute zone for cloud sdk.  

	```
	gcloud config set project PROJECT_ID
	gcloud config set compute/zone us-central1-b
	```

## Deploy local code to Kubernetes Engine

#### Build container image
Move to source directory,  
set project id so that it can be used to identify images later on.  

`export PROJECT_ID="$(gcloud config get-value project -q)"`

Then build docker image  

`docker build -t gcr.id/${PROJECT_ID}/hello-app:v1 .`

After that, uses can check building result  

`docker images | grep ${PROJECT_ID}`

##### Name of the docker image to Kubernetes cluster
`[HOSTNAME]/[PROJECT-ID]/[IMAGE]@[IMAGE_DIGEST]`

 - `[HOSTNAME]`  location in the console, available options: `gcr.io`, `us.gcr.io`, `eu.gcr.io`, `asia.gcr.io`
 - `[PROJECT-ID]`  GCP project ID
 - `IMAGE`  image name
 - `[IMAGE_DIGEST]`  the sha256 hash value of the image contents

#### Upload container image

`gcloud docker -- push gcr.io/${PROJECT_ID}/hello-app:v1`

Optionally, you can also enable docker cli access to Google Container Registry

`gcloud auth configure-docker`, then

`docker push gcr.io/${PROJECT_ID}/hello-app:v1`

#### Create a container cluster

`gcloud container clusters create hello-cluster --num-nodes=3`

Check working VM instances once creation is done.  

`gcloud compute instances list`

#### Deploy application  
After the configuration initially, `kubectl` can be used locally and control Cloud Kubernetes Engine.  

`kubectl run hello-web --image=gcr.io/${PROJECT_ID}/hello-app:v1 --port 8080`

Check the pods created  

`kubectl get pods`

#### Expose application to the Internet
`kubectl expose deployment hello-web --type=LoadBalancer --port 80 --target-port 8080`

Check established service  

`kubectl get service`

#### Scale up application
Change replicas to intended number to scale VMs in the cluster

`kubectl scale deployment hello-web --replica=4`

Get deploy information  

`kubectl get deployment hello-web`

Check pods after scaling  

`kubectl get pods`

## Deploy a new version  
When a new version is released, you need to build a new version of docker image (or rebuild the original image?) and update the new image to Kubernetes cluster.

1. Build a new version of docker image  

 `docker build -t gcr.io/${PROJECT_ID}/hello-app:v2`

2. Push the image to Google Container Registry  

 `gcloud docker -- push gcr.io/${PROJECT_ID}/hello-app:v2`

3. Apply a rolling update to the existing deployment with an image update  

 `kubectl set image deployment/hello-web hello-web=gcr.io/${PROJECT_ID}/hello-app:v2`

 "hello-app" is set when deploying the application

## Cleaning up

1. Delete the service

 `kubectl delete service hello-web`

2. Wait for the Load Balancer provisioned for the hello-web Service to be deleted

 `gcloud compute forwarding-rules list`

 This command will return 0 rules if deletion succeeded

3. Delete the container cluster

 `gcloud container clusters delete hello-cluster`

## Notes
##### Service in Kubernetes Engine
**Service** is a set of Pod endpoints in a cluster, differenct pods can be accessed simply be service.  
There are 5 types of services: **ClusterIP**, **NodePort**, **LoadBanlancer**, **ExternalName**, **Headless**  
`ClusterIP` is the default service type, `LoadBanlancer` is the only type that exposes to the internet.

##### `kubectl` commands
`kubectl` commands to Kubernetes command line tools is what `docker` commands to Docker command line tools.

 - `kubectl apply -f yaml-file-path` can create cluster/service according to configuration file
 - `kubectl get pods` Get pods in current project
 - `kubectl exec -it pod-name [-c container-name] sh` Enter a specific Pod in command line
 - `kubectl get service service-name -o yaml` Shows service configurations in the format of yaml
 - `kubectl port-forward svc/${SERVICE_NAME} ${PORT}:${PORT}` Create proxy to forward local request to service in cluster, the proxy needs to be recreated when the original pod is removed.

##### Switch Kubernetes cluster
`gcloud container clusters get-credentials ${CLUSTER_NAME} --region ${PROJECT_REGION} --project ${PROJECT_ID}`  
kubectl controls cluster according to current cluster configurations.

###### ConfigMaps
`kubectl create configmap [NAME] [DATA]` Create a configmap  
`kubectl create configmap [NAME] --from-file [/PATH/TO/DIRECTORY]`  Create configmap from files in a directory  
`kubectl get configmap [NAME] -o yaml`  list configurations in a configmap

##### gcloud configurations
`gcloud` can create configurations in set, activate and deactivate as a group.

 - `gcloud config configurations create configuraiton-name` Create a new named configuration, enable it by default, use `--no-activate` param to avoid activating the new configuration.
 - `gcloud config configurations activate configuration-name` Activate a configuration by name, you can change the configurations after it's activated, the changes are saved in current configurations. You don't need to deactivate a configuration, just switch to another one.
 - `gcloud config configurations describe configuration-name` Describe a configuration in detail
 - `gcloud config configurations delete configuration-name` Delete a configuration
 - `gcloud config configurations list` List existing configurations, can apply filter expressions via param `--filter`

