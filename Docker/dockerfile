FROM kalilinux/kali-rolling

# Instalação de dependências do Kali
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y python3 python3-pip git python3-dev libffi-dev libssl-dev libxml2-dev libxslt1-dev libjpeg62-turbo-dev zlib1g-dev && \
    pip3 install --upgrade pip && \
    pip install adversarial-robustness-toolbox

# Instalação de dependências adicionais
RUN apt-get install -y wireshark tcpdump metasploit-framework nmap imagemagick radare2 autopsy
# Instalação de bibliotecas Python adicionais
RUN pip install tensorflow numpy pandas scikit-learn matplotlib keras torch torchvision torchaudio opencv-python foolbox deepdream netron

# Criação do diretório de trabalho
RUN mkdir /kali
WORKDIR /kali

# Copia o conteúdo local para o diretório de trabalho no contêiner
COPY . /kali

# Comando padrão para iniciar o shell
CMD ["bash"]

