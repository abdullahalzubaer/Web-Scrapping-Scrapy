# Web-Scrapping-Scrapy

Readme:


Step 1: Please download the folder "corey" from this repo

Step 2: Please create a virtual env using 

```
conda env create --file scrapy_env.yml
```

Step 3: Navigate to the folder "corey\corey\spiders" (while in the env create on step 2)

Step 4: Execute the code on terminal using the following command

```
scrapy crawl corey -o crawled.json
```

This will create a json file with the crawled information from the given webpage (it will crawl all the pages till the last one)


Reference
---
[1] https://docs.scrapy.org/en/latest/intro/tutorial.html

[2] https://www.youtube.com/watch?v=ALizgnSFTwQ
