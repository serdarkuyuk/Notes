https://www.youtube.com/watch?v=3c-iBn73dDE

A way to package application with all the necessary dependencies and configuration \
Portable artifact, easily shared and moved around. isaloted environment \
Makes development and deployement more efficient

Container Repository \
Private repository \
Public repository for Docker -> DockerHub \

https://hub.docker.com/ hosted dockers official docker image.. \
search jenkins, non-official image exist...

## Environement

### Before Containers

for a development environment, developer have to align and setup their enviroment according to existing environment and things were going wrong since, every computer face various problems while installation.

PostresSQL v9.3 + Redis v5.0 -> Developer (Mac) \
PostresSQL + Redis -> Developer (Linux)

### After Container

own isolated environment \
packaged with all needed configuration \
Container (configuration, postresSQL v9.3 + Start script) \
PostgreSQL container -> Mac developer \
-> other developers

one command to install the app \
run same app with 2 different versions

## Application Deployment

### Before container

Develeper (artifact + instructions + JAR file (app) + server + database service +instructions ) \
Operations team team take these and configuration + external dependencies (dependency version conflicts) \
there are misunderstanding between developers and deployers since textual guide of deployment...

### After Container

Developer put everything to container that means encapsulated... \
No environmental configuration needed on server except Docker Runtime \
Then just pull Java App container to server

# What is a container

Layers of images \
Mostly Linux Base Image, because small in size (alpine:3.10) \
Application image on top postgres:10.10

Example \
docker hub -> search for postgres \
docker run postgres:9.6 \
downloads fromm internet... separate images are downloaded.... \
design of layer images is that when sth updated only that layer will be update not the others.. \
pull the image and start the server

database system is ready ot \

docker ps \
shows all the dockers containers \
container id + image + command + created + status + ports

image vs container \
image is the actual packages (configuration + app + start script) artifact that can be moved around \
container when I pull the image on my local machine and it starts the application that creates the container ...

docker run postgres:10:10 \
download different version (some layers are exist)

docker ps \
different application runs at the same time \

## Dockers vs Virtual Machine

Dockers on OS level \
Different levels of abstraction \
Why linux-based docker containers do not run on Windows \

Applications (2. layer) Dockers virtualize this level \
OS Kernel (1. layer) VM works this level together application level 1. \
Hardware \

Dockers images much smaller \
VM are gb \

Docker containers start and run much fast \
Compatibility : VM of any OS can run on any OS host

Some Docker+linux does not work in below Windows 10 and earlier MacOS -> docker installation toolbox

## Install Docker

two edition community and enterprise editions. \
install docker Select MacOS

pre-requisets \
docker natively runs only windows 10 \
docker toolbox workaround the incompatibility

docker engine - necessary engine \
docker CLI client - command line \
docker Compose - orchastrating multiple continers

download the community version \
multiple accounts in mac could give error

for windows 10 visisualation enabled should be done...

