# Cryptocurrency Application
This project is a web application that displays Cryptocurrency data, fetched from an external API. It includes features for sorting and filtering the data based on user input.

# Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

# Project Structure

The structure of the project is as follows:
```
project
├── README.md
├── requirements.txt
├── .gitignore
├── app
│   ├── __init__.py
|   ├── main.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── cryptocurrency.py
│   └── templates
│       └── index.html
```

# Features

- Fetches Cryptocurrency data from the external API: https://api.coincap.io/v2/exchanges
- Displays the Cryptocurrency data on the frontend.
- Allows sorting of the data in ascending/descending order.
- Allows filtering of the data by name.

# Installation

### Steps

# Prerequisites

- Python 3.7 or higher
- Virtual Environment (Anaconda)

1. **Clone the Repository**
   
   * `git clone https://github.com/PBehari/ptc-cryptocurrency-app.git`
   * `cd ptc-cryptocurrency-app`

2. **Create a Virtual Environment**
   
* For Anaconda users: 
  * `conda create --name conda_ptc_cryptocurrency_app python=3.12`
  * `conda activate conda_ptc_cryptocurrency_app`
  * `conda install pip`

3. **Install Dependencies**
   
   * `pip install -r requirements.txt`

### Usage

1. **Running the application**
   
   Open the app in integrated terminal and run the following command:
   * `python main.py`

2. **Access the Frontend**
   
   Open the app in your browser via the provided access link: http://127.0.0.1:5000.
