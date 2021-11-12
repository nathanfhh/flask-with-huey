def test_get_task_result_will_success(client):
    response = client.get("/get")
    assert response.status_code == 200


def test_huey_task_1():
    from huey_task.task import add_two_numbers_that_need_a_long_period_of_time
    # 會跑一陣子，因為途中被加了time.sleep()
    assert add_two_numbers_that_need_a_long_period_of_time.call_local("2", 3) == 5


def test_huey_task_2():
    from huey_task.task import huey, add_two_numbers_that_need_a_long_period_of_time
    # 會跑一陣子，因為途中被加了time.sleep()
    huey.immediate = True
    task = add_two_numbers_that_need_a_long_period_of_time("2", 3)
    assert huey.get(task.id) == 5
