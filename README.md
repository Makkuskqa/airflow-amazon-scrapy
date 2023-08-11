# airflow-amazon-scrapy
I have a key-word (clothes) request for Amazon store and I parse all information from Amazon include: [asin	Title	MainImage	Rating	NumberOfReviews	Price	AvailableSizes	AvailableColors	BulletPoints	SellerRank] for every product and page behind.
This information I parse, scheduled every day + 10 minutes, with airflow and host + save result on GCP vm-instance and bucket storage.

![image](https://github.com/Makkuskqa/airflow-amazon-scrapy/assets/105742207/6985bd1c-ef32-44a5-ac42-28f50a7b4806)

# Project description as image schema. Second variant
![image](https://github.com/Makkuskqa/airflow-amazon-scrapy/assets/105742207/bd7434e5-a91c-4fde-b6c1-285b458e4f92)

I have 2 full versions of this project:
- First variant. Is full on vm-instance gcp [postgres db - airflow init - external ip for UI + scrapy app]
- Second variant.   Partly on local Ubuntu[airflow, scrapy app], partly on vm-instance [bucker storage + host postgres db]

On this project I used different combinations of web-scrapping tools and different combinations, when set airflow

Tools for scraping:
  - scrapy Api. In result on Amazon worked the best.
  - selenium
  - bs4, requests
    
Combinations airflow:
- sqlite & postgres
- docker images, WIN python3-pip, Ubuntu python3-pip
