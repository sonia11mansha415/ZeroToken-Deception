# ZeroToken-Deception

An autonomous cyber deception platform designed to detect credential theft and trigger real-time containment playbooks using FastAPI and simulated SOAR workflows.

## 🎯 Architectural Overview
- **Deception Mechanism**: Deploys canary authentication endpoints (`/api/v1/trap`) masquerading as enterprise credential endpoints.
- **Attacker Interaction**: Intercepts requests, collects client metadata, and serves plausible deceptive failures (`Token expired`).
- **Telemetry & Forensics**: Automatically logs forensic indicators (IP, User-Agent, URI parameters) in structured JSON format (`incidents.log`) for SIEM ingestion.
- **Autonomous Containment**: Simulates sub-second host isolation and session revocation via automated security playbooks.

## 📁 Repository Structure