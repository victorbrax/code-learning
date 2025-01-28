docker build -t victorbrax/app-node:1.0 .
<!-- Irá pegar a imagem do Node lá do Docker Hub e construir uma nova imagem utilizando as configurações desejadas como base. -->
> Irá aperecer em `docker images`
> Execução:
docker run -d -p 8087:3000 victorbrax/app-node:1.0


<!-- Outros comandos -->
> Parar todos os containers em execução (usando "variáveis"):
docker stop $(docker container ls -q)


<!-- Usando bind mounts -->
> Persistindo um diretório da sua máquina no container
docker run -it -v /home/vito/garrafa:/app ubuntu bash

> Também há tmpfs mounts


> Criando bridges para estabelecer comunicação entre os containers
docker network create --driver bridge minha-bridge
docker run -it --name ubuntu1 --network minha-bridge ubuntu bash
docker inspect

> Docker Compose
# Através de arquivos .yml, é possível definir composições de containers.
# Depois adiciona os exemplos do RabbitMQ aqui, deu preguissa