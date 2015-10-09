rm prof_details.json
scrapy crawl reverse -o prof_details.json -t json
python3 profjson_to_wikitext.py > ../../pywikibot-core/prof_pages.txt
python pwb.py pagefromfile.py -start:xxxx -end:yyyy -file:prof_pages.txt -notitle -force
