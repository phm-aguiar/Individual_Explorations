docker build -t nome_do_container . # Cria a imagem a partir do Dockerfile
docker run -it -v $(pwd)/kali:/kali nome_do_container # Executa o container

