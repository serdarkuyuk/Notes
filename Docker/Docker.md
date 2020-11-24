# Docker Instructions

https://hub.docker.com/editions/community/docker-ce-desktop-mac/
get docker desktop for mac
~476 mb

Youtube videos
https://www.youtube.com/watch?v=bhBSlnQcq2k

Docker is a tool for running Application in an isolated environment
similar to virtual machine less memory
App run in same environment
standard for software deployment,
  easy environment, just works.

## Container vs VM
containers are an abstraction at the app layer that packages code and dependencies together. Multiple containers can run on the same machine and share same OS kernel with other containers. Each running as isolated process in user space

## Virtual Machines
VM are abstraction of physical hardware turning one server into many servers. The hypervisor allows multible VMs to run on a single machine. Each VM includes a full copy of an operating system, the application, necessary binaries and libraries, taking up tens of GBs. VMs can be slow to boot

![](./figure/docker1.png)

Benefits...
run container in seconds
less disk and memory space..
does not need full OS
deployment
testing
work

docker toolbox is previous version
docker desktop is new version.

after installation
run in terminal will show help and options

> docker

> docker --version

kill the docker in Desktop
in terminal

> docker ps
if it si running it gives contatiner id etc
says cannot connect to the docker daemon

## Docker Image
image is a templete for creating an environment of choice
