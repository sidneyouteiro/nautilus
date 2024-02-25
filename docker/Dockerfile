FROM ubuntu:20.04

RUN apt update && apt install tmux htop -y

CMD ["/bin/bash"]

WORKDIR /root/dir1

RUN bash -c 'mkdir -p /root/dir1/{dir2,dir3}'
