import datetime
import json
import sqlite3
from multiprocessing import (
    Pool,
    cpu_count,
)
from multiprocessing.pool import ThreadPool

import pydantic
import requests


class People(pydantic.BaseModel):
    name: str
    height: int
    mass: int
    gender: str


def create_objects(parameters: list[tuple]) -> None:
    with sqlite3.connect("hw") as conn:
        cursor = conn.cursor()
        cursor.executemany(
            """
            INSERT INTO people VALUES (?,?,?,?)
        """, parameters,
        )
        conn.commit()


def get_url_list() -> list[str]:
    base_url = "https://swapi.dev/api/people/"
    url_list: list[str] = []
    for person_number in range(1, 11):
        url_list.append(f"{base_url}{person_number}")
    return url_list


def worker(url: str) -> People:
    try:
        response = requests.get(url)
        data = json.loads(response.text)
        people = People.parse_obj(data)
        return people
    except requests.exceptions.RequestException:
        pass


def download_form_pool() -> datetime.timedelta:
    start_time = datetime.datetime.now()
    urls = get_url_list()
    with Pool(processes=cpu_count()) as pool:
        people_list = pool.map(worker, urls)
        parameters = [(people.name, people.height, people.mass, people.gender) for people in people_list]
        create_objects(parameters)
    return datetime.datetime.now() - start_time


def download_form_thread_pool() -> datetime.timedelta:
    start_time = datetime.datetime.now()
    urls = get_url_list()
    pool = ThreadPool(processes=10)
    people_list = pool.map(worker, urls)
    pool.close()
    pool.join()
    parameters = [(people.name, people.height, people.mass, people.gender) for people in people_list]
    create_objects(parameters)
    return datetime.datetime.now() - start_time


def main():
    download_form_pool_time = download_form_pool()
    print(f"Pool: {download_form_pool_time}")
    download_form_thread_pool_time = download_form_thread_pool()
    print(f"ThreadPool: {download_form_thread_pool_time}")


if __name__ == "__main__":
    with sqlite3.connect("hw") as conn:
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS people;")
        cursor.execute("""CREATE TABLE people (
            name VARCHAR(500) NOT NULL,
            height INTEGER not null,
            mass INTEGER not null,
            gender VARCHAR(500) not null
        );""")
        conn.commit()
    main()
