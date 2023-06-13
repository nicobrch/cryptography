FROM ubuntu:20.10

COPY sources.list /etc/apt/sources.list

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y openssh-client neovim

CMD ["bash"]