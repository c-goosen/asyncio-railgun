from asyncio import get_event_loop
from railgun.railgun import Railgun
from http import client


def example_method_one(one, two):
    return one + two


def example_call_api(host='www.google.com', url='/'):
    conn = client.HTTPSConnection(host, port=443, timeout=5)
    conn.request(method='GET', url=url)
    response = conn.getresponse()
    return response.status


def test_repeat():
    rail_gun = Railgun(semaphores_count=5, loop=get_event_loop())
    repeats = rail_gun.repeat(example_method_one, [1, 2], repeat=10)

    assert len(repeats) == 10
    assert repeats[0] == 3


def test_run():
    rail_gun = Railgun(semaphores_count=5, loop=get_event_loop())
    results = rail_gun.run([example_method_one(1, 2), example_method_one(1, 2)])
    assert len(results) == 2
    assert results[0] == 3


def test_run_async():
    loop = get_event_loop()
    rail_gun = Railgun(semaphores_count=5, loop=loop)
    results = rail_gun.run_async([example_method_one(1, 2), example_method_one(1, 2)])
    results = loop.run_until_complete(results)
    assert len(results) == 2
    assert results[0] == 3


def test_run_api_call():
    rail_gun = Railgun(semaphores_count=5, loop=get_event_loop())
    results = rail_gun.run([example_call_api(), example_call_api()])
    assert len(results) == 2
    assert results[0] == 200


def test_repeat_api_call():
    rail_gun = Railgun(semaphores_count=5, loop=get_event_loop())
    results = rail_gun.repeat(example_call_api, ['www.google.com', '/'], repeat=5)
    assert len(results) == 5
    assert results[0] == 200
