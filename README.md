# 🛰️ Hybrid Cloud + Self-Healing Infrastructure (AWS + On-Prem)

Simulated Hybrid Cloud project using VirtualBox (on-prem) and AWS VPC (cloud) connected via IPsec VPN.  
Includes self-healing automation using CloudWatch + Lambda and ML-based anomaly detection with Amazon Lookout.

---

## 🧠 What This Project Includes

- VirtualBox-based simulated "on-prem" Linux server
- AWS VPC with EC2 (private subnet)
- StrongSwan VPN tunnel (IPsec/IKEv2)
- Shared services (Secrets Manager, S3, Lambda)
- Self-healing Lambda triggered by CloudWatch alarms
- ML anomaly detection via Amazon Lookout or SageMaker
- IaC via Terraform (AWS infra)
- Optional VM provisioning with Ansible

---

## 📁 Folder Structure


