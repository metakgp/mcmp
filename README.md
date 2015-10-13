My Choice My Prof
=================

The repository holds the source for the crawler to generate data for mcmp ``` Professor Reverse Search ```.

Prerequisites :
Install Scrapy. Follow [Scrapy Install](http://doc.scrapy.org/en/latest/intro/install.html).
```
  pip install scrapy
```

To get started :

* Clone the repo as :

```
  git clone https://github.com/metakgp/mcmp.git
```

* Checkout to the source code branch :

```sh
git checkout source
cd reverse
```

* To run the crawler with spider-config as in rsspider.py and store data as json, use :
```
  scrapy crawl reverse -o prof_details.json -t json
```

How to change mcmp?
-------------------

The item which `scrapy` will scrape for are written in
`reverse/reverse/items.py` and the specific scraping logic is written in
`reverse/reverse/spiders/rsspiders.py`

The current `prof_details.json` file has been developed over multiple stages,
first `departments.json` was scrapped, then `professor.json` was scrapped and
the current code scrapes for `prof_details.json`. If you need to modify the
json for earlier stages please uncomment the corresponding code, comment out
the current code and proceede.

Fuzzy Search, Search Box
------------------------

`makelists.py` processes `prof_details.json` and creates `finallist.json` which
is then used to create the fuzzy search, search box on `http://metakgp.github.io/mcmp/`.
If you want to modify the web part checkout the `gh-pages` branch.


Populating the wiki with json
-----------------------------

`prof_details.json` can also be used to automatically create pages of
Professor on metakgp. `reverse/profjson_to_wikitext.py` creates a text file
from the json which can then be passes to
[Pywikibot](https://www.mediawiki.org/wiki/Manual:Pywikibot) to populate the
wiki.
