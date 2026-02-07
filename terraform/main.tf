provider "aws" {
  region = "eu-north-1"
}

resource "aws_instance" "server" {

  ami           = "ami-073130f74f5ffb161"
  instance_type = "t3.micro"
  key_name      = "terraform-key"

  tags = {
    Name = "DevOps-Monitoring-Server"
  }
}
