from app.API import core_api

from flask import request

from huey_task.task import huey, add_two_numbers_that_need_a_long_period_of_time


@core_api.get("/")
def index():
    return "Welcome to Huey x Flask Demo."


@core_api.get("/add")
def add_a_and_b():
    get_params = request.args
    a = get_params.get("a")
    b = get_params.get("b")
    task = add_two_numbers_that_need_a_long_period_of_time(a, b)
    return task.id


@core_api.get("/get")
def get_result():
    return f'<h1>Task Result: {huey.get(request.args.get("id"))}</h1>'
