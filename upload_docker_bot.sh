#! /usr/bin/bash

sudo docker build --network=host -t bot-docker -f bot_dockerfile .
sudo docker tag server-docker:latest etot/bot-docker:0.1
sudo docker push etot/bot-docker:0.1
sudo ./reload_image_bot.sh
