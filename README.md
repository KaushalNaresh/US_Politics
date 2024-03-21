# US Politics: A Data-Driven Analysis of Sentiment, Demography and Media in US poltics

This repository contains the STA220 course project "Navigating the Currents: Demographics, Sentiment, and Media Influence in American Political Waters", which examines the intricate relationships between public sentiment on national events, demographic factors, and media influence within the context of the United States political scene from 2016 to 2020.

## Project Structure

- `Data`: This folder contains all CSV files with the data obtained via web scraping and API calls.
- `Code`: This directory includes all scripts used for scraping data, executing API calls, performing sentiment analysis, and conducting LDA.
- `Dash_App_1`: Contains the code for the Dash application that demonstrates state-wise correlations between sentiment scores on various national topics and demographic features.
- `Dash_App_2`: Holds the code for the Dash application that explores how media framing can potentially shift public opinion.

## Data

The `Data` folder comprises several CSV files that form the backbone of our analysis:

- `demographics.csv`: Demographic data acquired from the U.S. Census Bureau.
- `sentiment_scores.csv`: Sentiment scores derived from Reddit comments on key national topics.
- `media_bias.csv`: Data reflecting media bias and sentiment on current events.
- `isreal_hamas_war_article_data.csv`: News article data for the Israel-Hamas war from allsides.com.
- `ukraine_war_article_data`: News article data for the Ukraine-Russia war from allsides.com.
- `allsides_bias_data`: Data reflecting news sources and their bias rating from allsides.com.

## Analysis

The research involved a multi-layered approach to data analysis:

- Sentiment analysis of Reddit comments to gauge public opinion on significant national issues.
- Regression analysis to explore the correlation between public sentiment and demographic factors.
- LDA to identify common themes within media coverage and to understand media bias.

## Dash Applications

Two interactive Dash applications provide visual insights:

- **Dash App 1**: An interactive tool that visualizes the correlation between demographic features and public sentiment on a state-by-state basis.
- **Dash App 2**: An application that highlights the role of media in shaping public opinion on pivotal topics.

## Usage

To explore the data and analysis, navigate to the respective directories. For a deep dive into the visualizations, run the Dash applications locally by executing the following command in each app's directory:

> python app.py

or you can directly access these apps on [Dash_App_1](https://data-and-web-technologies-for-data.onrender.com/) and [Dash_App_2](https://data-and-web-technologies-for-data-1cu1.onrender.com/) 

## Contributions

This project is the culmination of the collaborative efforts of Naresh Kumar Kaushal and Rutuja Abhijit Kale. Contributions to further expand on this research are welcome. Please submit a pull request or open an issue to discuss potential changes or additions.

## Acknowledgments

Special thanks to all the data providers, including the U.S. Census Bureau and allsides.com, for making their data accessible for academic and research purposes.

---

For more information on the project's methodology, findings, and implications, please refer to the comprehensive report included in this repository.



