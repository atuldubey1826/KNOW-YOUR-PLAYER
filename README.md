# KNOW-YOUR-PLAYER

Welcome to the **KNOW YOUR PLAYER**! This is a Python-based learning project designed to aggregate, clean, and search through football (soccer) player data. By leveraging powerful data science libraries and fuzzy string matching, this project allows users to explore player stats and find players even if they misspell their names.

The primary goal of this project was to master data manipulation workflows and solve real-world data duplication and search challenges.

---

## 🚀 Features

* **Data Aggregation & Cleaning:** Compiles raw football datasets into a structured, queryable format.
* **Advanced Search (Fuzzy Matching):** Uses `rapidfuzz` to handle typos, alternative spellings, or partial names (e.g., searching "Kylian Mbape" will still find "Kylian Mbappé").
* **Stat Insights:** Fast filtering and vectorized data operations to pull up player profiles, career stats, and comparisons instantly.

---

## 🛠️ Tech Stack & Learning Objectives

This project was built to gain hands-on experience with the following core Python libraries:

* **NumPy:** Used for high-performance numerical operations and handling underlying multi-dimensional arrays for fast statistical calculations.
* **Pandas:** The backbone of the project. Used for data ingestion, cleaning, handling missing values, filtering DataFrames, and structuring the encyclopedia.
* **RapidFuzz:** Integrated to implement string matching algorithms (like Levenshtein distance) to create a forgiving, user-friendly search interface.
