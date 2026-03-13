# Virtual Server Monitoring Dashboard

## Project Overview

This project demonstrates a **Data Engineering and Data Visualization workflow** for monitoring virtual server performance.
The system ingests server log data, processes it using Python, stores it in a database, and visualizes performance metrics using dashboards.

The project includes:

* Data ingestion and preprocessing
* Database storage using SQLite
* Visualization using Power BI
* Interactive monitoring dashboard using Streamlit

This project was developed as part of a **Data Engineering Case Study Assessment**.

---

## Project Architecture

Server Log Data → Data Ingestion (Python) → SQLite Database → Processed Dataset → Dashboards

Tools used in the pipeline:

* Python for data ingestion and preprocessing
* SQLite for data storage
* Power BI for analytical dashboard
* Streamlit for interactive monitoring dashboard

---

## Project Structure

```
Virtual-Server-Monitoring-Dashboard
│
├── app.py
├── Data_Ingestion.ipynb
├── processed_server_logs.csv
├── server_logs.db
├── Virtual_Server_Monitoring_Dashboard.pbix
├── README.md
├── requirements.txt
│
└── data
    └── sample_data_ingestion.csv
```

---

## Technologies Used

Python Libraries

* pandas
* streamlit
* plotly
* matplotlib
* sqlite3

Tools

* Python
* SQLite
* Power BI
* Streamlit
* GitHub

---

## Data Ingestion

The ingestion script performs the following tasks:

1. Reads server log data from CSV files
2. Cleans and processes the dataset
3. Stores the data into a SQLite database
4. Generates a processed dataset for visualization

The ingestion pipeline is implemented in:

```
Data_Ingestion.ipynb
```

---

## Database

Server performance data is stored in an SQLite database:

```
server_logs.db
```

This database contains structured records of server performance metrics including:

* CPU Utilization
* Memory Usage
* Network Traffic
* Server Location
* Operating System Type
* Instance Size

---

## Streamlit Monitoring Dashboard

An interactive monitoring dashboard was built using **Streamlit**.

The dashboard includes:

* KPI metrics for system performance
* Network traffic by server location
* CPU utilization by instance size
* Memory usage by operating system
* CPU vs Memory utilization analysis
* Interactive server filtering
* Dataset preview

Run the dashboard locally using:

```
streamlit run app.py
```

---

## Power BI Dashboard

A business intelligence dashboard was also created using **Microsoft Power BI**.

File:

```
Virtual_Server_Monitoring_Dashboard.pbix
```

This dashboard provides deeper analytical insights into server performance.

---

## Deployment

The Streamlit dashboard is deployed and accessible via:

Deployment Link:
https://virtual-server-monitoring-dashboard-eeec9dndlqmd6gyqbz9nx7.streamlit.app/

---

## How to Run the Project

Clone the repository:

```
git clone https://github.com/Anjali-12-coder/virtual-server-monitoring-dashboard.git
```

Install required dependencies:

```
pip install -r requirements.txt
```

Run the Streamlit application:

```
streamlit run app.py
```

---

## Key Insights

The dashboard helps monitor and analyze:

* Server CPU utilization trends
* Memory consumption patterns
* Network traffic distribution
* Performance comparison across server locations
* Resource usage across instance types

---

## Author

Anjali M N
Data Engineer Internship Assessment Project


