## Troubleshooting

### Docker permission denied
Fix:
sudo usermod -aG docker $USER
newgrp docker

### Flask not accessible
Fix:
app.run(host='0.0.0.0', port=80)

### Azure login issue
az login --use-device-code
