# Jumiascraper

This project is a web scraping tool designed to extract data from a website and store it for further processing. It utilizes the Python programming language along with libraries such as scrapy and sqlalchemy.

## Usage

Change directory to jumiascraper

```bash
cd jumiascraper
```

Install the required dependencies:

```bash
pip install --no-cache-dir -r requirements.txt
```

To run the scraper, execute the following command:

```bash
python run.py
```

This will initiate the scraping process and store the scraped data in the `dataset/` directory.

## Docker

To run the scraper using docker, execute the following commands:

1. Create a docker network:

    ```bash
    docker network create phonesjumia
    ```

2. Run docker compose:

    ```bash
    docker compose up
    ```

3. Build a Docker image:

    ```bash
    docker build -t jumiadocker:latest .
    ```

4. Spin up the Docker container in bash mode:

    ```bash
    docker run -it --network phonesjumia --link phonesdatabase --name jumiacontainer --rm jumiadocker:latest /bin/bash
    ```

5. Run the scraper:

    ```bash
    python run.py
    ```
