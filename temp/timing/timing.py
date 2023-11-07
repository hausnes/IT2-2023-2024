# Kjelde for meir informasjon om deler av koden under, samt alternative måtar
# å køyre kode på ved faste intervall: https://dev.to/alinsky/automation-scheduling-python-programs-pushing-notifications-executing-sqls-etc-4ob0

import schedule
import time

job1Count = 0
job2Count = 0

def job1():
    global job1Count
    job1Count += 1
    print(f"I'm working on task no. 1. I've done this job {job1Count} times so far.")

def job2():
    global job2Count 
    job2Count += 1
    print(f"I'm working on task no. 2. I've done this job {job2Count} times so far.")

# schedule.every().day.at("10:30").do(job1)
schedule.every(5).seconds.do(job1)
schedule.every(10).seconds.do(job2)
# schedule.every().hour.do(job1)
# schedule.every().tuesday.at("13:15").do(job2)

while True:
    schedule.run_pending()
    time.sleep(1)