variable "project_id" {
    description = "Project ID (not just name)"
    default = "rclone-446420"
  
}

variable "region" {
    description = "Project region for use with provider specs"
    default = "us-central1"
}

variable "bucket_name" {
    default = "rclone-446420-bucket"
}

variable "cred_location" {
    default = "/home/abbythecat27/my-de-zoomcamp/1_docker_gcp_terraform/gcp_key/rclone-446420-a9a8eec51226.json"
}