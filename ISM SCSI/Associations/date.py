import datetime
import time

print "BEGIN"

ts = datetime.datetime.now()
end_date = ts + datetime.timedelta(days=7)
ts = time.time()
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
print ts

print timestamp

print end_date
print "==="
print str(end_date)

