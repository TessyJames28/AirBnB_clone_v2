#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
folder of AirBnB Clone repo
"""
from fabric.api import task, local
from datetime import datetime
import os


def do_pack():
    """
    All files in the folder web_static must be added to the final archive
    All archives must be stored in the folder versions (create it if not exist)
    Archive name - web_static_<year><month><day><hour><minute><second>.tgz
    Return the archive path if successful otherwise return None
    """
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
