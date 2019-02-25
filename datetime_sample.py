import datetime

tday = datetime.date.today()
tdelta = datetime.timedelta(days=7)
print(tday - tdelta)

bday = datetime.date(2019, 10, 19)
till_bday = bday - tday
print(till_bday.total_seconds())
print(datetime.datetime.utcnow())
