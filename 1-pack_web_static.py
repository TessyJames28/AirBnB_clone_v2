#!/usr/bin/python3
"""make a tarball of web_static files"""
from fabric.api import local, task, settings
from datetime import datetime
import os


@task
def do_pack():
    """make a tar archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if os.path.isdir("versions") is False:
            local("mkdir versions")
        local('rm -rf git_folder')
        local('git clone https://github.com/wisdom209/AirBnB_clone git_folder')
        local('cp -r git_folder/web_static .')
        local('rm -rf git_folder')
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        local('rm -rf web_static')
        return file_name
    except Exception:
        return None
