FROM ubuntu:20.10

COPY sources.list /etc/apt/sources.list

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y build-essential wget zlib1g-dev libssl-dev sudo

RUN useradd -rm -d /home/ubuntu -s /bin/bash -g root -G sudo -u 1000 test 
RUN echo 'test:test' | chpasswd

# Instalar OpenSSH Portable 8.3
RUN wget https://cdn.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-8.3p1.tar.gz && \
    tar zxvf openssh-8.3p1.tar.gz

WORKDIR /openssh-8.3p1

# Modificar el archivo sshd_config para reducir el tamaño del paquete de KEX
RUN rm packet.c

COPY packet.c . 

# Buildear desde source
RUN ./configure && \
    make && \
    make install

# Crea el usuario sshd para la separación de privilegios
RUN groupadd -r sshd && useradd -r -g sshd -d /var/empty -s /sbin/nologin -c "sshd Privilege Separation" sshd && \
    mkdir -p /var/run/sshd

# Crea el directorio /var/empty
RUN mkdir -p /var/empty

EXPOSE 22

CMD ["/openssh-8.3p1/sshd", "-D"]