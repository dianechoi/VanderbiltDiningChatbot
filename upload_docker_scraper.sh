#! /usr/bin/bash

sudo docker build --network=host -t scraper-docker -f scraper_dockerfile .
sudo docker tag bot-docker:latest etot/scraper-docker:0.1
sudo docker push etot/scraper-docker:0.1
sudo ./reload_image_scraper.sh
