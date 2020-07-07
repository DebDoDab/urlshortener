# URLshortener

#### Project to make your long urls shorter


## Usage

#### Type any link in imput field and press 'Shortify' button
#### Copy your shortified link and enjoy  


## Installation and running

* Download this project
  * run `git clone https://github.com/DebDoDab/urlshortener.git` 
  * or `git@github.com:DebDoDab/urlshortener.git`
* Go into that directory
  * `cd urlshortener`
* Create and open file `.env` with any text editor and add HOST_NAME value
  * `echo HOST_NAME="https://vadi.tel/" > .env` (instead of `https://vadi.tel/` use your own host name like `localhost:8000/`)
* Make virtual environment
  * `python3 -m venv venv`
  * `source venv/bin/activate`
* Install requirements
  * `pip3 install -r requirements.txt`
* Test your local server with a shell script
  * `sh start.sh`


## Plans
* Write a good UI
* Make code asynchronous 
* Fix installation guide
* Make a dockerfile
* Add REDIS instead of sqlite3
  * Make CRON to automatically delete old links
  * But keep them in DB(Postgres, SQLite3, Mongo)