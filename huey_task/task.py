import logging
import time
import traceback
from pathlib import Path
from huey import SqliteHuey, signals

huey_db_path = Path("huey_demo.db").absolute()
huey = SqliteHuey(name="Huey Demo", fsync=True, filename=huey_db_path, utc=False)


@huey.task(retries=1, retry_delay=5, context=True)
def add_two_numbers_that_need_a_long_period_of_time(number_a, number_b, task=None):
    time.sleep(8)
    return int(number_a) + int(number_b)


@huey.signal(signals.SIGNAL_ERROR)
def task_error(signal, task, exception):
    message = f"Task:[{task.name}] failed!\nTaskID: [{task.id}]\n" \
              f"Args:[{task.args}]\nKwargs: [{task.kwargs}]\n" \
              f"Exception: [{exception}][{traceback.format_exc()}]\nRetries: [{task.retries}]"
    logging.critical(message)
