#!/usr/bin/python3
"""learning fabric"""
from fabric import task, Connection

conn = Connection('ubuntu@54.210.243.50')

@task
def print_file(c):
    c.run('echo "hello world" > print_me')
    result = c.run('cat ~/print_me')
    print(result.stdout)

def put_file(c):
    c.put('0-setup_web_static.sh', '/home/ubuntu/')

put_file(conn)
