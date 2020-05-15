# Observatorio 👁‍🗨🎲 

## Description 📜

This project is the implementation of my Undergraduate thesis.
It consists in populate one Data Warehouse, using the ETL (Extract, Transform, and Load) process.

## Technologies 🧰
  - Python 🐍
  - Pandas 🐼
  - MySql 🎲

## Open Data 🔓

We are using a huge CSV open data file provided by the Brazil Government. The data is from an education program called FUNDEB. It contains all values received by all Brazilian cities in every month since 2007.

## How to use 🧭

- **Linux**

  - Make sure you have at least [Python](https://www.python.org/) 3.7.4 installed in your machine

 - then clone this repository with one of these:
    - Git: 
     ```shell
        git clone https://github.com/KyroSx/observatorio_etl.git
      ```
    - Hub:
     ```shell
        hub clone KyroSx/observatorio_etl
      ```
  - Install the dependencies by running:
       ```shell
       $ pip install -r requirements.txt
       ```
       this can be done inside a [virtual env](https://virtualenv.pypa.io/en/stable/)

  - Create your own database config file, by running:
     ```shell
     $ touch database/database_env.py
     $ echo 'DB_USER = "your-database-user"\nDB_PASSWORD = "your-database-password"\nDB_NAME = "your-database-name"\nHOST = "127.0.0.1"' >> database/database_env.py
     ```
  
    - It needs to look like this: 
        ```python
        DB_USER = "your-database-user"
        DB_PASSWORD = "your-database-password"
        DB_NAME = "your-database-name"
        HOST = "127.0.0.1"
        ```

## Database structure
![database-model](https://user-images.githubusercontent.com/33635656/81863161-238bd180-9541-11ea-914e-d3c9384ccd9b.png)
