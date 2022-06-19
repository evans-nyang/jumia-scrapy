# Jumia-Scrapy
scrape through jumia.co.ke/mobile-phones/ using Python Scrapy  
dependencies in requirements.txt

# Building container image
docker build -t jumiadocker:latest .

# Running scraper in docker container
docker run -it --name jumiacontainer jumiadocker:latest

