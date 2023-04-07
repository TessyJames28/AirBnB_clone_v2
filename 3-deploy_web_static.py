#!/usr/bin/python3
"""Fabric script base on file 2-do_deploy_web_static.py"""
from fabric.api import run, put, env, task, local
from fabric.tasks import execute
from datetime import datetime
import os


env.hosts = ["100.25.119.211", "100.25.48.208"]


def do_pack():
    """create a tar gzipped file"""
    try:
        if os.path.isdir("versions") is False:
            if local("mkdir versions").failed is True:
                return None
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        arch_name = "versions/web_static_{}.tgz".format(timestamp)
        local("tar -czvf {} web_static".format(arch_name))
        return arch_name
    except Exception:
        return None


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


def deploy():
    """creates and distributes an archive to your web servers"""
    archive = do_pack()
    if archive is None:
        return False
    return do_deploy(archive)
