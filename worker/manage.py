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
        
    def give_access(self, key, user, hosts: list, group_name="team", root_access=False) -> None:
        ssh_file = f"{user}.pub"
        with open(ssh_file, "w+") as p:
            p.write(key)

        tasks = [
            {
                "name": f"Make sure we have a '{group_name}' group",
                "group": {
                    "name": group_name,
                    "state": "present"
                }
            },
            {
                "name": f"Allow '{group_name}' group to have passwordless sudo",
                "lineinfile": {
                    "dest": "/etc/sudoers",
                    "state": "present",
                    "regexp": f"^%{group_name}",
                    "line": f"%{group_name} ALL=(ALL) NOPASSWD: ALL",
                    "validate": "visudo -cf %s"
                }
            },
            {
                "name": f"Add sudoers users to {group_name} group",
                "user": f"name={user} groups={group_name} append=yes state=present createhome=yes"
            },
            {
                "name": "Set up authorized keys for the {user} user",
                "authorized_key": "user={user} key=\"{{item}}\"",
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
        # TODO: Log subprocess output - https://www.endpointdev.com/blog/2015/01/getting-realtime-output-using-python/
        os.remove(file_name)
        os.remove(host_file)
        os.remove(ssh_file)

