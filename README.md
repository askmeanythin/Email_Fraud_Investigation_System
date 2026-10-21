# Email Fraud Investigation & Reporting System

Python tool for investigating suspicious emails. It parses the headers,
checks authentication results (SPF/DKIM/DMARC), analyses the sender,
domains and URLs, extracts IOCs, scores the risk and generates an
investigation report.

Run: `pip install -r requirements.txt`, then `python main.py`.
