#! /usr/bin/bash

sudo docker build --network=host -t server-docker -f server_dockerfile .
sudo docker tag server-docker:latest etot/server-docker:0.1
sudo docker push etot/server-docker:0.1
sudo ./reload_image_server.sh
