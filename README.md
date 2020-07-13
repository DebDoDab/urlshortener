# URLShortener

#### Project to make your long urls shorter


## Usage

#### Type any link (with http:// or https://) in input field and press 'Shortify' button
#### Copy your shortified link and enjoy  


## Installation and running


* Download this project
  ```
  git clone https://github.com/DebDoDab/urlshortener.git
  ``` 
* Go into that directory
  ```
  cd urlshortener
  ```
* Run docker-container
  * in development
  ```
  docker-compose build
  docker-compose up
  ```
  * or in production
  ```
  docker-compose -f prod.yml build
  docker-compose -f prod.yml up
  ``` 



## Plans
* Write a better UI
* Add REDIS instead of Mongo _(Optional)_
  * Make CRON to automatically delete old links
  * But keep them in MongoDB