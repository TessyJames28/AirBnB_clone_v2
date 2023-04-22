#!/usr/bin/python3
"""make a tarball of web_static files"""
from fabric.api import local, task, run, put, env
from datetime import datetime
import os
import sys

# set connection parameters
env.hosts = ['54.173.2.233', '54.210.243.50']


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
        return False


@task
def deploy():
    """make a tar archive"""
    archive_path = do_pack()
    try:
        if os.path.exists(archive_path) is False:
            return False
        # split to get the archive name
        filename = archive_path.split('/')[-1]
        # get the archive name without extensions
        file_no_ext = filename.rstrip('.tgz')
        # push the archive to /tmp/ folder in server
        put(archive_path, '/tmp/{}'.format(filename))
        # maka a directory /data/web_static/releases/archive_name_no_ext
        run('mkdir -p /data/web_static/releases/{}/'.format(file_no_ext))
        # extract compressed archive in
        # /data/web_static/releases/archive_name_no_ext
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.
            format(filename, file_no_ext))
        # remove archive file in /tmp/
        run('rm -rf /tmp/{}'.format(filename))
        # archive extracts to a folder webstatic, move the contents out,
        # so they stand alone directly under /data/releases/web_static/archive
        # but first test if the archive subfolder webstatic exists already
        if run('test -e /data/web_static/releases/{}/web_static'
               .format(file_no_ext)).failed:
            run('mv -f /data/web_static/releases/{}/web_static\
                 /data/web_static/releases/{}/'.
                format(file_no_ext, file_no_ext))
        # remove the now empty webstatic folder
        run('rm -rf /data/web_static/releases{}/web_static'.
            format(file_no_ext))
        # delete old symbolic link
        run('rm -rf /data/web_static/current')
        # map symbolic link to deployed files
        run('ln -sf /data/web_static/releases/{}/web_static/\
             /data/web_static/current'.
            format(file_no_ext))
        print('New version deployed')
        return True
    except Exception:
        return False
