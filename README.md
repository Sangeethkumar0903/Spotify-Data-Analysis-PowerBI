# Spotify Data Analysis with Power BI and Python

## Project Overview

This project analyzes Spotify streaming data using Power BI for visualization and Python for data processing. The dataset was sourced from Kaggle and cleaned to enhance usability. The project includes customized visualizations using Vega-Lite JSON, such as an energy percentage circle and a heatmap.

## Features

- Data cleaning and processing using Python.
- Power BI dashboard with interactive charts and filters.
- Custom Vega-Lite visualizations for enhanced insights.
- Heatmap analysis for track popularity trends.
- Analysis of track energy levels using circular progress visualization.

## Dataset and Processing

1. The original dataset was downloaded from Kaggle and saved as `spotify_raw.csv`.
2. A Python script (`data_cleaning.py`) was used to clean the data and add album cover URLs.
3. The cleaned dataset (`spotify_cleaned.csv`) was used for Power BI visualizations.
4. To fetch album cover URLs dynamically, you need to get a **Client ID** and **Client Secret** from the Spotify Developer Dashboard:
   - Visit [Spotify Developer](https://developer.spotify.com/)
   - Log in and create a new application
   - Copy the **Client ID** and **Client Secret**
   - Use them in your Python script to make API requests.

## Power BI Dashboard

The Power BI dashboard contains multiple visualizations to explore trends in the dataset:

- Line chart showing track count over time.
- Stacked bar chart displaying total streams per track.
- Custom energy percentage circle visualization using Vega-Lite JSON.
- Heatmap visualization to analyze streaming patterns by month and day of the week.

## Project Structure

```
Spotify-Data-Analysis-PowerBI
│── dataset/
│   ├── spotify_raw.csv      # Original dataset
│   ├── spotify_cleaned.csv  # Cleaned dataset
│   ├── data_cleaning.py     # Python script for data processing
│── assets/
│   ├── dashboard.png        # Power BI dashboard preview
│   ├── design.png           # Canva-designed visuals
│── visualizations/
│   ├── energy_circle.json   # Vega-Lite visualization for energy percentage
│   ├── heatmap.json         # Vega-Lite heatmap visualization
│── Spotify_Analysis.pbix    # Power BI file
│── README.md                # Documentation
```

## Technologies Used

- Power BI for data visualization and reporting.
- Python (Pandas, Requests) for data processing.
- Vega-Lite JSON for advanced custom visualizations.
- Canva for designing additional UI elements.

## How to Use This Project

1. Clone this repository:
   ```
   git clone https://github.com/YOUR_USERNAME/Spotify-Data-Analysis-PowerBI.git
   ```
2. If you want to clean the data again, run the Python script:
   ```
   cd dataset
   python data_cleaning.py
   ```
3. Open `Spotify_Analysis.pbix` in Power BI.
4. Interact with the dashboard to explore the insights.

## Custom Vega-Lite Visualizations

### Energy Percentage Circle (`energy_circle.json`)

This visualization represents the energy percentage of a track using a circular progress bar with gradient colors. It dynamically updates based on the dataset values.

### Heatmap (`heatmap.json`)

The heatmap helps identify track popularity trends by visualizing streaming activity across different months and days of the week. It uses a color gradient to represent the density of streams.







