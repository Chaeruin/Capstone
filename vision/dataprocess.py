import imageread
from datetime import datetime

# Extract information what we want
ident = imageread.texts[0].description

# Decide the result of ident
if ident == '11':
    result = '양성'
elif ident == '1':
    result = '음성'
else:
    result = '검출 오류'

# Take real date time
date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# id, humadity and temp