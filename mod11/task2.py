import datetime
import json
import sqlite3
import typing
from threading import Thread

import pydantic
import requests
from requests import Response


class People(pydantic.BaseModel):
    name: str
    height: int
    mass: int
    gender: str


class SW(Thread):
    def __init__(self, url):
        super(SW, self).__init__()
        self.url = url

    def run(self):
        response = requests.get(self.url)
        data = json.loads(response.text)
        people = People.parse_obj(data)
        create_objects([(people.name, people.height, people.mass, people.gender)])


def get_url_list() -> list[str]:
    base_url = "https://swapi.dev/api/people/"
    url_list: list[str] = []
    for person_number in range (1, 11):
        url_list.append(f"{base_url}{person_number}")
    return url_list


def get_response(urls: list[str]) -> list[Response]:
    response_list: list[Response] = []
    for url in urls:
        try:
            response_list.append(requests.get(url))
        except:
            continue
    return response_list


def pars_object(responses: list[Response]) -> list[People]:
    people_list: list[People] = []
    for response in responses:
        try:
            data = json.loads(response.text)
            people_list.append(People.parse_obj(data))
        except:
            continue
    return people_list

def create_objects(parameters: list[tuple]) -> None:
    with sqlite3.connect("hw") as conn:
        cursor = conn.cursor()
        cursor.executemany(f"""
            INSERT INTO people VALUES (?,?,?,?)
        """, parameters)
        conn.commit()

def one_threed() -> datetime.timedelta:
    start_time = datetime.datetime.now()
    urls = get_url_list()
    responses = get_response(urls)
    people_list = pars_object(responses)
    parameters = [(people.name, people.height, people.mass, people.gender) for people in people_list]
    create_objects(parameters)
    end_time = datetime.datetime.now()
    return end_time - start_time


def get_response_for_threed(urls: list[str]) -> list[Response]:
    pass


def many_threeds() -> datetime.timedelta:
    start_time = datetime.datetime.now()
    urls = get_url_list()
    thread_list: list[Thread] = []
    for url in urls:
        sw = SW(url)
        sw.start()
        thread_list.append(sw)
    for sw in thread_list:
        sw.join()
    end_time = datetime.datetime.now()
    return end_time - start_time


def main():
    build_time_one_threed = one_threed()
    print(f"one threed {build_time_one_threed}")
    build_time_many_threeds = many_threeds()
    print(f"many threeds {build_time_many_threeds}")



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
