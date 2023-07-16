import os
import json
import subprocess

class Worker():
    def generate_host_file(self, hosts: list) -> str:
        temp = {
            "all": {
                "children": {
                    "webservers": {
                        "hosts": {}
                    }
                }
            }
        }

        for host in hosts:
            entry =  {}
            entry[host.label] = {}
            entry[host.label]["ansible_host"] = host.ip_address
            entry[host.label]["ansible_port"] = host.ssh_port
            entry[host.label]["ansible_user"] = host.ssh_user
            temp["all"]["children"]["webservers"]["hosts"] = entry
        
        file_name = "host.json"
        with open(file_name, "w+") as p:
            p.write(json.dumps(temp))
        return file_name
        
    def give_access(self, key, hosts: list) -> None:
        ssh_file = "felix.pub"
        with open(ssh_file, "w+") as p:
            p.write(key)
            
        tasks = [
            {
                "name": "Make sure we have a 'team' group",
                "group": {
                    "name": "team",
                    "state": "present"
                }
            },
            {
                "name": "Allow 'team' group to have passwordless sudo",
                "lineinfile": {
                    "dest": "/etc/sudoers",
                    "state": "present",
                    "regexp": "^%team",
                    "line": "%team ALL=(ALL) NOPASSWD: ALL",
                    "validate": "visudo -cf %s"
                }
            },
            {
                "name": "Add sudoers users to team group",
                "user": "name=felix groups=team append=yes state=present createhome=yes"
            },
            {
                "name": "Set up authorized keys for the felix user",
                "authorized_key": "user=felix key=\"{{item}}\"",
                "with_file": [ssh_file, ]
            }
        ]

        playbook = [{
            "name": "Add SSH Key",
            "hosts": [
                "webservers"
            ],
            "gather_facts": "no",
            "tasks": tasks
        }]

        file_name = "playbook.json"
        with open(file_name, "w+") as p:
            p.write(json.dumps(playbook))
        host_file = self.generate_host_file(hosts)
        subprocess.call(["ansible-playbook", file_name, "-i", host_file])
        # os.remove(file_name)
        # os.remove(host_file)

