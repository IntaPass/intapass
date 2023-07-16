import os
import json
import subprocess

class Worker():
    def give_access(self, keys: list, hosts: list) -> None:
        playbook = [{
            "name": "Test script",
            "hosts": [
                "webservers"
            ],
            "gather_facts": "no",
            "tasks": [
                {
                    "name": "List dir",
                    "command": "ls -la /home/"
                }
            ]
        }]

        file_name = "playbook.json"
        with open(file_name, "w+") as p:
            p.write(json.dumps(playbook))
        subprocess.call(["ansible-playbook", file_name, "-i", "hosts.yml"])
        os.remove(file_name)

