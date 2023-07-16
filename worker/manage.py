import os
import json
import subprocess

class Worker():
    def generate_host_file(self, hosts: list) -> str:
        temp = {
            "all": {
                "hosts": {
                    "146.190.49.200": None
                },
                "children": {
                    "webservers": {
                        "hosts": {
                            "remote": {
                                "ansible_host": "146.190.49.200",
                                "ansible_port": 22,
                                "ansible_user": "root"
                            }
                        }
                    }
                }
            }}
        
        file_name = "host.json"
        with open(file_name, "w+") as p:
            p.write(json.dumps(temp))
        return file_name
        
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
        host_file = self.generate_host_file(hosts)
        subprocess.call(["ansible-playbook", file_name, "-i", host_file])
        os.remove(file_name)
        os.remove(host_file)

