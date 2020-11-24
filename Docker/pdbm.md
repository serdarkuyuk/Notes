# Docker Instructions

to run the playground

https://hub.docker.com/editions/community/docker-ce-desktop-mac/
get docker desktop for mac
~476 mb

after installing dockers

install the zip file from website
https://github.com/Macuyiko/pdbmbook-docker/archive/master.zip
https://github.com/Macuyiko/pdbmbook-docker
unzip the file and put this into directory and run

> docker build .   

this will take a while (1.4 gb)

Then run
> docker images

REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
<none>              <none>              bd812ff2456f        14 minutes ago      1.48GB
docker101tutorial   latest              8febc6fcd2eb        About an hour ago   27.2MB
alpine/git          latest              76a4083eacef        4 days ago          28.4MB
nginx               latest              daee903b4e43        6 days ago          133MB

<none> id bd812ff2456f
in terminal

> docker run -i -t -p 8081:80 bd812ff2456f

in your web browser
> http://127.0.0.1:8081/

# to close playground

close the web browser

in terminal
> cmd+c
