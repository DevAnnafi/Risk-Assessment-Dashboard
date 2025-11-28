# Risk Assessment Dashboard

A Governance, Risk, and Compliance (GRC) project simulating risk identification, scoring, mitigation, and visualization for a hypothetical organization.

## Features
- Calculates Risk Score (Likelihood × Impact) for 25+ risks
- Shows Residual Risk after mitigation strategies
- Generates a Heatmap for top risks by category
- Mitigation strategies included for each risk

## Tech Stack
- Python
- pandas
- matplotlib
- seaborn

## Project Structure
```
risk-assessment-dashboard/
├── data/
│ └── risks.csv
├── scripts/
│ └── risk_dashboard.py
├── outputs/
│ └── risk_heatmap.png
├── README.md
└── requirements.txt
```

## Usage
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the dashboard: `python scripts/risk_dashboard.py`
4. View the heatmap in `outputs/risk_heatmap.png`

## Results
<img width="2394" height="1594" alt="image" src="https://github.com/user-attachments/assets/7e85b1cd-3905-4c67-897f-a2f416199cec" />
<img width="1102" height="376" alt="image" src="https://github.com/user-attachments/assets/9b1fe817-cfbd-47b2-a90a-4c24ba0cc9a0" />

## Conclusion From Results

This assessment identifies **Data Breach** as the single most critical risk to our organization, with a maximum risk score of 20. This underscores an urgent need for enhacned cybersecurity controls and data protection protocols.

The top 10 risks are dominated by **Cybersecurity** threats (4 out of 10), including Ransomware Attack, Phishing Attack, and Malware infection. This highlights that our digital infrastructure and user awareness are primary attack surfaces requiring immediate investment.

Significant operational and third-party risks also demand attention:
- **Supply Chain Disruption** and **Vendor Failure** pose major operational threats.
- **Reputation Damage** and **Regulatory Fines** (from GDPR/HIPPA non-compliance) represent substantial financial and brand risks.

**Strategic Recommendation:** My risk mitigation strategy must prioritize:
1. **Fortifying Cyber Defenses** against data breaches and ransomware.
2. **Strengthening Third-Party Risk Management** and supply chain resilience.
3. **Ensuring Regulatory Compliance** to avoid severe penalties and reputational harm.

Proactive management of these top-tier risks is essential for organizational stability, financial health, and long-term success.


## Learning Outcomes
- Risk assessment and prioritization
- Data visualization for GRC insights
- Hands-on experience with Python and pandas for risk reporting
