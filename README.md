
# Laptop Price Tracker

## Project Description

The **Laptop Price Tracker** project aims to monitor daily price fluctuations of 16GB RAM laptops available at Intercomp Malta shops. It accomplishes this by scraping the Intercomp website to collect data such as the laptop name, price, and an image to visualize the laptop. This data is then stored in databases for further analysis.

## Technologies Used

The following technologies and tools were used in the development of this project:

- Python 3.x
- BeautifulSoup for web scraping
- MySQL for data storage
- SQL Server Developer Edition for an alternative data storage solution
- Docker for containerization
- PowerBI for data visualization
- Windows Scheduler for task scheduling


## Data Sources

The project scrapes data from the Intercomp Malta website, extracting information such as the laptop name, price, and image.

## Data Base
 - MySQL
 - SQL Server

## Data Pipeline

The data pipeline consists of the following steps:

1. Web scraping using Python and BeautifulSoup, Pandas, SqlAlchemy ecc to collect data from the Intercomp website.
2. Data storage in MySQL and SQL Server databases using Python scripts.
3. Scheduling daily updates using Docker or Windows Scheduler.

## Dashboard

A simple PowerBI dashboard has been created to visualize the collected data and monitor price fluctuations.

## Contributing

Contributions to this project are welcome.