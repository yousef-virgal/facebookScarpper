from facebook_scraper import get_posts, get_profile
import json
from facebook_scraper import get_group_info
from datetime import date, datetime
import os
from facebook_scraper.fb_types import Credentials
from openpyxl import Workbook
import re
filename = "data.xlsx"

workbook = Workbook()
sheet = workbook.active
columnNames = 'ABCDEFGHI'

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    return obj
get_group_info(1772910512846903,cookies=r'C:\Users\Yousef\OneDrive\Desktop\Ai project training\Puppeteer-FB-Scraping\cookies.txt') 
headers = ('is_Available','Number of Comments','is_FactChecked','Image_URL','Number of Likes','Post_ID','Time','UserName','Post_text')
counter = 0 
for column in columnNames:
    sheet[column+'1'] = headers[counter] 
    counter += 1

rowTracker = 2
column_size = len(headers)
for post in get_posts(group=1772910512846903,pages=150):
    data = [post['available'],post['comments'],post['factcheck'],post['image'],post['likes'],post['post_id'],json_serial(post['time']),post['username'],post['text']]
    columnNumber = 0
    for column in columnNames:
        sheet[column+str(rowTracker)] = json_serial(data[columnNumber])
        columnNumber += 1
    rowTracker += 1
    workbook.save(filename=filename)

print('done')