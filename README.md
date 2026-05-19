# Wellness-Data-Analytics
Fitness Data Analysis
Fitness Business Intelligence & Market Analysis – README
1. Introduction
The fitness industry in urban India is rapidly evolving due to increasing health awareness, urbanization, and rising wellness spending among young professionals and students. Bengaluru, as one of India’s largest metropolitan and IT hubs, has a highly competitive and fragmented fitness ecosystem — gyms, yoga studios, CrossFit centres, Pilates studios, Zumba centres, calisthenics centres, and other specialized wellness businesses.
This project focuses on scraping, cleaning, and analysing Bengaluru fitness centre data to generate business intelligence insights related to market saturation, customer engagement, demographic accessibility, and expansion opportunities. Using Playwright, we collected business listings from Justdial, merged multiple CSV outputs, and prepared the dataset for structured analysis.
The goal is to provide actionable insights for fitness businesses, investors, and analysts.
2. Assumptions
•	Justdial listings are representative of the local fitness market.
•	Ratings and reviews reflect customer sentiment, though they may be biased.
•	Contact details (phone numbers, addresses) are accurate at the time of scraping.
•	Data completeness depends on Justdial’s dynamic loading and anti bot measures.
•	Merged CSV files contain consistent column structures (name, address, phone, rating, reviews, category).
3. Project Objectives
•	Scrape fitness centre data from multiple online sources.
•	Clean and standardize raw business listings.
•	Perform geographic and demographic analysis across Bengaluru.
•	Identify underserved localities and business opportunity gaps.
•	Analyse customer ratings, reviews, and category trends.
•	Generate actionable business recommendations for market entry and expansion.
4. Features
•	Dynamic web scraping using Playwright.
•	Handles JavaScript rendered content.
•	User agent rotation and stealth patch integration to reduce blocking risk.
•	Automatic infinite scrolling and lazy load handling.
•	Data cleaning and standardization pipeline.
•	Geographic and business intelligence analysis.
•	CSV and Excel export support.
•	Data visualization using Matplotlib, Seaborn, and Folium.
5. Dataset Description
Column	Description
name	Fitness centre name
address	Complete business address
locality	Extracted locality name
city	City name
category	Standardized fitness category
rating	Average customer rating
reviews	Total review count
phone	Contact number
medium	Source platform (e.g., Justdial)
6. Requirements
text
playwright>=1.45.0
pandas>=2.2.0
numpy>=1.26.0
matplotlib>=3.8.0
seaborn>=0.13.0
folium>=0.16.0
geopy>=2.4.1
openpyxl==3.1.1
platforms used :Vs code,Jupiter notebook
Scraping URLs include categories such as: Gyms, Fitness Studios, Yoga Centres, Dance/Zumba Studios, CrossFit Gyms, Calisthenic Gyms, Pilates Studios, Karate Dojos, Taekwondo Academies, Kickboxing Studios.
7. Methodology
1.	Data Collection – Scraped business listings from Justdial using Playwright.
2.	Data Cleaning – Removed duplicates, handled missing values, normalized categories, standardized addresses, validated contacts.
3.	Geographic Analysis – Locality density mapping, opportunity gap analysis, inter centre distance calculation.
4.	Demographic Proximity Analysis – Metro accessibility, university proximity, IT park proximity.
5.	Business Intelligence Analysis – Category trends, rating distribution, competitive saturation, market opportunity scoring.
8. Outputs
•	fully_cleaned_justdial.csv → Final cleaned dataset.
•	locality_density_analysis.csv → Geographic density insights.
•	opportunity_gap_analysis.csv → Market gap analysis.
•	category_analysis.csv → Category level analysis.
•	quality_hotspots.csv → Top rated locality analysis.
9. Business Use Cases
•	Lead generation for partnerships and outreach.
•	Competitor density and market saturation analysis.
•	Localized marketing strategy planning.
•	Identification of underserved localities.
•	Expansion planning for new fitness businesses.
•	Customer engagement and sentiment trend analysis.
10. Notes
•	Justdial actively implements anti bot protection mechanisms.
•	User agent rotation and stealth techniques were applied to improve scraping stability.
•	All scraping activities should comply with website terms of service and ethical data collection practices.
11. Future Enhancements
•	Integration with Google Maps API for accurate geospatial analytics.
•	Sentiment analysis on customer reviews.
•	Interactive dashboard development using Power BI or Tableau.
•	Automated proxy rotation for large scale scraping.
•	Real time market monitoring pipelines.
12. Author
Lavanya Ravilla
Bengaluru Fitness Business Intelligence Project

