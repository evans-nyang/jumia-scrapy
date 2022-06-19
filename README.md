# Jumia-Scrapy
scrape through jumia.co.ke/mobile-phones/ using Python Scrapy  
dependencies in requirements.txt

# Building container image
docker build -t jumiadocker:latest .

# Running scraper in docker container
docker run -it --name jumiacontainer jumiadocker:latest
<!-- run container in bash shell to see ingestion changes in dataset directory -->
docker run -it --name jumiacontainer --rm jamdocker:latest /bin/bash

