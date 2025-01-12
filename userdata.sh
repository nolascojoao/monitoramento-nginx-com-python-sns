#!/bin/bash
set -e

# ---------------------------
# Instalar AWS CLI NO UBUNTU
# ---------------------------
sudo apt install -y unzip
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip > /dev/null
sudo ./aws/install > /dev/null
rm -rf awscliv2.zip aws/
