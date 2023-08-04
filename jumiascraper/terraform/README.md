# Terraform

This Terraform template creates an AWS S3 bucket with versioning enabled and sets its ACL to private.

## Resource Configuration

The Terraform configuration file (`main.tf`) defines the AWS resources required to deploy the serverless website. It creates the following resources:

- `aws_s3_bucket`: Creates an S3 bucket to store the website files.
- `aws_s3_bucket_acl`: This resource block sets the Access Control List (ACL) of the S3 bucket created earlier to "private".
- `aws_s3_bucket_versioning`: This resource block enables versioning for the S3 bucket, ensuring that multiple versions of objects can be stored and accessed.

## Usage

1. Change directory to terraform_s3

    ```bash
    cd terraform
    ```

2. Create a new file `variables.tf` in same directory as main.tf, use var_example file as template.

3. Review the configuration in `main.tf` and make any necessary changes.

4. Initialize the Terraform working directory:

    ```bash
    terraform init
    ```

5. Format and validate the Terraform configuration:

    ```bash
    terraform fmt
    terraform validate
    ```

6. Preview the resources that will be created by running the command:

    ```bash
    terraform plan
    ```

7. Apply the Terraform configuration:

     ```bash
    terraform apply
    ```

    When prompted, enter `yes` to confirm the action.

## Clean Up

To destroy the deployed infrastructure and delete all resources created by this Terraform configuration, run the following command:

```bash
terraform destroy
```
