# Jumiascraper

A web scraper extracting phone data from [Jumia](https://www.jumia.co.ke/mobile-phones/) and loading it in a database for transformation and analysis using [Dbt](https://www.getdbt.com/).

## Usage

### Run with Docker Compose

To run the scraper using docker, execute the following commands:

1. Create a docker network:

    ```bash
    docker network create phonesjumia
    ```

2. Run docker compose:

    ```bash
    docker compose up
    ```

3. Clean up:

    ```bash
    docker compose down -v
    ```
