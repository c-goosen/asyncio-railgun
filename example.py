from railgun.railgun import Railgun
import time
import asyncio
import requests

async def random_task_async(num, times):
    _ = num * times
    print(_)
    await asyncio.sleep(times)
    return _

def random_task(num, times):
    _ = num * times
    time.sleep(times)
    return _

def call_web(url='http://www.google.com'):
    return requests.get(url=url).status_code

async def call_web_async(url='http://www.google.com'):
    status_code = requests.get(url=url).status_code
    print(status_code)
    await asyncio.sleep(0.1)
    return status_code

# tasks = [random_task(5,10), random_task(1,1), random_task(2,5), random_task_async(6,3)]

tasks = [call_web() ] * 100
print('before railgun')
rail_gun = Railgun(semaphores_count=500)
# time.sleep(3)
print('After rail gun')
# test = rail_gun.run(tasks)
print('After rail gun run')

# print(test)
# print(f'len of returns {len(test)}')
loop = asyncio.get_event_loop()
async_tasks_1 = []
async_tasks_2 = []
start = time.time()
# for x in range(0, 299):
#     async_tasks_1.append(call_web_async())
#     async_tasks_2.append(call_web_async())
print(f'after for loop: {time.time() -start}')
# async_test_1 = loop.run_until_complete(rail_gun.run_async(async_tasks_1))
# async_test_2 = rail_gun.run(async_tasks_2)

# async_tasks_3 = [random_task_async(1,3), random_task_async(4,2), random_task_async(1,1)] * 100
# async_tasks_3 = async_tasks_3 + [random_task_async(2,6), random_task_async(2,2)]
from random import shuffle
# async_tasks_3 = list(shuffle(async_tasks_3))
# async_test_3 = rail_gun.run(async_tasks_3)

async_test_3 = rail_gun.repeat(random_task, [12, 0.01], 200)
print(async_test_3)
print(len(async_test_3))


start = time.time()
# print(async_test_1)
# print(time.time() - start)
# print('\n\n')
# start = time.time()
# print(async_test_2)
# print(time.time() - start)
# for x in async_test:
#     print(loop.run_until_complete(x))