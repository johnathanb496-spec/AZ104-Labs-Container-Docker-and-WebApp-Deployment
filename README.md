🚀 Azure Container Lab (AZ-104)
📌 Overview

This project demonstrates deploying a containerized web application in Microsoft Azure using Docker and Azure Container services.

🧱 Architecture
Local VM → Docker → Azure Container Registry → Azure Container Instances
⚙️ What I Built

Flask web app

Docker container

Deployed to Azure Container Instances

🐳 Run Locally
docker build -t mywebapp .
docker run -d -p 80:80 mywebapp
☁️ Deploy to Azure
docker tag mywebapp <registry>.azurecr.io/mywebapp
docker push <registry>.azurecr.io/mywebapp
🛠️ Skills Demonstrated

Linux VM setup

Docker containerization

Azure Container Registry

Azure Container Instances

Troubleshooting real errors


## 📸 Screenshots

<img width="1510" height="1171" alt="image" src="https://github.com/user-attachments/assets/94a12c66-b81a-43f8-98ff-ee84a2eb219c" />



