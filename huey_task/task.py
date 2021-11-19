import logging
import time
import traceback
from pathlib import Path
from huey import SqliteHuey, signals

huey_db_path = Path("huey_demo.db").absolute()
huey = SqliteHuey(name="Huey Demo", fsync=True, filename=huey_db_path, utc=False)


@huey.pre_execute()
def pre_step(task):
    print("PRE-Step", task.name)


@huey.task(retries=1, retry_delay=5, context=True)
def add_two_numbers_that_need_a_long_period_of_time(number_a, number_b, task=None):
    time.sleep(8)
    return int(number_a) + int(number_b)


@huey.post_execute()
def post_hook(task, task_value, exc):
    print("POST-Step", task, task_value, exc)


@huey.signal(signals.SIGNAL_ERROR, signals.SIGNAL_SCHEDULED, signals.SIGNAL_EXECUTING, signals.SIGNAL_COMPLETE)
def signal_handler(signal, task, exception=None):
    if signal == "error":
        message = f"Task:[{task.name}] failed!\nTaskID: [{task.id}]\n" \
                  f"Args:[{task.args}]\nKwargs: [{task.kwargs}]\n" \
                  f"Exception: [{exception}][{traceback.format_exc()}]\nRetries: [{task.retries}]"
        logging.critical(message)
    print("SIGNAL", signal, task, exception)
