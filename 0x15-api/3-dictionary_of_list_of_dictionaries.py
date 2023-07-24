#!/usr/bin/python3

"""
A Python script to export data in the JSON format.
"""

from requests import get
import json


if __name__ == "__main__":
    endpoint = "https://jsonplaceholder.typicode.com"
    users = get(endpoint + "/users/").json()
    to_dos = get(endpoint + "/todos/").json()

    index, records = 0, list()
    id, user, all = users[index]["id"], users[index]["username"], dict()

    for to_do in to_dos:
        if to_do["userId"] != id:
            all[id] = records
            index += 1
            id, user = users[index]["id"], users[index]["username"]
            records = list()
        records.append({"username": user, "task": to_do["title"],
                        "completed": to_do["completed"]})

    all[id] = records

    # Exporting data in the JSON format file
    with open("todo_all_employees.json", "w") as f:
        json.dump(all, f)
