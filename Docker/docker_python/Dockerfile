# Use a imagem base do Anaconda
FROM continuumio/anaconda3

# Exponha a porta 8888 para o Jupyter Notebook
EXPOSE 8888
# Configure o ambiente do Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
