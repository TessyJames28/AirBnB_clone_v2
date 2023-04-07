#!/usr/bin/python3
"""Fabric script that deletes out of date archives"""
from fabric.api import run, env, cd, lcd, local
import os


env.hosts = ["100.25.119.211", "100.25.48.208"]


def do_clean(number=0):
    """Deletes out of date archives and leaves most recent ones"""
    num = 1 if int(number) <= 1 else int(number)

    archives = sorted(os.listdir("versions"))
    with lcd("versions"):
        for archive in archives[:-num]:
            local("rm -f ./{}".format(archive))

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        del_arch = archives[:-num]
        for archive in del_arch:
            run("rm -f ./{}".format(archive))