for linux (setup docker's repositories) \
sudo apt-get remove docker docker-engine docker.io \
sudo apt-get update \
sudo apt-get istall docker-ce=Version \
sudo docker run hello-world

## Basic Docker commands

Container is a running environment for IMAGE \
application image : postgres, redis, mongo... file systems + environment configs \
port binded: talk to application running inside of container \
virtual file system

all docker hubs are images

docker pull redis -> install images from docker hub \
docker images -> check all the images in computer \
tag means versions \
size, image id, created etc...

only image does not create container \
so my application can connect to container

docker run redis -> this will start container \
tertimante ctrl+c

new tab \
docker ps -> shows all contaners baased on the image ex image port etc... \

docker run -d redis -> run container as a detach mode \
output is the id...

docker stop idOfTheContainer \
docker start idOfTheContainer

docker stop idOfTheContainer \
docker ps \
docker ps -a -> show list of running and stopped container \
docker start idOfTheContainer

### running differen version at the same time

docker run redis:4.0 -> pulls the image and starts container \
docker ps \
I have two container... \
there are two ports... both container have same ports....

### container Port vs Host Port

multiple container can run on your host machine \
my host has only certain ports available \
we need to link them \
5000 == 5000 if you use two port in host, it will throw a error

hosts 3000 - container3000 \
host 3001 - container3000

like this
some-app://localhost:3001

docker run -p6000:6379 redis -d (note host:container)

docker ps
shows ports
0.0.0.0:6000->6379/tcp

docker run -p6001:6379 redis:4.0 -d (note: different port and version)

## Docker names

docker run -d -p6001:6378 --name redis-older redis:4.0 \
docker ps \
name is changed \
docker stop id \
docker run -d -p6000:6378 --name redis-latest redis

## Debugging Dockers

docker logs theContainerID \
docker logs nameOfContainer \
docker logs redis-older

docker exec -it theConainerId /bin/bash \
docker exec -it nameOfContainer /bin/bash

interective terminal \
curser changed to root user \
ls pwd cd... etc, I see virtual file system in the container \
curl is not available.... \
env -> shows environmental variables

exit out

# Development with Container - Example application Hands on

Frontend (html+js) + backend (node) -> localhost:3000/my-app \
Docker MongoDB database \
MongoExpress (db ui) localhost:8081/db/my-db

find official images in mongohub mongdb image and mongoExpress \
docker pull mongo \
docker pull mongo-express

docker images

### Docker Network

Isolated Docker Network \
When containers in the same network, they can talk in with their container names, without local host port etc \
MongoDb and Mongo Expres UI \
backend server comminicate from outside but eventually app will be in the network with its container and they will be in the same network. Then user can connect with localhost:3000 from outside

docker network ls -> autogenerated networks

docker network create mongo-network \
docker network ls -> it is created

> Run mongo containter \
> docker run -d \
> -p 27017:27017 \
> -e MONGO_INITDB_ROOT_USERNAME=admin \
> -e MONGO_INITDB_ROOT_PASSWORD=password \
> --name mongodb \
> --network mongo-network \
> mongo

> go to environmental variables in hub-docker website

docker logs DockerId \
attaching mongo-exress to above network

docker run -d \
-p 8081:8081 \
-e ME_CONFIG_MONGODB_ADMINUSERNAME=admin \
-e ME_CONFIG_MONGODB_ADMINPASSWORD=pasword \
--net mongo-network (due to above network) \
--name mongo-express \
-e ME_CONFIG_MONGODB_SERVER=mongodb \
mongo-express

mongo-express is available at the port localhost:8081

create user-account in the browser

docker ps \
now we have two container running, we need to connect it to node.js backend \
now change in node.js \
var MongoClient = require('mongodb').MongoClient;

to get method \

```javascript
app.get(....) {

> MongoClient.connect('mongodb://admin:password@localhost:27017, function(err, client)){ \
>  \

    .... \
    db = client.db('user-account'); \
    query ={ userid: 1}; \
    db.collection('users').findOne(query, function (err, result)){ (note user is collection) \
        ... \
        client.close() \
    } \

} \
to update method \
app.post(){ \
db.collections('users).updateOne(query, newValues, {upsert:true}, fucntion (err, res) ) \
}
```

docker logs containerIdofMongo | tail \
clear \
to stream the log \
docker logs containerIdofMongo -f \
make line last log, make other changes

## Docker Compose

mongo-docker-compose.yaml

```yaml
version: '3' (version of docker-compose)'
services:
  mongodb: (container name)
    image: mongo
    ports:
      -27017:27017 (host:container)
    environment:
      -ME_CONFIG_MONGODB_ADMINUSERNAME=admin

  mongo-express:
    image: mongo-express
    ports:
      -8080:8080
    environment:
      -ME_CONFIG_MONGODB_ADMINUSERNAME=admin
```

note: yaml file take care of network cettings..

docker-compose -f mongo.yaml up (-f means file, up starts all containers) \
docker-compose -f mongo.yaml down (also removed the networks) \

## Dockerfile

My application will be dockerized \
Blueprint for building images is dockerfile \
copy artifact (jar, war, bundle.js) \

FROM node (install node) \
ENV ME_CONFIG_MONGODB_ADMINUSERNAME=admin (set environment) \
ME_CONFIG_MONGODB_ADMINpwd=password \
RUN mkdir -p /home/app (note:folder will be created in container) \
COPY . /home/app (copy current folder files to /home/app source to container) \
CMD ["node","server.js"] (start the app with: "node server.js") \

Note: we can have multiple of RUN commands but CMD is entrypoint command

NAME SHOULD BE Dockerfile

```yaml
FROM node:13-alpine
ENV MONGO_DB_USERNAME=admin
MONGO_DB_PWD=password
RUN mkdir -p /home/app
COPY . /home/app
CMD ["node","/home/app/server.js"]
```

Every image is on top of other images \
Image Layer \
app:1.0 (This is my application) \
node:13-alpine (FROM NODE:13-alpine) \
alpine:3.10 (FROM alpine:3.10) \

### Build docker image from that Dockerfile

docker build -t my-app:1.0 . (to save current directory) \
than id will be created

docker images

docker run my-app:1.0 \
when you make an edit in Dockerfile, we have to create another image

docker ps -a | grep my-app \
docker rm ContainerID \ \
docker rmi ImageId \ \
docker images

docker run my-app:1.0 \
docker ps \
docker logs containterId \
docker exec it ContainId /bin/sh or /bin/bash

env (.... pasword set) \
ls /home/app \
Note everything in Dockerfile directory copied to this dockerfile image \
exit

## Private Docker Registery

docker images in nexus, digital ocean, amazon ECR \
Docker private repository \
Registry options \
build & tag an image \
docker login \
docker push

## Docker registery

in AWS \
ECR Elastic container registery \
create a repository \
repository name /my-app \
repository per image, but in a repository/image you can save different tags or versions \
click the app then view push commands
this give the registery ctl

in local \

1. AWS Cli needs to be installed
2. Credentials configured
   > $(aws escr......)

Image naming in Docker registeries

registryDomain/imageName:tag \
docker pull mongo:4.2 == docker pull docker.io/library/mongo:4.2 \
docker tag my-app:latest 34530495.dkr.ecr..amazon.com/my-app:latest (rename image by tag) \
docker push 34530495.dkr.ecr..amazon.com/my-app:latest

with name app \
docker build -t my-app:1.1 \
docker images

docker tag my-app:1.1 amazonName/my-app:1.1 \
docker push amazonName/my-app:1.1

## Deploy Containerized App

```yaml
version: '3' (version of docker-compose)'
services:
  my-app:
    image: 34530495.dkr.ecr..amazon.com/my-app:latest (private repository)
    ports:
      - 3000:3000 host(amazon):container
  mongodb:
    image: mongo
    ports:
      - 27017:27017 (host:container)
    environment:
      - ME_CONFIG_MONGODB_ADMINUSERNAME=admin
      - etc

  mongo-express:
    image: mongo-express
    ports:
      - 8080:8080
    environment:
      - ME_CONFIG_MONGODB_ADMINUSERNAME=admin
```

Docker-Copmose file would be used on the server to deploy all the applications/services

docker login aws repository \
vim mongo.yaml \
copy and paste all yaml file in here. \
docker-compose -f mongo.yaml up \
this install all dependences however when created everything all db is started over, and we lost the data \

**_Note_** \
we change the localhost to services because they are in the network

```javascript
app.get(....) {

previous MongoClient.connect('mongodb://admin:password@localhost:27017, function(err, client)){
changed  MongoClient.connect('mongodb://admin:password@mongodb, function(err, client)){ \
>  \

    .... \
    db = client.db('user-account'); \
    query ={ userid: 1}; \
    db.collection('users').findOne(query, function (err, result)){ (note user is collection) \
        ... \
        client.close() \
    } \

} \
to update method \
app.post(){ \
db.collections('users).updateOne(query, newValues, {upsert:true}, fucntion (err, res) ) \
}
```

## Docker Volumes

This is for data persistence. Data is gone when restarting or removing the container \
Host - Container has it's own file system like /var/lib/mysql/data \
Folder in physical host file system is mounted into the virtual file system of Docker
Container (var/lib/mysql/data) mounted to host (/home/mount/data)
data gets automatically replicated

3 Volume Types \
**_Host Valumes_** \
you decide where on the host file system the reference is made \
docker run -v /home/mount/data:/var/lib/mysql/data \

**_Anonymous Volumes_** \
for each container a folder is generated that gets mounted \
/var/lib/docker/volumes/random-hash/\_data (automatically created by Docker) \
docker run -v /var/lib/mysql/data \

**_Named Volumes_** \
you can reference the volume by name \
docker run -v name:/var/lib/mysql/data \
should be used in production

for docker-compose

```yaml
version: '3' (version of docker-compose)'
services:
  mongodb:
    image: mongo
    ports:
      - 27017:27017 (host:container)
    environment:
      - ME_CONFIG_MONGODB_ADMINUSERNAME=admin
      - etc
    volumes:
      - db-data: /var/lib/mysql/data

volumes:
  db-data
```

Example

docker-compose -f docker-compose.yaml up \
starts mongdb and express \ (adjust db name and collections)
npm run start (starts the application)
if I not use volume, I loose data

```yaml
version: '3' (version of docker-compose)'
services:
  my-app:
    image: 34530495.dkr.ecr..amazon.com/my-app:latest (private repository)
    ports:
      - 3000:3000 host(amazon):container
  mongodb:
    image: mongo
    ports:
      - 27017:27017 (host:container)
    environment:
      - ME_CONFIG_MONGODB_ADMINUSERNAME=admin
      - etc
    volumes:
      - mongo-data:/data/db      (1. Host-volume-name, 2. path-inside-of-the-container)
(for mysql: var/lib/mysql, for postgres: var/lib/postgresql/data, this path differs for each database)
This will copy local host database mongo-data to data/db when we restart the container
  mongo-express:
    image: mongo-express
    ports:
      - 8080:8080
    environment:
      - ME_CONFIG_MONGODB_ADMINUSERNAME=admin

volumes:
  mongo-data:
    driver: local
```

to check if /data/db exist \
docker ps \
docker exec -it ContainerId sh \
ls \
exit \

Example

docker-compose -f docker-compose.yaml up \
make adjustement and changes in db then \
docker-compose -f docker-compose.yaml down
docker-compose -f docker-compose.yaml up
entry is persisted.

### Docker Volume Locations

Where the dockers volumes are located.. \
for windows = C":\ProgramData\docker\volumes \
for linux = /var/lib/docker/volumes \
for macos = var/lib/docker/volumes \

cfc1ab...ddf22/\_data hash and data

note: docker for mac create a linux virtual machine and stores all the docker data here
