notes base on https://www.youtube.com/watch?v=X48VuDVv0do

Trend from monolith to microservices \
increased usage of containers \
Demand for a proper way of managing those hundereds of containers

High availabilty or no downtime \
scalibility or high performance \
disaster recovery, backup and restore \

## K8s Components

### Node and Pod

In one node (server) there could be many pods
Smallest unit of K8s \
Abstraction over container \
You only interact with the k8s layer \
Usually 1 application per pod \
Each pod gets Ip address (internal)
Each pod can comminicate, if a container dies, a new one created
when there is a new container, pod starts again a new ip address assigned

### Service

Permanent Ip address. \
lifecycle of pod and service is not connected \
Ingress get the domanain name and forword it to services \

### ConfigMap and Secret

for example, if database url changes, you need to push to repo, pull it in your pod etc... \
for this ConfigMap exist in K8s \
it is external configuration of your application \
with this you will change only url in configmap \
no need to go whole cycle \
however if db user or password changes, you can not put it in to ConfigMap \
for this there is Secret \
it is base64 encoded, the built-in security mechanism is not enabled by default \
Use it as environment variables or as a properties file

### Data storage, Volume

If database restart again, data is lost \
Volumes are persist the data \
Storage on local machine or remote, outside of the K8s cluster \
external reference storage, external pluged in hdd \
K8s does not manage data persistance \

### Deployment and Stateful Set

To service all the time and user experience, the replica is connected to the same Service \
Two node has two application to connected service with permanent IP, services has 2 functionalities \
Service is like a load balancer.
you define a blueprint for pods, and define how many replicas you would like to run \

Deployement: blueprint for my-app pods \
we crete Deployments, it is an abstraction of Pods \
Databases can not be replicated via Deployment because it has states \
Databases should be shared hdd.

StatefulSet
for stateful apps, elastic, mongoDB, MySQL should be created by stateful apps or databases \
Database in K8s is tedious so DB are often hosted outside of K8s cluster \

## Kubernetes Architecture

### Master and slaves

**_Node process_**

each node has multiples pods on it \
3 processes must be installed on every node (kubelet, kube proxy, container runtime) \
Worerker Nodes do the actual work \
Kubelet interacts with both container runtime and node (server)

Kubelet starts the pod with a container inside \
kuberneties cluster contains multiple nodes, container runtime, kubelets should be installed \
comminication is done by Services, which is a load balancer \
Kube proxy forwards the requests

Managing processes are done by Master Nodes

4 processes run on every master node \

1. Api Server which interact with client, is like a cluster gateway \
   acts as a gatekeeper for authentication. Only 1 entrypoint into the cluster \
   some request -> Api server -> validates request -> other process -> pods (logs )
2. Scheduler : Schedule new Pod -> API server -> Scheduler -> Where to put the Pod (based on resources) -> Kubelet
3. Controller manager, when pods died, it detects and rescheduler, it detects cluster state changes and recover the pod as soon as possbile. Controller Manager -> Scheduler -> Kublet
4. etcd, this is a key value store in master node, it is cluster's brain. All chaanges updated and save, get stored in the key value store of etcd. Application data is not stored in etcd. Cluster states data is here. There are multiple master in real application. API server is load balanced. Etcd are distributed storage across all master nodes.

### Example Cluster Setup

Master needs less work so resource could be smaller. On demand master and workers can be increase. \
Add new Master/node server \

1. get new bare server
2. install all the master/worker node process
3. add it to the cluster

### Minikube and kubectl - local setup

Production cluster setup. Multiple master and worker nodes, separate virtual or physical machines \
test on local machine?

#### Minikube

Master and Node processes run on one machine. Docker pre-installed. Minikube creates virtual box on laptop. Nodes runs in that Virtual Box. 1 node K8s cluster for testing purposes. \
To interact kubectl is for

#### kubectl

Command line tool for k8s cluster. UI vs API vs CLI (kubectl)
enable pods to run on node, create, destroy pods or create services

## Installation

Installation \
brew update \
brew install hyperkit \
brew install minikube (kubctl alos installed) \
kubectl \
minikube \
clear \
minikube start --vm-driver=hyperkit \
kubectl get nodes (get status of nodes) \
minikute status (host, kubelet apiserver kubeconfig running configured) \
kubectl version (both client and server versions installed) \

### Main Kubectl Commands

#### create, edit, delete, get, log

Create and debug Pods in a minikube cluster

1. kubectl get nodes (status of the nodes)
   kubectl get pod
   kubectl get services

2. kubectl create -h
   (Pod is the smallest unit but is not created by users) there is an abstraction layer, deployment \
   kubectl create deployment NAME --image=image [--dry-run] [options]
   kubectl create deployment nginx-depl --image=nginx
   kubectl get deployement
   kubectl get pod
   deployment is the blueprint for creating pods, most basic configuration for deployment (name and image to use)
   rest defaults
   kubectl get replicaset (replicaset is managing the replicas of a Pod)

Layers of Abstraction

Deployment manages a \
ReplicasSet manages a \
Pod is an abstraction of \
Everything below Deployement is handled by Kubernetes

kubectl edit deployment nginx-depl (will auto-generated configuration file with default values) \
go and edit something, it will auctomatically delete the old pod and start new one \
kubectl get replicaset (oldone deleted, new one is created)

kubectl logs podName \
kubectl create deployment mongo-depl --image:mongo \
kubectl get pod \
kubectl logs nameOfPod \
kubectl describe pod podName \
kubectl get pod 

kubectl exec -it podName -- bin/bash (inside of application, ls, pwd etc)

kubectl get deployment \
kubectl get pod \
kubectl delete deployment mongo-depl \
kubectl get pod \
kubectl get replicaset \
kubectl delete deployment nginx-depl

#### apply

kubectl apply - fileNameConfig.yaml \
touch config.yaml

nginx-deployment.yaml \

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec: (for deployment)
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec: (for pods)
      containers:
        - name: nginx (one container)
          image: nginx:1.16
          ports:
            - containerPort: 80
```

kubectl apply -f nginx-deployment.yaml \
kubectl get pod \
kubecty get deployment \
K8s knows when to create or update deployment \
(you can apply services volumes etc...)

### Yaml configuration file in Kubernetes

1. Metadata
2. Specification (deployment, services will have different attributes)
3. Status (automatically generated and added by Kubernetes) Kubernetes will always look at desired and actual states, if there is no match, K8s will make it happen. K8s updates its states constantly. etcd is cluster brain, it holds the current status of any K8s components

```yaml
apiVersion: apps/v1
kind: Deployment or kind: Service
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec: (for deployment)
  replicas: 1
  selector:
  template:
    metadata:
      labels:
        app: nginx
    spec: (for pods)
      containers:
        - name: nginx (one container)
          image: nginx:1.16
          ports:
            - containerPort: 80
```

store them in the application code. \
Template has its own metadata and spec section. Specs will define port, image name etc..

#### Connection components

Between deployment and service via labels and Selectors \ 
metadata contains labels, and spec contains selector
 