# AZ104-Labs-Container-Docker-and-WebApp-Deployment
This is a demonstration on how to build, store, and deploy containerized applications in azure.
🚀 Azure Container Lab (AZ-104)
📌 Overview

This project demonstrates deploying a containerized web application in
Microsoft Azure using:

Linux Virtual Machine

Docker

Azure Container Registry

Azure Container Instances

🧱 Architecture
User → Web Container → Azure Container Registry → Azure Container Instances
⚙️ What I Built

A Flask web app that returns:

Hello from Azure Container Lab!

Containerized the app using Docker

Pushed the image to Azure Container Registry

Deployed it using Azure Container Instances

🛠️ Key Skills Demonstrated

Linux server setup and SSH

Docker containerization

Azure CLI usage

Cloud deployment with ACI

Troubleshooting real-world errors

🐳 Application Code
app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Azure Container Lab!"

app.run(host='0.0.0.0', port=80)
Dockerfile
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install flask
CMD ["python", "app.py"]
🚀 Deployment Steps
# Build container
docker build -t mywebapp .

# Run locally
docker run -d -p 80:80 mywebapp

# Push to Azure
docker tag mywebapp <registry>.azurecr.io/mywebapp
docker push <registry>.azurecr.io/mywebapp
🌐 Result

Application successfully deployed and accessible via Azure Container Instances.
