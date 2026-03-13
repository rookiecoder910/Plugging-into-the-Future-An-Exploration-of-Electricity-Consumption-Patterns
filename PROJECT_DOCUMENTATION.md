# Plugging into the Future: An Exploration of Electricity Consumption Patterns

---

**Department of Computer Science / Information Technology**
**Academic Year: 2024–2025**

---

## Table of Contents

1. [Abstract](#1-abstract)
2. [Introduction](#2-introduction)
3. [Problem Statement](#3-problem-statement)
4. [Objectives of the Project](#4-objectives-of-the-project)
5. [Tools and Technologies Used](#5-tools-and-technologies-used)
6. [Data Collection](#6-data-collection)
7. [Database Setup and Table Analysis using MySQL Workbench](#7-database-setup-and-table-analysis-using-mysql-workbench)
8. [Data Cleaning and Preprocessing](#8-data-cleaning-and-preprocessing)
9. [Data Visualization using Tableau](#9-data-visualization-using-tableau)
10. [Dashboard Creation and Explanation](#10-dashboard-creation-and-explanation)
11. [Results and Insights from the Visualization](#11-results-and-insights-from-the-visualization)
12. [Conclusion](#12-conclusion)
13. [Future Scope](#13-future-scope)
14. [References](#14-references)

---

## 1. Abstract

The rapid growth of energy demand in a developing nation such as India necessitates a thorough understanding of electricity consumption patterns across diverse geographical and demographic regions. This project, titled *Plugging into the Future: An Exploration of Electricity Consumption Patterns*, aims to investigate and visualize daily electricity usage across 33 Indian states and union territories spanning the years 2019 and 2020. The dataset, comprising 16,599 records, was stored and queried using MySQL Workbench, and subsequently connected to Tableau Desktop for the purpose of interactive visual analysis.

The study employs a range of Tableau chart types — including geographic maps, bar charts, line charts, pie charts, heat maps, and parameter-driven Top N / Bottom N filters — to uncover regional disparities, seasonal trends, monthly fluctuations, and the unprecedented impact of the COVID-19 national lockdown on electricity consumption. The resulting dashboards and story presentations are further embedded in a Flask-based web application for accessible public viewing.

Key findings reveal that the Western Region consistently records the highest electricity consumption, while the North Eastern Region records the lowest. Most significantly, a sharp decline of approximately 86.8% in electricity consumption was observed during April 2020, corresponding to the period of India's first nationwide lockdown. The project demonstrates how structured data analysis and interactive visualization tools can provide actionable insights for energy planners, policymakers, and researchers.

---

## 2. Introduction

Electricity is the backbone of modern civilisation. Industries, households, transportation systems, healthcare facilities, and digital infrastructure all depend on a reliable and sufficient supply of electrical power. In a country as vast and diverse as India — with a population exceeding 1.4 billion people and economic activity spanning agriculture, manufacturing, and services — understanding regional electricity consumption is not merely an academic exercise but a strategic necessity.

India's power grid is managed across five major regional grids: the Northern Region (NR), Western Region (WR), Southern Region (SR), Eastern Region (ER), and North Eastern Region (NER). Each of these regions encompasses multiple states, union territories, and metropolitan centres, each with its own consumption profile driven by factors such as industrialisation levels, population density, seasonal climate patterns, and urbanisation.

The years 2019 and 2020 present a particularly compelling comparative window. The year 2019 represents a baseline of relatively stable consumption under normal economic and social conditions. The year 2020, however, was marked by the COVID-19 pandemic, which triggered a nationwide lockdown beginning in late March 2020, causing a dramatic and near-instantaneous disruption of industrial activity, commercial operations, and human mobility. This lockdown had a measurable impact on electricity demand — an impact that this project aims to document, quantify, and visualise.

This project utilises a data-driven approach, integrating database management through MySQL with advanced visual analytics through Tableau. The workflow spans data collection, storage, querying, cleaning, and visualisation, culminating in an interactive web application built with Flask that embeds the Tableau dashboards for broader accessibility.

---

## 3. Problem Statement

India's electricity distribution network is one of the largest and most complex in the world. Despite extensive data collected by the Central Electricity Authority (CEA), granular insights about state-level and region-level consumption trends remain underutilised. The absence of accessible, interactive analytical tools makes it difficult for administrators, researchers, and the general public to understand how and where electricity is consumed, what seasonal patterns exist, and how extraordinary events — such as a nationwide pandemic lockdown — alter consumption behaviour.

The specific problems this project addresses are:

1. **Lack of interactive visualisation** of multi-state, multi-year electricity consumption data that is accessible to non-technical stakeholders.
2. **Insufficient comparative analysis** between states, regions, and time periods (monthly, quarterly, yearly).
3. **Limited documentation** of the COVID-19 lockdown's quantitative impact on electricity demand across India's diverse regions.
4. **Absence of a unified platform** that integrates database-stored consumption records with dynamic dashboards and a web interface.

By addressing these problems, this project provides a comprehensive analytical framework that transforms raw tabular data into meaningful, interactive visual narratives.

---

## 4. Objectives of the Project

The objectives of this project are as follows:

1. **To collect and organise** daily electricity consumption data for 33 Indian states and union territories across the years 2019 and 2020.
2. **To store the dataset** in a structured relational database (MySQL) and perform exploratory SQL queries to validate and understand the data.
3. **To connect the MySQL database** to Tableau Desktop for seamless data extraction and live or extract-based visualisation.
4. **To create individual worksheets** in Tableau covering geographic maps, bar charts, line charts, pie charts, heat maps, and parameter-controlled rankings.
5. **To assemble three interactive dashboards** combining multiple worksheets, filters, and parameters to enable multidimensional analysis.
6. **To develop a Tableau Story** that narrates the key findings in a structured, step-by-step presentation suitable for stakeholders.
7. **To quantify and highlight** the impact of the COVID-19 lockdown on electricity consumption, with specific reference to the drop observed in April 2020.
8. **To deploy the dashboards** on Tableau Public and embed them in a Flask web application for accessible online viewing.
9. **To derive actionable insights** regarding regional disparities, seasonal trends, and consumption patterns that can inform energy policy and planning.

---

## 5. Tools and Technologies Used

### 5.1 MySQL and MySQL Workbench

MySQL is an open-source relational database management system (RDBMS) widely used for storing, managing, and querying structured data. MySQL Workbench is the official graphical user interface (GUI) for MySQL, providing tools for database design, SQL development, and server administration. In this project, MySQL Workbench was used to:

- Create the database schema and the consumption table.
- Import the CSV dataset into the database.
- Execute SQL queries for data exploration and validation.
- Establish a live connection to Tableau Desktop via the MySQL connector.

**Version used:** MySQL 8.0 / MySQL Workbench 8.0

### 5.2 Tableau Desktop

Tableau Desktop is a leading business intelligence and data visualisation platform that allows users to connect to various data sources and build interactive charts and dashboards. Key features used in this project include:

- Connecting to MySQL as a live data source.
- Building worksheets with various chart types (maps, bars, lines, pie charts, heat maps).
- Creating calculated fields (e.g., lockdown period classification).
- Implementing parameter controls for dynamic Top N / Bottom N filtering.
- Assembling multiple worksheets into dashboards with interactive filters.
- Creating a Tableau Story for a narrative presentation.

**Version used:** Tableau Desktop 2023.x

### 5.3 Tableau Public

Tableau Public is the free, cloud-based hosting service for Tableau visualisations. After completing the dashboards and story in Tableau Desktop, the workbook was published to Tableau Public, making it accessible via shareable embed URLs. These URLs were then used in the Flask web application.

### 5.4 Flask (Python Web Framework)

Flask is a lightweight WSGI web application framework for Python. It was used in this project to build a web interface that:

- Embeds the Tableau Public dashboards and story via iframes.
- Provides a login-protected interface for authorised users.
- Serves an aesthetically styled HTML/CSS/JavaScript front end.
- Displays metadata, tags, and descriptions for each visualisation.

**Version used:** Flask 3.x, Python 3.10+

### 5.5 Dataset

The primary dataset is a CSV file (`Consumption.csv`) containing daily electricity consumption records for 33 Indian states and union territories. The data was sourced from publicly available records maintained by the Central Electricity Authority (CEA), Government of India.

### 5.6 Supporting Libraries and Technologies

| Technology | Purpose |
|---|---|
| Python 3.10+ | Backend scripting and Flask application |
| HTML5 / CSS3 | Front-end templates and styling |
| JavaScript (ES6) | UI interactivity (scroll effects, iframe loading) |
| Google Fonts (Inter) | Typography for the web application |
| Git / GitHub | Version control and repository hosting |

---

## 6. Data Collection

### 6.1 Dataset Description

The dataset used in this project is a CSV file named `Consumption.csv`, containing daily electricity consumption records for all major states and union territories of India for the period **January 2019 to December 2020**. The data was originally sourced from official energy reports published by the Central Electricity Authority (CEA) of India.

**Total Records:** 16,599 rows (excluding the header row)
**File Format:** Comma-Separated Values (CSV)

### 6.2 Dataset Fields

The dataset contains the following six columns:

| Column Name | Data Type | Description |
|---|---|---|
| `States` | VARCHAR | Name of the Indian state or union territory (e.g., Maharashtra, Delhi, Punjab) |
| `Regions` | VARCHAR | The power region the state belongs to: NR (Northern), WR (Western), SR (Southern), ER (Eastern), NER (North Eastern) |
| `latitude` | DECIMAL | Geographic latitude coordinate of the state's approximate centroid |
| `longitude` | DECIMAL | Geographic longitude coordinate of the state's approximate centroid |
| `Dates` | DATE | The specific date of the consumption record (format: DD-MM-YYYY) |
| `Usage` | DECIMAL | Electricity consumed on that date, expressed in Million Units (MU) |

### 6.3 States and Regions Covered

The dataset covers **33 states and union territories** distributed across **5 regional grids**:

| Region Code | Region Name | States Included |
|---|---|---|
| NR | Northern Region | Punjab, Haryana, Rajasthan, Delhi, Uttar Pradesh, Uttarakhand, Himachal Pradesh, J&K, Chandigarh |
| WR | Western Region | Chhattisgarh, Gujarat, Madhya Pradesh, Maharashtra, Goa, DNH |
| SR | Southern Region | Andhra Pradesh, Telangana, Karnataka, Kerala, Tamil Nadu, Pondicherry |
| ER | Eastern Region | Bihar, Jharkhand, Odisha, West Bengal, Sikkim |
| NER | North Eastern Region | Arunachal Pradesh, Assam, Manipur, Meghalaya, Mizoram, Nagaland, Tripura |

### 6.4 Sample Data

The following is a representative sample of the dataset:

| States | Regions | latitude | longitude | Dates | Usage |
|---|---|---|---|---|---|
| Punjab | NR | 31.52 | 75.98 | 02-01-2019 | 119.9 |
| Maharashtra | WR | 19.25 | 73.16 | 02-01-2019 | 428.6 |
| Tamil Nadu | SR | 12.92 | 79.15 | 02-01-2019 | 268.3 |
| West Bengal | ER | 22.58 | 88.33 | 02-01-2019 | 108.2 |
| Assam | NER | 26.75 | 94.22 | 02-01-2019 | 21.7 |

---

## 7. Database Setup and Table Analysis using MySQL Workbench

### 7.1 Creating the Database

The dataset was imported into a MySQL database to enable structured querying and seamless integration with Tableau. The following steps were performed in MySQL Workbench:

**Step 1: Create the Database**
```sql
CREATE DATABASE electricity_db;
USE electricity_db;
```

**Step 2: Create the Table**
```sql
CREATE TABLE consumption (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    States      VARCHAR(100),
    Regions     VARCHAR(10),
    latitude    DECIMAL(12, 8),
    longitude   DECIMAL(12, 8),
    Dates       DATE,
    Usage       DECIMAL(10, 2)
);
```

**Step 3: Import Data from CSV**

The CSV file was imported using the MySQL Workbench Table Data Import Wizard:
- Navigate to the `consumption` table → Right-click → **Table Data Import Wizard**.
- Select `Consumption.csv` as the source file.
- Map each CSV column to the corresponding table column.
- Execute the import. All 16,599 records were successfully loaded.

### 7.2 SQL Queries for Data Exploration

After importing the data, several SQL queries were executed to explore and validate the dataset:

**Total number of records:**
```sql
SELECT COUNT(*) AS total_records FROM consumption;
-- Result: 16599
```

**List all distinct states:**
```sql
SELECT DISTINCT States FROM consumption ORDER BY States;
```

**Total consumption by region:**
```sql
SELECT Regions, SUM(Usage) AS total_usage
FROM consumption
GROUP BY Regions
ORDER BY total_usage DESC;
```

**Monthly average consumption for 2020:**
```sql
SELECT MONTH(Dates) AS month, AVG(Usage) AS avg_usage
FROM consumption
WHERE YEAR(Dates) = 2020
GROUP BY MONTH(Dates)
ORDER BY month;
```

**Consumption during lockdown period (April–May 2020):**
```sql
SELECT States, SUM(Usage) AS lockdown_usage
FROM consumption
WHERE Dates BETWEEN '2020-04-01' AND '2020-05-31'
GROUP BY States
ORDER BY lockdown_usage DESC;
```

**Top 5 highest consuming states overall:**
```sql
SELECT States, SUM(Usage) AS total_usage
FROM consumption
GROUP BY States
ORDER BY total_usage DESC
LIMIT 5;
```

### 7.3 Connecting MySQL to Tableau

Once the database was populated and validated, the following steps were performed to connect MySQL to Tableau Desktop:

1. Open Tableau Desktop → **Connect** → **To a Server** → **MySQL**.
2. Enter the server address (localhost), port (3306), database name (`electricity_db`), username, and password.
3. Select the `consumption` table and drag it to the canvas.
4. Verify the data preview to confirm all columns and data types are correctly recognised.
5. Set the date column (`Dates`) to the **Date** data type and `Usage` to **Number (decimal)**.

The connection screenshot confirms the successful linkage between MySQL Workbench and Tableau Desktop, enabling live querying of the database from within the Tableau workbook.

---

## 8. Data Cleaning and Preprocessing

### 8.1 Overview

Before building visualisations, the dataset was examined for quality issues and prepared for analysis. Although the dataset was relatively clean, several preprocessing steps were performed to ensure accuracy and usability.

### 8.2 Handling Missing Values

A review of the imported table revealed no significant missing values across the core columns (`States`, `Regions`, `Dates`, `Usage`). Rows with null or empty `Usage` values (if any) were excluded from aggregate calculations using SQL `WHERE Usage IS NOT NULL` conditions and Tableau's built-in null handling.

### 8.3 Data Type Correction

In MySQL Workbench, the `Dates` field was stored as a `DATE` type after conversion from the original DD-MM-YYYY string format used in the CSV. In Tableau, the `Dates` field was further configured to support hierarchical date drill-downs (Year → Quarter → Month → Day).

### 8.4 Derived Fields and Calculated Columns

Several calculated fields were created in Tableau to support the analysis:

**Lockdown Period Classification:**
```
IF [Dates] < #2020-03-25# THEN "Before Lockdown"
ELSEIF [Dates] <= #2020-06-01# THEN "During Lockdown"
ELSE "After Lockdown"
END
```
This field was used to segment consumption data into three distinct phases relative to India's first national lockdown.

**Year Extraction:**
```
YEAR([Dates])
```
Used to filter and compare data between 2019 and 2020.

**Month-Year Label:**
```
DATENAME('month', [Dates]) + " " + STR(YEAR([Dates]))
```
Used for labelling monthly consumption trends on line charts.

### 8.5 Outlier Review

A visual inspection of the consumption data revealed that the significant drop in April 2020 is not an outlier in the traditional statistical sense but rather a genuine, event-driven anomaly caused by the COVID-19 lockdown. This data point was retained as it forms a critical component of the analysis.

### 8.6 Geographic Coordinate Validation

The `latitude` and `longitude` columns were validated to ensure each state's coordinates fall within the geographic boundaries of India. These coordinates were used to plot filled maps and symbol maps in Tableau.

---

## 9. Data Visualization using Tableau

### 9.1 Overview

Tableau Desktop was used to create fifteen individual worksheets, each presenting a distinct analytical perspective on the electricity consumption data. These worksheets were subsequently assembled into three dashboards and one story.

### 9.2 Worksheet Descriptions

#### 9.2.1 State-wise Consumption Map — 2019

A **filled map (choropleth)** displaying total electricity consumption per state for the year 2019. States are shaded according to a colour gradient, with darker shades representing higher consumption. Maharashtra, Uttar Pradesh, and Gujarat emerge as the top consumers.

#### 9.2.2 State-wise Consumption Map — 2020

An analogous filled map for the year 2020. The overall pattern is similar to 2019, but consumption levels are noticeably lower during the lockdown months, particularly for industrial states.

#### 9.2.3 Usage by Year (Bar Chart)

A grouped **vertical bar chart** comparing total annual electricity consumption for 2019 versus 2020, broken down by region. This chart clearly illustrates the year-over-year change caused by the pandemic.

#### 9.2.4 Total Consumption by Region (Pie Chart)

A **pie chart** showing the proportional share of total electricity consumption contributed by each of the five regions (NR, WR, SR, ER, NER). The Western Region holds the largest share, followed by the Southern and Northern Regions.

#### 9.2.5 2019 Month-wise Consumption (Line Chart)

A **line chart** showing the monthly trend in total electricity consumption across all states for 2019. The chart reveals seasonal peaks during summer months (May–June) and winter months (December–January) driven by air conditioning and heating demands respectively.

#### 9.2.6 2020 Month-wise Consumption (Line Chart)

A corresponding line chart for 2020. The chart shows a sharp dip starting in March 2020, with the lowest point in April 2020, followed by a gradual recovery from May onwards as lockdown restrictions were progressively eased.

#### 9.2.7 2019 State Consumption (Horizontal Bar Chart)

A **horizontal bar chart** ranking all 33 states by their total electricity consumption in 2019. Maharashtra, Uttar Pradesh, Gujarat, Tamil Nadu, and Rajasthan consistently rank among the highest consumers.

#### 9.2.8 2020 State Consumption (Horizontal Bar Chart)

An equivalent ranking chart for 2020, enabling direct comparison of state-level consumption shifts between the two years.

#### 9.2.9 Top N States (Dynamic Bar Chart with Parameter)

A **parameter-driven bar chart** allowing the user to dynamically select the top N states (e.g., Top 5, Top 10) by electricity consumption. The parameter control is exposed as a slider or input box on the dashboard, providing interactivity.

#### 9.2.10 Bottom N States (Dynamic Bar Chart with Parameter)

A complementary chart displaying the bottom N states by consumption, enabling analysis of the lowest-consuming states and union territories such as Chandigarh, Sikkim, and Mizoram.

#### 9.2.11 Regional Usage Comparison (Grouped Bar Chart)

A grouped bar chart comparing monthly electricity consumption across all five regions side-by-side. This visualisation is particularly useful for identifying seasonal divergences between regions.

#### 9.2.12 Usage Before and During Lockdown

A **dual-axis or side-by-side bar chart** comparing electricity consumption across states before and during the COVID-19 lockdown period. The lockdown period is classified using the calculated field described in Section 8.4.

#### 9.2.13 Month-wise Top Consumption (Heat Map)

A **heat map (text table with colour encoding)** showing monthly consumption totals for each state, enabling a comprehensive overview of all states across all months of both years simultaneously.

#### 9.2.14 Region-wise State Breakdown

A **tree map or bar-in-bar chart** presenting the contribution of individual states within each region, supporting analysis of intra-regional disparities.

#### 9.2.15 Quarter-wise Usage

A **bar chart** or **line chart** aggregated at the quarterly level, showing consumption trends across four quarters for both 2019 and 2020. Quarter 2 of 2020 (April–June) shows the most dramatic decline.

#### 9.2.16 Metro City Comparison

A focused visualisation comparing electricity consumption in major metropolitan states (Delhi, Maharashtra, Tamil Nadu, West Bengal, Karnataka) before and during the lockdown.

---

## 10. Dashboard Creation and Explanation

### 10.1 Overview

Three interactive dashboards were constructed in Tableau Desktop by combining the individual worksheets described in Section 9. Each dashboard serves a distinct analytical purpose and includes interactive filters and parameters to enable user-driven exploration.

### 10.2 Dashboard 1: Overview and Geographic Analysis

**Purpose:** Provide a high-level geographic overview of electricity consumption patterns across India.

**Components:**
- State-wise Consumption Map for 2019 (filled map)
- State-wise Consumption Map for 2020 (filled map)
- Usage by Year bar chart (region-wise comparison)
- Total Region Consumption pie chart

**Interactive Elements:**
- Year filter to toggle between 2019 and 2020 data.
- State filter to highlight or isolate specific states.
- Region filter for drilling down into regional data.

**Key Insight:** The maps visually confirm that states in the Western and Southern regions dominate in absolute consumption terms, while the North Eastern states remain the lowest consumers.

**Dashboard Screenshot:** `dashboard/dash1.png`

### 10.3 Dashboard 2: Comparative and Ranking Analysis

**Purpose:** Enable comparative analysis of state rankings and monthly/regional consumption patterns.

**Components:**
- Top N States dynamic bar chart (with parameter control)
- Bottom N States dynamic bar chart (with parameter control)
- Monthly consumption comparison for 2019 and 2020
- Regional usage comparison grouped bar chart

**Interactive Elements:**
- Top N / Bottom N parameter slider (range: 1–33)
- Year filter for 2019 vs. 2020 toggle
- Region filter for narrowing comparisons

**Key Insight:** Maharashtra, Uttar Pradesh, Gujarat, Tamil Nadu, and Andhra Pradesh consistently rank in the top five consuming states across both years. Conversely, Mizoram, Sikkim, and Arunachal Pradesh consistently rank at the bottom.

**Dashboard Screenshot:** `dashboard/dash2.png`

### 10.4 Dashboard 3: Deep Dive and Lockdown Analysis

**Purpose:** Provide a detailed investigation of the COVID-19 lockdown's impact on electricity consumption.

**Components:**
- Usage Before and During Lockdown chart
- Month-wise Top Consumption heat map
- Region-wise State Breakdown
- Quarter-wise Usage chart
- Metro City Comparison chart

**Interactive Elements:**
- Lockdown period filter (Before / During / After)
- State selection filter
- Region filter
- Date range slider

**Key Insight:** April 2020 recorded the most dramatic drop in electricity consumption, with some industrial states recording declines exceeding 40% relative to April 2019. The North Eastern region showed relatively smaller declines, as it had lower baseline industrial activity.

**Dashboard Screenshot:** `dashboard/dash3.png`

### 10.5 Tableau Story

In addition to the three dashboards, a **Tableau Story** was created to provide a guided, narrative walkthrough of the key findings. The story is structured as a sequence of story points, each focusing on a specific insight:

1. **Introduction:** Overview of the dataset and project scope.
2. **Regional Overview:** Geographic map of 2019 consumption.
3. **Year-over-Year Change:** Comparison of 2019 vs. 2020 totals.
4. **Lockdown Impact:** The dramatic consumption drop in April 2020.
5. **State Rankings:** Top and bottom consuming states.
6. **Conclusion:** Summary of key insights and implications.

The story is particularly suited for presenting findings to non-technical audiences such as policymakers and energy planners.

---

## 11. Results and Insights from the Visualization

### 11.1 Regional Consumption Patterns

The analysis reveals significant regional disparities in electricity consumption across India:

- **Western Region (WR)** is the highest consuming region, driven by large industrial states such as Maharashtra, Gujarat, and Madhya Pradesh. The Western Region contributes approximately 30–35% of total national consumption.
- **Southern Region (SR)** is the second highest, with Tamil Nadu, Andhra Pradesh, and Karnataka being the primary contributors.
- **Northern Region (NR)** ranks third, led by Uttar Pradesh and Rajasthan.
- **Eastern Region (ER)** ranks fourth, with West Bengal contributing the most within this region.
- **North Eastern Region (NER)** records the lowest consumption, consistent with its lower level of industrialisation and smaller population base.

### 11.2 State-level Rankings

Among all 33 states and union territories:

- **Top 5 Consuming States (2019):** Maharashtra, Uttar Pradesh, Gujarat, Tamil Nadu, Rajasthan
- **Bottom 5 Consuming States (2019):** Chandigarh, Sikkim, Mizoram, Nagaland, Tripura

### 11.3 Seasonal and Monthly Trends

- Consumption follows a seasonal pattern, with peaks in **May–June** (summer months, driven by air conditioning and cooling demand) and **November–December** (winter months in northern India).
- The lowest consumption in 2019 occurred during the monsoon months of **July–August**, when industrial activity partially slows and temperatures moderate.

### 11.4 COVID-19 Lockdown Impact

This is the most significant finding of the study:

- **April 2020** recorded the lowest electricity consumption across all regions. This directly corresponds to India's first nationwide lockdown, which began on 25 March 2020.
- The Tableau Story highlights a decline of approximately **86.8%** in peak daily consumption recorded during the strictest phase of the lockdown (late March – April 2020) compared to comparable pre-lockdown days, representing an extraordinary disruption to normal energy demand patterns. This figure reflects the peak single-day drop observed in the data story and is prominently featured in the project's narrative visualisation.
- States with heavy industrial and commercial activity (Maharashtra, Gujarat) showed the sharpest declines during the lockdown.
- States with primarily agricultural economies and smaller industrial bases showed comparatively smaller percentage declines.
- By **June–July 2020**, consumption began recovering as lockdown restrictions were progressively relaxed.

### 11.5 Quarter-wise Analysis

- **Q1 2019 vs Q1 2020:** Broadly similar consumption levels, with marginal differences.
- **Q2 2019 vs Q2 2020:** The most dramatic divergence. Q2 2020 consumption was significantly lower due to the lockdown coinciding with April–June.
- **Q3 and Q4 2020:** Gradual recovery, with Q4 2020 approaching Q4 2019 levels.

### 11.6 Metro City Analysis

Metropolitan states (Delhi, Maharashtra, Tamil Nadu, West Bengal, Karnataka) showed the greatest absolute decline in consumption during the lockdown, as these regions host the largest concentrations of commercial establishments, offices, malls, restaurants, and industrial units that were mandatorily closed.

---

## 12. Conclusion

This project successfully demonstrates the application of data management and visual analytics tools — specifically MySQL and Tableau — to derive meaningful insights from large-scale electricity consumption data. By analysing daily usage records for 33 Indian states and union territories across two calendar years (2019 and 2020), the project achieves all stated objectives and produces a comprehensive analytical product.

The key conclusions drawn from this study are:

1. **Regional disparities are substantial and persistent.** The Western Region dominates in total electricity consumption, while the North Eastern Region remains far behind due to structural differences in economic activity and population.

2. **Seasonal patterns are clearly discernible.** Summer and winter peaks are consistent with climate-driven demand for cooling and heating respectively.

3. **The COVID-19 lockdown had a profound and measurable impact** on electricity consumption, with April 2020 recording the single largest month-over-month decline in the dataset. This finding underscores the deep interconnection between economic activity, human mobility, and energy demand.

4. **Interactive visualisation significantly enhances data comprehension.** The use of Tableau dashboards with dynamic filters, parameter controls, and geographic maps allows stakeholders to explore the data from multiple perspectives without requiring technical expertise.

5. **Web-based embedding extends the reach** of analytical products. The integration of Tableau Public dashboards into a Flask web application makes the analysis accessible to a broader audience beyond desktop tools.

The project thus establishes a replicable workflow for energy data analysis that can be extended to other datasets, geographies, and time periods.

---

## 13. Future Scope

The current project lays a solid foundation for further research and development. Several avenues for future enhancement are proposed:

1. **Extending the Dataset:** Incorporate electricity consumption data beyond 2020 (2021, 2022, 2023) to study the post-pandemic recovery trajectory and emerging trends in renewable energy adoption.

2. **Predictive Modelling:** Apply machine learning algorithms (e.g., ARIMA, LSTM, Prophet) to forecast future electricity demand based on historical patterns, seasonal trends, and economic indicators.

3. **Integration of External Variables:** Incorporate meteorological data (temperature, humidity), GDP data, and population data to build multivariate models explaining the drivers of regional consumption differences.

4. **Renewable Energy Analysis:** Extend the analysis to include data on solar, wind, and hydro power generation to study the relationship between renewable supply and demand patterns.

5. **Real-time Data Pipeline:** Replace the static CSV dataset with a real-time data pipeline that continuously ingests live electricity consumption data from official APIs, enabling up-to-date dashboards.

6. **Mobile-Responsive Interface:** Enhance the Flask web application with a fully mobile-responsive design and dedicated Tableau Mobile API integration for seamless use on smartphones and tablets.

7. **Granular Geographic Analysis:** Extend the analysis from state level to district level as more granular data becomes available, enabling targeted analysis of consumption hotspots.

8. **User Authentication and Role Management:** Expand the Flask application's authentication system to support multiple user roles (admin, analyst, viewer) with role-specific access to different dashboards and reports.

9. **Automated Reporting:** Implement automated report generation (PDF/email) that summarises key metrics and anomalies on a scheduled basis for distribution to stakeholders.

10. **Cross-country Comparison:** Extend the framework to compare India's consumption patterns with those of other rapidly developing nations (China, Brazil, Indonesia), providing a global perspective on energy demand growth.

---

## 14. References

1. Central Electricity Authority (CEA), Government of India. *Daily Report on Generation of Power Stations*. Ministry of Power. Available at: [https://cea.nic.in](https://cea.nic.in)

2. Tableau Software. *Tableau Desktop User Guide*. Salesforce, 2023. Available at: [https://help.tableau.com/current/pro/desktop/en-us/getstarted_overview.htm](https://help.tableau.com/current/pro/desktop/en-us/getstarted_overview.htm)

3. MySQL Documentation. *MySQL 8.0 Reference Manual*. Oracle Corporation, 2023. Available at: [https://dev.mysql.com/doc/refman/8.0/en/](https://dev.mysql.com/doc/refman/8.0/en/)

4. Flask Documentation. *Welcome to Flask*. Pallets Projects, 2023. Available at: [https://flask.palletsprojects.com/en/3.0.x/](https://flask.palletsprojects.com/en/3.0.x/)

5. Ministry of Power, Government of India. *Annual Report 2020–21*. Government of India, 2021. Available at: [https://powermin.gov.in/sites/default/files/Annual_Report_2020-21_English.pdf](https://powermin.gov.in/sites/default/files/Annual_Report_2020-21_English.pdf)

6. International Energy Agency (IEA). *India 2020: Energy Policy Review*. IEA, 2020. Available at: [https://www.iea.org/reports/india-2020](https://www.iea.org/reports/india-2020)

7. World Bank Group. *Access to Electricity (% of Population) – India*. World Bank Open Data, 2023. Available at: [https://data.worldbank.org/indicator/EG.ELC.ACCS.ZS?locations=IN](https://data.worldbank.org/indicator/EG.ELC.ACCS.ZS?locations=IN)

8. Tableau Public. *Plugging into the Future — Electricity Consumption Dashboards*. Available at: [https://public.tableau.com/views/PluggingIntoTheFuture/](https://public.tableau.com/views/PluggingIntoTheFuture/)

9. Python Software Foundation. *Python Language Reference, Version 3.10*. Available at: [https://docs.python.org/3.10/](https://docs.python.org/3.10/)

10. Few, S. *Show Me the Numbers: Designing Tables and Graphs to Enlighten*. 2nd Edition. Analytics Press, 2012.

11. Wexler, S., Shaffer, J., & Cotgreave, A. *The Big Book of Dashboards: Visualizing Your Data Using Real-World Business Scenarios*. Wiley, 2017.

12. National Disaster Management Authority (NDMA), Government of India. *COVID-19 Lockdown Guidelines*. 2020. Available at: [https://ndma.gov.in](https://ndma.gov.in)

---

*This documentation was prepared as part of an academic project submission. All data used in this project is sourced from publicly available government and institutional databases. The analysis and interpretations presented herein are intended for educational purposes.*

---

**End of Document**
