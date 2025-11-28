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
risk-assessment-dashboard/
├── data/
│ └── risks.csv
├── scripts/
│ └── risk_dashboard.py
├── outputs/
│ └── risk_heatmap.png
├── README.md
└── requirements.txt


## Usage
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the dashboard: `python scripts/risk_dashboard.py`
4. View the heatmap in `outputs/risk_heatmap.png`

## Results
<img width="2394" height="1594" alt="image" src="https://github.com/user-attachments/assets/7e85b1cd-3905-4c67-897f-a2f416199cec" />
<img width="1102" height="376" alt="image" src="https://github.com/user-attachments/assets/9b1fe817-cfbd-47b2-a90a-4c24ba0cc9a0" />

## Learning Outcomes
- Risk assessment and prioritization
- Data visualization for GRC insights
- Hands-on experience with Python and pandas for risk reporting
