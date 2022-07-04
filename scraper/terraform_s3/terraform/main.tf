terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">=1.2.0"
}

provider "aws" {
  region = var.region
}

resource "aws_s3_bucket" "scrapp" {
  bucket = var.bucket_name

  tags = {
    Name = "ScrapyBucket"
  }
}

resource "aws_s3_bucket_acl" "scrapp" {
  bucket = aws_s3_bucket.scrapp.id
  acl    = "private"
}

resource "aws_s3_bucket_versioning" "versioning_scrapp" {
  bucket = aws_s3_bucket.scrapp.id
  versioning_configuration {
    status = "Enabled"
  }
}
