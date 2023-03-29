FROM continuumio/anaconda3:latest

RUN apt-get update

#copiar proyecto
COPY ./ ./challenge_wallmart


# Crear y activar entorno conda
RUN conda create -n wallmart_spider python=3.8
RUN echo "conda activate wallmart_spider" >> ~/.bashrc

SHELL ["/bin/bash", "--login", "-c"]

#instalar nano y frameworks para conda
RUN apt-get install nano -y
RUN conda install -n wallmart_spider scrapy
RUN conda install -n wallmart_spider flask

# Agregar script para ejecutar comandos
COPY start.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/start.sh

# Exponer puerto
EXPOSE 5000

# Iniciar comando de arranque
WORKDIR "/challenge_wallmart/wallmart"
CMD ["bash", "/usr/local/bin/start.sh"]

# docker build -t wallmart_spider:1.0 .
# docker run -p 5000:5000 wallmart_spider:1.0