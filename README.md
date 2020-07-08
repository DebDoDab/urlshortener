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
  ```
  cd urlshortener
  ```
* Make virtual environment
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```
* Install requirements
  ```
  pip3 install -r requirements.txt
  ```
* Install mongodb and run mongodb server
  ```
  sudo apt install mongodb
  sudo systemctl start mongodb
  ``` 
* Create and open file `.env` with any text editor and add HOST_NAME, MONGO_HOST, MONGO_PORT, MONGO_DATABASE_NAME values
  ```
    echo "HOST_NAME=http://localhost:8000/
    MONGO_HOST=mongodb://localhost
    MONGO_PORT=27017
    MONGO_DATABASE_NAME=url_shortener" > .env
  ```
* Test your local server with a shell script
  ```
  sh start.sh
  ```


## Plans
* Try to get host name not from `.env` file
* Write a better UI
* Make a dockerfile
* Add REDIS instead of Mongo
  * Make CRON to automatically delete old links
  * But keep them in MongoDB