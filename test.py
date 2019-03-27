#!/usr/bin/env python3

from datetime import datetime

ExpectedDate = "27/3/2019 9:57"
ExpectedDate = datetime.strptime(ExpectedDate, "%d/%m/%Y %H:%M")
print(ExpectedDate)
while(ExpectedDate > datetime.now()):
    print(datetime.now())
    print("wait")
    sleep(1)




