#!/usr/bin/python3

import os
import datetime

path = '/var/atlassian/application-data/jira/export/'

filesInDir = os.listdir(path)

filesWithPath = []
rmFiles = []
files = {}

for _ in filesInDir:
    
    if _.endswith('.zip'):
        tmp = os.path.join(path, _)
        if os.path.isfile(tmp):
            filesWithPath.append(tmp)

for _ in filesWithPath:
    tmpTimeStamp = os.path.getmtime(_)
    tmpDateHRdbl = datetime.datetime.fromtimestamp(tmpTimeStamp).date()
    files[_] = tmpDateHRdbl
    

dateToday = datetime.date.today()
dateWeekAgo = dateToday - datetime.timedelta(days=7)

for key, value in files.items():
    if value <= dateWeekAgo:
        rmFiles.append(key)


for _ in rmFiles:
    os.remove(_)