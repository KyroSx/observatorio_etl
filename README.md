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

Make sure you have [Python](https://www.python.org/) installed in your machine, then clone this repository with `git clone link`.

You need to install the dependencies by running ` pip install -r requirements.txt`, this can be done inside a [virtual env](https://virtualenv.pypa.io/en/stable/).

Inside the `database` folder, create a file called `database_env.py` which contains all your database information. It needs to look like this:
    ```
    DB_USER = "your-database-user"
    DB_PASSWORD = "your-database-password"
    DB_NAME = "your-database-name"
    ```

## Database structure
![database-model](https://user-images.githubusercontent.com/33635656/81863161-238bd180-9541-11ea-914e-d3c9384ccd9b.png)
