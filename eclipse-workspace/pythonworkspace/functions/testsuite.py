import datetime
# import time

def time_fetch(min=0):
  time_now = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
      minutes=min)
  return time_now.strftime("%Y-%m-%dT%H:%M:00.000Z")
  
print(time_fetch())