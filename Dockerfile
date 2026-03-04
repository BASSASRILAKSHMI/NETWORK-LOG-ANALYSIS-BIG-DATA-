FROM bde2020/hadoop-namenode:2.0.0-hadoop3.2.1-java8

USER root

RUN sed -i 's/deb.debian.org/archive.debian.org/g' /etc/apt/sources.list && \
    sed -i 's/security.debian.org/archive.debian.org/g' /etc/apt/sources.list && \
    apt update && \
    apt install -y python3 && \
    apt clean

USER root