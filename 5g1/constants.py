# -*- coding: utf-8 -*-

API_URL = "https://rent.591.com.tw/home/search/rsList"

CONDITIONS = {
'is_new_list': '1',
'type': '1',

'kind': '1,2',#1:整層住家,2: 獨立套房

'searchtype': '1',

'region': '1',#1:台北市,3: 新北市 

'section':'3,4,5,7,10,12',
#1:中正
#2:大同
#3:中山
#4:松山
#5:大安
#6:萬華
#7:信義
#8:士林
#9:北投
#10:內湖
#11:南港
#12:文山

'rentprice': '12500,25000',

#'patternMore': '2',#幾房

'area':'12,40',#坪

#'shape':'1,2,3',
#1:公寓,2:電梯大樓,3:透天厝,4:別墅

#'option': 'cold',
#cold:冷氣,hotwater:熱水器,naturalgas:天然瓦斯,

#'other':'lift',
#lifr:電梯,balcony_1:陽台,cook:開火,pet:寵物,tragoods:近捷運,cartplace:車位,lease:短租

'hasimg': '1',

'not_cover': '1',#非頂加

#'role':'1',#屋主

#'firstRow':'30',
#firstRow=210&totalRows=403

'order':'posttime', #money,area,posttime
'orderType':'desc', #asc

#keywords
}

WEB_URL_FORMAT_STR = "https://rent.591.com.tw/rent-detail-{}.html"

SETTINGS_PATH = "./example-settings.ini"
