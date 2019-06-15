# Load balancing with haproxy

Project was made to compare performance of haproxy algorithms depending on the web application usage frequency

## Requirements

To run project you will need:
- docker
- docker-compose

## Usage

Firstly you will need to build node-app container

```
cd node-app
docker build -t node-app .
```

Next you need to init docker swarm
```
docker swarm init
```

Last step will run the application

```
sudo docker stack deploy -c docker-compose.yml haproxy
```

If everything is setup correctly you should be able to
```
$ sudo docker service ls
[sudo] password for piotr: 
ID                  NAME                MODE                REPLICAS            IMAGE                        PORTS
gsalhcohjkzi        haproxy_app         replicated          3/3                 node-app:latest              *:30001->8080/tcp
ygd8sce6w5j6        haproxy_proxy       replicated          1/1                 dockercloud/haproxy:latest   *:12001->80/tcp

```

Application server will run on you localhost

```
$ for i in {1..10}; do printf "$(curl -s -X GET http://localhost:12001)\n"; done;
```


## License
[MIT](https://choosealicense.com/licenses/mit/)
