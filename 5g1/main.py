#!/usr/bin/env python3

import configparser
import json
import time
import codecs
import requests

from logger import logger
from constants import API_URL, CONDITIONS, WEB_URL_FORMAT_STR, SETTINGS_PATH

cache = set()

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

total = 1
firstRow = 0

def get_houses():
    global total, firstRow, CONDITIONS
    #logger.info('requests 591 API...')
    response = requests.get(API_URL, params=CONDITIONS, headers=headers)
    response_json = json.loads(response.text)

    try:
        data = response_json['data']
    except KeyError:
        logger.error("Cannnot get data from response_json")
    except:
        raise
    else:
        total = response_json['records']
        houses = data.get('data', [])
        logger.info('firstRow:'+str(firstRow)+'/'+total+'\n')
        firstRow += len(houses)
        CONDITIONS['firstRow'] = firstRow

        for house in houses:
            yield house


def log_house_info(house):
    logger.info(
        u"名稱：{}-{}-{}".format(
            house['region_name'],
            house['section_name'],
            house['fulladdress'],
        )
    )
    logger.info(u"網址：{}".format(WEB_URL_FORMAT_STR.format(house['post_id'])))
    logger.info(u"租金：{} {}".format(house['price'], house['unit']))
    logger.info(u"坪數：{} 坪".format(house['area']))
    logger.info(u"格局：{}".format(house['layout']))
    logger.info(u"{}".format(house['floorInfo']))
    logger.info(u"更新時間：{}".format(time.ctime(house['refreshtime'])))
    logger.info("\n")


def search_houses():
    houses = get_houses()
    for house in houses:
        if house['post_id'] in cache:
            continue

        log_house_info(house)
        cache.update([house['post_id']])


def main():
    global total, firstRow
    config = configparser.ConfigParser()
    config.read(SETTINGS_PATH)

    while firstRow < int(total):
        print '*'
        search_houses()
        time.sleep(1)
        #time.sleep(int(config['default']['parse_interval_in_seconds']))
    print 'done'

if __name__ == "__main__":
    main()
