# ecommerce-ebay-scraper-selenium-python

A robust Python script using Selenium to scrape product data from eBay, including product name, price, delivery charge, and location, designed for e-commerce analysis. The script automates searches, handles pagination, and exports results to Excel and CSV formats, making it ideal for price monitoring, competitor analysis, or market research. It complements other data projects, such as news scraping, to provide holistic market insights.

## Overview

This project automates the extraction of product listings from eBay, a leading e-commerce platform, using Selenium for browser automation. It searches for user-defined queries (e.g., "used iPhone"), scrapes multiple pages, and collects key data points: product name, price, delivery charge, and location. The script employs anti-detection techniques (user-agent spoofing, random delays) to minimize CAPTCHA interruptions and exports clean, structured data to Excel and CSV files using Pandas.

Developed as part of a broader data scraping initiative, this tool complements news scraping projects (e.g., The Daily Star) to combine e-commerce trends with economic insights. It’s suitable for businesses, researchers, or developers needing reliable e-commerce data for market analysis or automation workflows.

## Features

- **Automated Scraping**: Searches eBay for any query and scrapes product listings across multiple pages.
- **Data Points**: Extracts product name, price, delivery charge, and location.
- **Anti-Detection**: Uses user-agent spoofing and random delays to simulate human behavior, reducing CAPTCHA risks.
- **Data Export**: Saves results to Excel (`ebay_product_list.xlsx`) and CSV (`ebay_product_list.csv`) for easy analysis.
- **Pagination Handling**: Navigates through eBay’s pagination to collect comprehensive data.
- **Error Handling**: Robust exception handling ensures reliable scraping even with dynamic web elements.
- **Customizable**: Easily modified for other eBay queries, categories, or e-commerce platforms.

## Technologies

- **Python**: Core programming language for scripting.
- **Selenium**: Browser automation for navigating and scraping eBay.
- **Pandas**: Data manipulation and export to Excel/CSV.
- **ChromeDriver**: WebDriver for controlling Chrome browser (configurable for Firefox/GeckoDriver).
- **webdriver-manager**: Automatically manages ChromeDriver installation.
- **Optional**: `selenium-stealth` for enhanced anti-detection (not included but supported).
