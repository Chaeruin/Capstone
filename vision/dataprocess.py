import imageread
from datetime import datetime
from ..rspi import testDHT22 as dht

# Extract information what we want
ident = imageread.texts[0].description

# Decide the result of ident
if ident == '11' or 'II':
    result = '양성'
elif ident == '1' or 'I':
    result = '음성'
else:
    result = '검출 오류'

# Take real date time
date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


# id, humidity and temp

# id = 0                        # auto increament, 자동 생성으로 바꾸기
humidity = dht.humidity         # rsp 바로 연동해서 그 값 가져오기
temp = dht.temperature          # rsp 바로 연동해서 그 값 가져오기