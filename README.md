My Choice My Prof
=================
Searching for professors from given fields is easier than you thought. Reverse search enables to find professors from the field, say you need a list of all the professors working in nanomaterials. What's next? Keep reading.

The repository holds the source for the crawler to generate data for mcmp ``` Professor Reverse Search ```.

**Prerequisites :**
Install `Scrapy`. Follow [Scrapy Install](http://doc.scrapy.org/en/latest/intro/install.html).
```
  pip install scrapy
```

Get started :
============


* Clone the repo as :

```
  git clone https://github.com/metakgp/mcmp.git
```

* Checkout to the source code branch :

```sh
git checkout source
cd reverse
```

* To run the crawler with spider-config as in `rsspider.py` and store data as json, use :
```
  scrapy crawl reverse -o prof_details.json -t json
```

Contributing to mcmp
===============
Please use [issues](https://github.com/metakgp/mcmp/issues) page to report any bugs or file feature requests.


Developing mcmp
--------------------
We love PR's. 
Before we begin developing, a short note: 

* `scrapy` will scrape items written in `reverse/reverse/items.py`

* find scraping logic (= rules for scraping from html dump) in `reverse/reverse/spiders/rsspiders.py`

* `departments.json` contains list of all departments.
* `prof_details.json` uses `professor.json` to populate itself. (Itself, huh? Oh yes, yes you do it. Code is just a manifestation of your brilliant mind. :D )


Search Box on webpage
------------------------

`makelists.py` processes `prof_details.json` and creates `finallist.json` which
is then used to create the fuzzy search, search box [here](http://metakgp.github.io/mcmp/).
If you want to modify the webpage for mcmp, checkout the `gh-pages` branch.  [More about github pages](https://pages.github.com/).


Populating metakgp wiki with the data from json files
-------------------------------------------

`prof_details.json` can also be used to automatically create profile pages of
each Professor on metakgp. `reverse/profjson_to_wikitext.py` creates a text file
from the json which can be subsequentially passed to
[Pywikibot](https://www.mediawiki.org/wiki/Manual:Pywikibot) to populate the
wiki pages.
