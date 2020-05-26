from datetime import datetime


ti = (3, 30, 2019, 9, 25)
print('{:%m/%d/%Y %H:%M}'.format(datetime(ti[2], ti[3], ti[4], ti[0], ti[1])))
