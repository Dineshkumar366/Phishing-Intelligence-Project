# Project Structure

``` text
Phishing_Intelligence_Project/
│
├── dataset/
│   ├── phishing_dataset_clean.csv
│   ├── ml_dataset_final.csv
│   └── live_url_dataset.csv
│
├── models/
│   ├── production_url_model.pkl
│   ├── phishing_model.pkl
│   ├── phishslayer_model.pkl
│   └── ...
│
├── scripts/
│   ├── admin_portal.py
│   ├── url_scanner.py
│   ├── final_feature_pipeline.py
│   ├── content_analysis.py
│   ├── redirect_analysis.py
│   ├── threat_intelligence.py
│   ├── scan_history_logger.py
│   ├── risk_scoring.py
│   └── ...
│
├── logs/
│   └── scan_history.csv
│
├── launcher.py
├── phishing_icon.ico
├── requirements.txt
└── README.md
```

## Important Files

-   `README.md` --- project documentation
-   `requirements.txt` --- Python dependencies
-   `launcher.py` --- starts the admin dashboard
-   `scripts/admin_portal.py` --- Flask admin portal
-   `scripts/url_scanner.py` --- complete URL scanning pipeline
-   `models/production_url_model.pkl` --- production ML model
-   `logs/scan_history.csv` --- scan history
