# 🛰️ HITCLOUD – Hybrid AI-Powered Self-Healing Cloud Infrastructure

A next-gen **modular AI-driven cloud framework** built for hybrid deployments.  
HITCLOUD includes **three autonomous agents** – each handling detection, healing, and scaling — across **on-prem and AWS** zones.

> 💡 Designed for real-time anomaly detection, automated remediation, and infra orchestration with zero human intervention.

---

## 🧠 Architecture Overview

```
                +------------------------------+
                |  CloudWatch / EventBridge    |
                +------------------------------+
                             |
          +------------------+------------------+
          |                                     |
          v                                     v
     +----------------+                 +----------------+
     |   Agent 47     |   →  GPT / Claude API  ←   Agent 48   |
     | (Anomaly Intel)|                 | (Threat Control) |
     +----------------+                 +----------------+
                  \                          /
                   \                        /
                    \                      /
                  +---------------------------+
                  |       Agent 49            |
                  |  Infra Commander / Orchestrator |
                  +---------------------------+
                             |
           +----------------+----------------+
           |                                 |
           v                                 v
   AWS Infrastructure                On-Prem VirtualBox
 (EC2, Docker, VPC, Lambda)      (Ubuntu + Docker + Agent Daemon)
```

---

## 🧩 Modular Agent Roles

| Agent        | Role |
|--------------|------|
| **Agent 47** | CloudWatch + Log monitor → OpenAI/Claude → Detect anomaly type |
| **Agent 48** | CPU spike / Fork bomb detector → Whitelist/Blacklist logic |
| **Agent 49** | Infra scaling + EC2 reboot/recover → Terraform / Docker orchestration |

---

## 🔒 Hybrid Cloud Connectivity

- **AWS ↔️ On-Prem via StrongSwan (IPsec VPN)**
- Secure sync with bash/cron-based daemons
- SSH-triggered workflows for local automation

---

## 🚀 Self-Healing Capabilities

- Auto-reboot crashed EC2
- Disk cleanup when full
- Kill rogue/forkbomb processes
- Whitelist safe processes to avoid false alarms
- Blacklist repeat offenders
- Anomaly classification via OpenAI or Claude

---

## 🛠️ Tech Stack

- **AWS**: Lambda, EC2, CloudWatch, EventBridge, S3, IAM, Secrets Manager
- **Infra as Code**: Terraform
- **AI**: OpenAI API, Claude LLM
- **Hybrid VPN**: StrongSwan (IKEv2/IPsec)
- **On-Prem Stack**: VirtualBox, Ubuntu, Bash, Python, Docker
- **Automation**: Ansible, Python Daemon Agents

---

## 📁 Project Structure

```
├── terraform/                # IaC for AWS infra
├── agents/
│   ├── agent47/              # GPT Anomaly Detector
│   ├── agent48/              # Forkbomb / Threat Shield
│   └── agent49/              # Infra Commander
├── daemon/                   # On-prem sync agent (Python + Bash)
├── vpn-config/               # StrongSwan tunnel configs
├── lambda/                   # Self-healing and routing logic
├── ascii-diagram.txt         # The glorious ASCII map
└── README.md                 # You're here
```

---

## 📦 Getting Started

1. Spin up on-prem server via VirtualBox (Ubuntu preferred)
2. Configure VPN tunnel (use `vpn-config/`)
3. Deploy AWS side via `terraform apply`
4. Install on-prem daemon (`daemon/agent.sh`)  
5. Sit back — let HITCLOUD heal, scale, and protect

---

## 🧠 Bonus: Add More Agents?

The framework is plug-and-play.  
Add more agents like:
- Log classifier (Agent 50)
- RAG + context summarizer
- Predictive scale-out logic
- Multi-region resilience controller

Just register them under the central dispatcher.

---

## 🏁 Author

**Sudharsan V. (aka ghostanon17)**  
Lead Architect – Project HITCLOUD  
[Portfolio](https://sudharsan17.online) • [LinkedIn](https://linkedin.com/in/sudharsan177) • [Zenpulse Demo](https://sim.sudharsan17.online)

---

## 🔒 License

PRIVATE — All rights reserved. Redistribution or reuse prohibited without explicit permission.
