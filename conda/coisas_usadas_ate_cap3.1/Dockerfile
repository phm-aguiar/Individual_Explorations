FROM continuumio/miniconda3

# Instala o Jupyter
RUN /opt/conda/bin/conda install jupyter -y --quiet
RUN pip install statistics pandas matplotlib scipy numpy seaborn scikit-learn xlrd openpyxl

# Define o diretório de trabalho
WORKDIR /opt/notebooks

# Expõe a porta 8888
EXPOSE 8888

# Executa o Jupyter Notebook quando o contêiner for iniciado
CMD ["/opt/conda/bin/jupyter", "notebook", "--notebook-dir=/opt/notebooks", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"]
