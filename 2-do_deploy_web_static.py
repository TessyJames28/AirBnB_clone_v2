#!/usr/bin/python3
"""Fabric script that distributes an archive to web servers"""
from fabric.api import put
from fabric.api import run
from fabric.api import env
import os


env.hosts = ["100.25.119.211", "100.25.48.208"]


def do_deploy(archive_path):
    """fabric command to deploy archive to remote servers"""
    if os.path.isfile(archive_path) is False:
        return False

    path = archive_path.split("/")[-1]
    filename = path.split(".")[0]

    try:
        put(archive_path, "/tmp/{}".format(path))
        run("rm -rf /data/web_static/releases/")
        run("mkdir -p /data/web_static/releases/{}".format(filename))
        run("tar xzf /tmp/{} -C /data/web_static/releases/{}/".
            format(path, filename))
        run("rm -rf /tmp/{}".format(filename))
        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(filename, filename))
        run("rm -rf /data/web_static/releases/{}/web_static".format(filename))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{} /data/web_static/current".
            format(filename))
        print("New version deployed!")
        return True
    except Exception:
        return False
