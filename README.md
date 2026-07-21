# 🤖 AI-Powered SIEM Alert Investigation Chatbot

🚀 An AI-driven cybersecurity project that automates SIEM alert investigation, threat analysis, and SOC incident response using **Wazuh, Splunk, Flask, and Llama 3**.

---

# 📌 Project Overview

This project demonstrates the development of an AI-powered Security Operations Center (SOC) assistant that integrates SIEM platforms with Artificial Intelligence to simplify security alert investigation.

The system collects security alerts from **Wazuh and Splunk**, analyzes events using an AI investigation engine, performs threat intelligence enrichment, maps attacks to MITRE ATT&CK techniques, and provides investigation recommendations through an interactive dashboard.

The objective is to reduce manual SOC analyst workload by automating repetitive alert analysis and improving incident response efficiency.

---

# ⚙️ Key Features

- Centralized security alert monitoring
- Integration with Wazuh SIEM
- Splunk log analysis and event investigation
- AI-powered alert investigation using Llama 3
- Automated threat analysis and explanation
- Brute-force attack detection
- Suspicious login activity detection
- MITRE ATT&CK technique mapping
- Threat intelligence enrichment
- Risk scoring and incident classification
- SOC investigation dashboard
- CSV and PDF investigation reports

---

# 🧠 Core Modules

### SIEM Engine
- Collects and processes security alerts
- Handles event correlation
- Performs alert classification

### AI Investigation Engine
- Analyzes security events using Llama 3
- Generates investigation summaries
- Provides analyst recommendations

### Incident Response Engine
- Categorizes security incidents
- Generates response actions
- Supports SOC workflows

### Threat Intelligence Module
- Performs indicator analysis
- Enriches alerts with threat information

### Risk Engine
- Calculates alert severity
- Prioritizes security events

---

# 🛠️ Technologies Used

### Security Platforms
- Wazuh SIEM
- Splunk Enterprise
- MITRE ATT&CK Framework

### Backend
- Python
- Flask
- REST APIs

### Artificial Intelligence
- Llama 3
- AI Investigation Engine
- Natural Language Processing

### Database & Reporting
- SQLite
- Pandas
- ReportLab

### Frontend
- HTML
- CSS
- JavaScript

### Environment
- Linux
- GitHub Codespaces

---

# 📸 Project Screenshots

(Add dashboard, Wazuh alerts, Splunk dashboards, and chatbot screenshots here)

---

# ⚙️ Implementation

The system workflow:

1. Security logs are collected from endpoints and SIEM sources.
2. Wazuh and Splunk generate security alerts.
3. Alerts are processed by the SIEM engine.
4. Threat intelligence enriches security indicators.
5. AI engine investigates the alert using Llama 3.
6. Risk engine calculates severity.
7. Dashboard displays investigation results and recommendations.

---

# 🔄 Project Execution Workflow

```
Security Events
       |
       ↓
 Wazuh / Splunk SIEM
       |
       ↓
 Alert Processing Engine
       |
       ↓
 AI Investigation Engine
       |
       ↓
 Threat Intelligence
       |
       ↓
 Risk Assessment
       |
       ↓
 SOC Dashboard & Reports
```

---

# 🚨 Attack Simulation Scenarios

The system was tested using:

### Brute Force Attack Detection

- Multiple failed login attempts
- Suspicious authentication activity
- Source IP tracking
- MITRE ATT&CK mapping (T1110 - Brute Force)

### Unauthorized Access Detection

- Abnormal login attempts
- Privilege misuse detection
- Security event analysis

These activities generate alerts that are collected, analyzed, and investigated by the AI-powered SOC assistant.

---

# 📊 Results

✅ Real-time security alert monitoring  
✅ Automated alert investigation  
✅ AI-generated threat analysis  
✅ Detection of suspicious activities  
✅ SOC dashboard visualization  
✅ Incident response recommendations  
✅ Security report generation  

---

# ⚙️ Setup & Execution
For complete setup instructions and commands, refer to:

📂 [setup/commands.txt](setup/commands.txt)


---

# 🧪 Testing

Test AI Investigation:

```bash
python test_ai.py
```

Test SIEM Engine:

```bash
python test_siem.py
```

Test Splunk Integration:

```bash
python test_splunk.py
```

Test Wazuh Integration:

```bash
python test_wazuh.py
```

---

# 🔐 Security Considerations

- API keys and credentials are stored separately using environment variables.
- Private certificates and sensitive files are excluded using `.gitignore`.
- Secure API communication is used for SIEM integrations.

---

# 🚀 Future Enhancements

- Automated incident response actions
- SOAR platform integration
- Real-time threat hunting
- Advanced machine learning anomaly detection
- Cloud SIEM integration
- Automated ticket creation

---

# 💡 Conclusion

This project simulates a real-world Security Operations Center (SOC) environment by combining SIEM platforms with Artificial Intelligence.

It provides practical experience in:
- Security monitoring
- Alert investigation
- Incident response
- Threat intelligence
- SIEM automation
- AI-assisted cybersecurity operations

---

# 👩‍💻 Author

**Gagana Kuruba**

Cyber Security Graduate | SOC Analyst Aspirant

🔗 GitHub:
https://github.com/Kurubagagana

🔗 LinkedIn:

