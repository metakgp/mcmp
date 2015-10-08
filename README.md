mcmp source
======================

The repository holds the source for the crawler to generate data for mcmp ``` Professor Reverse Search ```.

Prerequisites :
-> Install Scrapy. Follow [Scrapy Install](http://doc.scrapy.org/en/latest/intro/install.html).
```
  pip install scrapy
```

To get started :

-> Clone the repo as :
```
  git clone https://github.com/metakgp/mcmp.git
```

-> Checkout to the source code branch :
```sh
  $ git checkout source
  $ cd reverse
```

-> To run the crawler with spider-config as in rsspider.py and store data as json, use :
```
  scrapy crawl reverse -o <corresponding json> -t json
```

-> The python scripts to process the data are in makelists.py. Ensure Pickle is installed.
```
  python makelists.py
```