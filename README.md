# Overview

A data ingestion pipeline incorporating Extract Load Transform connecting data producers and consumers.

## Prerequisites

- Python >= 3.6
- Airflow >= 1.10.0
- Docker >= 19.03.0
- Terraform >= 1.2.0
- AWS account credentials configured

## Project Structure

The project is structured as follows:

- `airflow/`: Directory containing the Airflow plugins and DAGs.
- `dataset/`: Directory containing the scraped data.
- `jumiascraper/`: Directory containing crawler entrypoint and docker files.
  - `jumiascraper/`: Contains the scrapy project files and configurations.
    - `spiders/`: Directory containing the spiders.
- `terraform_s3`: Directory containing the terraform configuration files for creating an s3 bucket.
- `README.md`: Documentation file providing an overview of the project and instructions for setup and usage.

## Getting Started

To set up the project, clone the repository:

```bash
git clone https://github.com/evans-nyang/jumia-scrapy.git
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
Feel free to update the content based on your project's specifics, including adding information about the website you are scraping, additional features, or any other relevant details.

## License

This project is licensed under the [Apache License 2.0](LICENSE).

Please note that this configuration assumes you have AWS account credentials properly configured and have the necessary permissions to create and manage AWS resources.

For more information on Terraform and AWS, refer to their official documentation:

- [Terraform Documentation](https://www.terraform.io/docs/index.html)
- [AWS Documentation](https://docs.aws.amazon.com/)
