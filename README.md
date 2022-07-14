# Jumia-Scrapy
Create a data ingestion pipeline by incorporating ELT(Extract Load Transform) approach. Crawl through jumia.co.ke/mobile-phones/ using Python Scrapy framework to obtain phone listings, insert the raw data into an Amazon S3 bucket. We'll then leverage ETL(Extract Transform Load) system when retrieving the data from s3 bucket into a postgres database for exploratory analysis.

# Terraform 
+ Create a variables.tf in same directory as main.tf, use var_example file as template
+ Commands:
  - terraform init
  - terraform fmt
  - terraform validate 
  - terraform plan
  - terraform apply

# Dockerization
+ How To:
  + Create docker network
    - docker network create phonesjumia
  + Build container image
    - docker build -t jumiadocker:latest .
  + Run docker compose
    - docker compose up
  + Run docker image as a container
    - docker run -it --network phonesjumia --link phonesdatabase --name jumiacontainer --rm jumiadocker:latest /bin/bash
  + Run crawler in bash
    - python run.py
