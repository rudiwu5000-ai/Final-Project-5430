
# **README.md**

# WSB Sentiment Trading Simulation – Repository Guide

This repository contains all scripts and datasets used to scrape WallStreetBets posts, extract stock price data, apply sentiment labels, and run a trading simulation based on positive sentiment signals.

## Files and What their purpose

### 1. subreddit_scrape.py

Scrapes recent WallStreetBets posts from Reddit.
Outputs:
Stock wallstreetbets.csv → raw November WSB posts.

### 2. stockprice_scrape.py

Downloads stock price data for November for all tickers mentioned in WSB posts.
Outputs:
november_stock_data.csv

### 3. Stock wallstreetbets.csv

Raw scraped WSB posts from November.
Used for:

* Cleaning timestamps
* Matching stock mentions
* Applying sentiment model

### 4. `Stock_wallstreetbets_clean_timestamp.csv

A cleaned version of the raw WSB scrape, with:

* Standardized timestamps
* Extracted tickers
* Removed duplicates/irrelevant posts

Used as input for the sentiment labeling step.

### 5. wsb3000.py

Scrapes the top 3000 historical WSB posts.
This dataset is manually labeled by you to train a sentiment framework.

Outputs (not included):
wsb3000.csv (raw scraped top 3000 posts)

### 6.wsb3000_with_sentiment.csv

Manually labeled sentiment dataset.
Reference used for supervised sentiment modeling.

### 7. sentiment_apply.py

Applies the sentiment framework (from the labeled 3000 posts) to the cleaned November dataset.

Outputs:
Stock_wallstreetbets_with_ml_sentiment.csv

The November WSB posts now contain ML-based sentiment predictions.

### 8. project.Rmd

The main simulation and analysis file.

This script:

* Loads the ML-labeled WSB data
* Matches sentiment timestamps to stock price data
* Simulates $100 long positions for positive sentiment
* Applies 7% stop-loss and 25% take-profit rules
* Computes PnL, win rate, return distribution, exit reasons
* Generates visualizations
* Produces summary statistics and outputs for interpretation

This is the final step in the full workflow.

## Workflow Summary and pipeline

1. Scrape posts → subreddit_scrape.py → Stock wallstreetbets.csv
2. Clean timestamps & extract tickers** → output: cleaned CSV
3. Scrape stock prices** → stockprice_scrape.py → november_stock_data.csv
4. Create sentiment model

   Scrape top posts → wsb3000.py
   Manually label → wsb3000_with_sentiment.csv
5. Apply sentiment to November posts → sentiment_apply.py
6. Run trading simulation & analysis → project.Rmd

## All requirements of packages can be found in the code files

