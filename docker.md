An image is a lightweighted, stand-alone, executable package that includes everything needed to run a piece of software, including the code, libraries, a runtime, envrionment variables, and config files.

A container is a runtime instance of an image--what the image becomes in memory when actually executed. It runs completely isolated from the host environment by default, only accessing host files and ports if configured to do so.

`docker exec -it ${containerID} bin/bash`  Enter into bash shell of target container

#### docker volume
Create volume used for docker containers

 - `docker volume create volume_name`
 - `docker volume ls`
 - `docker volume inspect volume_name`
 - `docker volume rm volume_name`

#### container
`docker containers prune`  remove unused containers

### docker-compose

also support other docker commands like docker build, create, run ...

If project name is not specified, `docker-compose` command will use directory name as service name by default.

`docker-compose -p project-name up`  create and start containers, -d run services in detached mode  
`docker-compose -p project-name stop`  stop services  
`docker-compose -p project-name kill`  kill containers  
`docker-compose -p project-name restart`  restart services  
`docker-compose -p project-name rm  remove` stopped containers  
`docker-compose build` build or rebuild services, if project name is not specified, will use directory name  
  --force-rm  always remove intermediate containers  
  --no-cache  do not use cache when building the image
 
 `docker-compose -p project-name up -d app-name1 app-name2 ...`  restart only specified application, can also be done in interactive mode
 
 
### Dockerfile
Used to build an image, can also use another file by parameter -f:  
`docker build -f path/to/a/dockerfile`

