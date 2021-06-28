from datetime import datetime
import schedule as sc


@sc.repeat(sc.every(3).seconds, info=True)
def simple_task(info=False):
    print(datetime.now().second) if info else None


@sc.repeat(sc.every(10).seconds)
def once_job():
    print('I\' do my part, goodbye')
    return sc.CancelJob


sc.every(4).seconds.do(simple_task, info=True)


while True:
    sc.run_pending()