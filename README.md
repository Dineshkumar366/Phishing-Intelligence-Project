# Phishing Intelligence & URL Threat Detection System

## Overview

The **Phishing Intelligence & URL Threat Detection System** is a
cybersecurity project that analyzes a submitted URL using multiple
security and threat-intelligence layers.

The system combines machine-learning-based URL classification with DNS,
domain, SSL, VirusTotal, redirect, and website-content analysis. It
produces a risk score and a final security decision through an admin
dashboard.

## Key Features

-   Machine Learning URL classification
-   Phishing and legitimate probability
-   DNS resolution analysis
-   WHOIS/domain-age analysis
-   SSL certificate validation
-   VirusTotal threat intelligence
-   Redirect-chain analysis
-   Website content analysis
-   Risk scoring from 0--100
-   Final decision generation
-   Scan history logging
-   Web-based admin dashboard
-   Windows one-click launcher EXE

## System Workflow

``` text
User enters URL
       |
       v
URL Normalization
       |
       +----> ML URL Analysis
       |
       +----> DNS Analysis
       |
       +----> Domain / WHOIS Analysis
       |
       +----> SSL Analysis
       |
       +----> VirusTotal Analysis
       |
       +----> Redirect Analysis
       |
       +----> Website Content Analysis
       |
       v
Risk Assessment Engine
       |
       v
Risk Score + Final Decision
       |
       v
Scan History + Admin Dashboard
```

## Technology Stack

-   Python
-   Flask
-   Pandas
-   Scikit-learn
-   Random Forest
-   Requests
-   Python-WHOIS
-   Joblib
-   PyInstaller
-   HTML / CSS
-   VirusTotal API

## Main Project Components

  -----------------------------------------------------------------------------
  Component                                 Purpose
  ----------------------------------------- -----------------------------------
  `scripts/admin_portal.py`                 Admin dashboard and URL scanner
                                            interface

  `scripts/url_scanner.py`                  Main multi-layer URL scanning
                                            engine

  `scripts/final_feature_pipeline.py`       URL feature extraction pipeline

  `scripts/content_analysis.py`             Website content analysis

  `scripts/redirect_analysis.py`            Redirect-chain analysis

  `scripts/threat_intelligence.py`          VirusTotal integration

  `scripts/scan_history_logger.py`          Scan history logging

  `scripts/risk_scoring.py`                 Risk scoring logic

  `models/production_url_model.pkl`         Production ML model

  `logs/scan_history.csv`                   Scan history

  `launcher.py`                             Starts the admin portal and opens
                                            the dashboard

  `dist/PhishingIntelligenceLauncher.exe`   Windows launcher
  -----------------------------------------------------------------------------

## Risk Levels

-   **0--39:** LOW RISK
-   **40--69:** MEDIUM RISK
-   **70--100:** HIGH RISK

A high-confidence ML phishing prediction is given priority in the final
decision.

## Admin Portal

The local admin portal runs at:

`http://127.0.0.1:5050`

Demo credentials:

-   Username: `admin`
-   Password: `admin123`

> These credentials are intended only for a local academic/demo
> environment and should be replaced with secure authentication for
> production use.

## Running the Project

### Option 1 --- Windows EXE

Run:

`dist\PhishingIntelligenceLauncher.exe`

The launcher starts the Flask admin portal and opens the dashboard
automatically.

### Option 2 --- Python

From the project root:

``` bash
python scripts/admin_portal.py
```

Then open:

`http://127.0.0.1:5050`

## Machine Learning

The production model was trained using the same URL feature extraction
logic used during prediction. This helps avoid train/serve feature
mismatch.

The model uses 17 URL-level features including:

-   URL length
-   Domain length
-   IP-based domain detection
-   TLD length
-   Number of subdomains
-   Obfuscation indicators
-   Letter and digit ratios
-   Special-character ratios
-   HTTPS usage

The project uses a Random Forest classifier for URL classification.

## Scan History

Every completed scan is recorded in:

`logs/scan_history.csv`

The history contains information such as:

-   Timestamp
-   URL
-   ML prediction
-   Phishing probability
-   DNS status
-   Domain status
-   Domain age
-   SSL status
-   VirusTotal results
-   Redirect count
-   Website content indicators
-   Risk score
-   Final decision

## Security Notes

-   VirusTotal API keys must be stored securely as environment
    variables.
-   Do not commit API keys or passwords to Git.
-   The system is intended for defensive cybersecurity analysis and
    academic demonstration.
-   Website content analysis is based on fetched HTML and may not fully
    capture JavaScript-rendered content.
-   A legitimate website can occasionally receive a suspicious ML score;
    results should be interpreted using multiple security layers.

## Future Enhancements

-   Browser extension
-   Dynamic JavaScript rendering
-   Additional threat-intelligence APIs
-   Better authentication and role-based access
-   Automated email alerts
-   Cloud deployment
-   Real-time monitoring
-   Improved model validation using independently sourced data

## Author

**Dineshkumar T**

B.Sc. Computer Science\
Cyber Security Training --- Pumo Technovation
