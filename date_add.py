from datetime import datetime, timedelta


d = datetime.strptime(input(), "%Y %m %d")
r = timedelta(int(input()))
delta = d+r
print(f'{delta.year} {delta.month} {delta.day}')
