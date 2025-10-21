🛡️ Custor API

Automated Website Security, Maintenance & Global Compliance Platform.
Custor is a SaaS platform designed to automate the monitoring, maintenance, and compliance of websites (starting with WordPress) according to international security and data-protection standards.

🚀 Objective

The goal of Custor is to provide a fully automated solution for:
🔒 Technical Security: plugin/core updates, backups, hardening, and rollback.
⚖️ Legal Compliance: IT-Grundschutz, NIS2, GDPR (EU), NIST & CCPA (US), PIPEDA (CA).
🤖 Artificial Intelligence: automatic vulnerability analysis, human-readable explanations, remediation suggestions, and audit summaries.
📊 Auditable Reporting: PDF/Word reports for auditors, insurers, and management.

🧩 System Architecture
┌────────────────────────────┐
│        CUSTOR CLOUD        │
│────────────────────────────│
│ Django API  +  Celery      │
│ PostgreSQL + Redis + S3    │
│ Compliance Engine (YAML)   │
│ AI Microservice (LLM API)  │
└──────────────┬─────────────┘
               │ REST API (JWT)
               ▼
┌────────────────────────────┐
│     CUSTOR WP-AGENT        │
│ Plugin → REST / WebSocket  │
│ Scan, Backup, Fix, Update  │
└────────────────────────────┘
               │
               ▼
┌────────────────────────────┐
│  CUSTOR APP (Frontend)     │
│ Next.js 15 + Tailwind CSS  │
│ Dashboard, Reports, Alerts │
└────────────────────────────┘

⚙️ Technology Stack
Component	Technology
Backend	Django 5 + Django REST Framework
Task Queue	Celery + Redis
Database	PostgreSQL 15
Storage	MinIO / AWS S3
Frontend	Next.js 15 (TypeScript + Tailwind CSS)
Monitoring	Prometheus + Grafana + Loki
AI Module	OpenAI / Anthropic (LLM-based)
Containerization	Docker + Docker Compose
CI/CD	GitHub Actions

🧱 Project Structure
custor-api/
├── config/              # Django settings, URLs, ASGI/WSGI
├── apps/
│   ├── core/            # Health check, utils, logging
│   ├── user/            # Authentication, JWT, roles
│   ├── workspace/       # Multi-tenant workspace management
│   ├── wp_site/         # WordPress scanning and sync logic
│   ├── compliance/      # YAML rule engine (EU/US/CA)
│   ├── ai_assistant/    # AI-based vulnerability explanations
│   ├── report/          # PDF/Word report generation
│   └── monitoring/      # Uptime, SSL/TLS, and keyword checks
├── docker/              # Docker & Compose configurations
├── scripts/             # Automation and maintenance scripts
├── requirements.txt
└── manage.py

🧠 Core Features
🔍 Scan & Detection
Automatic detection of CMS type, versions, and plugin vulnerabilities (via NVD, WPScan, Wordfence).
Periodic Celery tasks for continuous scanning.

⚖️ Compliance Engine (YAML-based)
Rulesets for regional frameworks:
🇪🇺 EU: IT-Grundschutz, NIS2, GDPR
🇺🇸 USA: NIST SP 800-53, CCPA, ADA
Computes a compliance score (0–100%) per site and region.

🤖 AI Assistant
Explains vulnerabilities in natural language.
Suggests automated or manual fixes.
Generates executive summaries for reports.

🧾 Reports & Audit
PDF and Word report generator.
Compliance Matrix + Technical Findings.
White-label options for agencies.

📈 Monitoring & Alerts
SSL/TLS certificate monitoring.
Keyword and uptime checks (Prometheus Blackbox).
Slack, Telegram, or Email alerts.

📅 Roadmap
Version	Description
v0.1.0	Django API base + /health endpoint
v0.2.0	Docker + Celery + Redis integration
v0.3.0	JWT Auth + Workspace models
v0.4.0	Compliance Engine (EU rules)
v0.5.0	AI Assistant + PDF/Word reports
v1.0.0	Multi-CMS support + Global launch

👥 Author
Andrei Sili
📧 contact: [andrei.sili.dev@gmail.com]

💼 GitHub: andrei-sili

🧾 License
MIT License — see LICENSE
