#!/bin/bash

export PYTHONPATH="/var/www/euromillion:/var/www/euromillion/euro_million:/var/envs/euromillion/lib/python2.7/site-packages:/var/envs/euromillion/bin"
export PATH="/var/envs/euromillion/bin:/usr/lib/lightdm/lightdm:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games"

cd /var/www/euromillion/euro_million/

scrapy crawl euro_numbers

sleep 2m

python /var/www/euromillion/euro_class.py

