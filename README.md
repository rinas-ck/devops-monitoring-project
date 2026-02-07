# 🚀 DevOps CI/CD & Monitoring Project

## 📌 Overview
End-to-end DevOps project deploying a containerized Flask application on AWS EC2 with automated CI/CD and monitoring.

## 🏗 Architecture
- Terraform – Infrastructure provisioning
- AWS EC2 – Cloud server
- Docker – Application containerization
- GitHub Actions – CI/CD pipeline
- Prometheus – Metrics collection
- Grafana – Visualization

## 🔁 CI/CD Workflow
1. Code pushed to GitHub
2. GitHub Actions triggered
3. SSH to EC2
4. Pull latest code
5. Build Docker image
6. Restart container

## 📊 Monitoring Stack
- Node Exporter
- Prometheus
- Grafana Dashboard (ID: 1860)

## 🌐 Access
- Application: http://<EC2_PUBLIC_IP>
- Prometheus: http://<EC2_PUBLIC_IP>:9090
- Grafana: http://<EC2_PUBLIC_IP>:3000

## 📸 Screenshots

### Live Application
![App](screenshots/app-live.png)

### CI/CD Pipeline
![CI/CD](screenshots/github-actions.png)

### Grafana Dashboard
![Grafana](screenshots/grafana-dashboard.png)

### Prometheus Targets
![Prometheus](screenshots/prometheus-targets.png)

### Terraform Deployment
![Terraform](screenshots/terraform-apply.png)

## 👨‍💻 Author
Rinas CK  
DevOps Engineer
