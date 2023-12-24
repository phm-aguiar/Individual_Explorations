# Use a imagem base do Debian
FROM debian:latest
RUN apt-get update && \
    apt-get install -y build-essential gcc g++ make cmake && \
    apt-get install -y vim gdb valgrind && \
    apt-get install -y git wget curl && \
    apt-get install -y libssl-dev libncurses5-dev libncursesw5-dev && \
    apt-get install -y zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev && \
    apt-get install -y llvm libncurses5-dev libncursesw5-dev tk-dev libffi-dev liblzma-dev python3-openssl && \
    apt-get install -y python3-pip && \
    apt-get install -y clangd && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY . /app
CMD ["/bin/bash"]

