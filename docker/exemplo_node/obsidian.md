# Instalação
## Windows
1. Instalar o WSL em: https://learn.microsoft.com/pt-br/windows/wsl/install
2. Acessar: https://docs.docker.com/desktop/setup/install/windows-install/
3. Seguir os passos e reiniciar a máquina
4. No *PowerShell* execute:
   ```bash
   docker run hello-world
```
## Linux
1. Acessar: https://docs.docker.com/engine/install/ubuntu/
2. Seguir os passos
3. Se quiser, execute o comando abaixo para adicionar seu usuário ao grupo Docker
   ```bash
  sudo usermod -aG docker $USER 
```
4. Reiniciar a máquina.
5. No *bash* execute:
   ```bash
      sudo docker run hello-world
```
# Conceitos Iniciais
## Isolamentos (Namespaces)
![[Pasted image 20241218091206.png]]

O Docker precisa encontrar imagens para resolver e executar containers, o repositório *main* é o [Docker Hub](https://hub.docker.com/).

>[!INFO] Informação
>"hello-world" é uma imagem Docker de boas vindas.
```bash
docker run --help
```

Por mais que nem sempre haja necessidade, você pode gerar containers que contenham sistemas operacionais, como por exemplo, um container com uma imagem do Ubuntu. 

O exemplo abaixo mostra como fazer o download e a utilização.
```bash
docker pull ubuntu
docker run ubuntu
```

Para verificar quais containers estão em execução no presente momento, execute:
```bash
docker ps
```
ou
```bash
docker container ls
```
*Nota:* para ver todos os containers, inclusive os que já não estão mais em execução, utilize o parâmetro `-a`.

>[!INFO] Informação
>Para que um container se mantenha "vivo", é necessário que haja no mínimo um processo em execução "dentro dele", vide a coluna COMMAND.

### Executando os primeiros comandos
```bash
docker run ubuntu sleep 1d
```

Se o comando sair como esperado, o seu terminal será travado por um dia. Utilize o `ls` para verificar se obteve êxito.

Para dar o *kill* no container, utilize o comando abaixo passando o *Container ID* ou *Name*:
```bash
container stop vibrant_johnson
```
Caso queira reexecutar, utilize:
```bash
container start vibrant_johnson
```
>[!INFO] Informação
Vide a coluna STATUS para ver há quanto tempo um container está ativo.

Você tambem pode pausar um container usando o `pause`.
## Executar comandos de formas interativas
```bash
docker exec -it vibrant_johnson bash
```
O comando acima irá iniciar o terminal bash no container, podendo assim navegar como se fosse um Ubuntu comum. Veja os processos em execução que estão o mantendo:
```bash
top
```
Após encerrar o container, caso queira remover utilize:
```bash
docker rm vibrant_johnson
```
#### Parâmetros
- `-i` interativo;
- `-t` TTY (terminal padrão).
### Ganhando tempo
```bash
docker run -it ubuntu bash
```

# Docker Samples

[Docker Samples](https://hub.docker.com/r/dockersamples/static-site) é um usuário não oficial da comunidade que posta aplicações com o fim de exemplificar a utilização do Docker de forma facilitada.

Uma aplicaçãozinha web simples será usada:
```bash
docker run -d dockersamples/static-site
```
#### Parâmetros
- `-d` detach (executar em background, sem travar o terminal).

Ao visualizar no `docker ps`, é possível visualizar que o comando utilizado mantém um processo vivo no terminal deste container.

Ao olhar a coluna de PORTS, é possível ver onde a aplicação está sendo "disponibilizada". Porém graças ao isolamento **NET**, a porta 80 do container não é uma porta acessível diretamente ao seu localhost.

Se você quiser acessar a aplicação, você precisa expor esta porta:
1. Force a remoção do container
   ```bash
   docker rm 1b6d75073457 force
```
2. Execute o container, mas passe a flag `-P` para fazer um mapeamento de todas as portas
   ```bash
   docker run -d -P dockersamples/static-site
```
3. Será possível perceber que na coluna de PORTS, o mapeamento foi realizado, através do comando abaixo é possível exibir as portas do container e quais correspondem ao localhost hospedeiro do container.
   ```bash
   docker port b0e93e405db6
```
**Saída:**
```bash
80/tcp -> 0.0.0.0:32768
443/tcp -> 0.0.0.0:32769
```
4. Logo, ao acessar http://localhost.com/32768, é possível acessar a aplicação que o container subiu.
##### Definindo a porta de forma explícita:
```
   docker run -d -p 8080:80 dockersamples/static-site
```
Logo, ao acessar http://localhost.com/8080, é possível acessar a aplicação que o container subiu.


# Imagens
Verificar imagens baixadas:
```bash
docker images
```

Para coletar mais informações (utilizando o *Image ID*):
```bash
docker inspect f589ccde7957
```
Para visualizar as camadas:
```
docker history f589ccde7957
```

As imagens são imutáveis (R/O), e o Docker é inteligente o suficiente para fazer o *pull* apenas das camadas necessárias, caso você ja tenha algumas.

O container (R/W) é uma camada temporária "em cima da imagem", onde é possível inserir informações. Essa camada do container é "fina", para que o container seja leve para ser executado, sendo assim, reaproveitando sempre a mesma imagem apenas inserindo uma camada leve R/W.

# Dockerfile
Através do comando `docker build` é possível construir imagens personalizadas. Use o parâmetro `-t` para dar uma tag à sua build, um nome para referencia-la.

Você pode conferir/listar as imagens presentes usando o comando: `docker images`.





#### Referências
[[Tecnologia]]
##### Tags
#docker #tecnologia