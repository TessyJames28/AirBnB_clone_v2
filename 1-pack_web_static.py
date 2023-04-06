#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
folder of AirBnB Clone repo
"""
from fabric.api import task, local
from datetime import datetime


@task
def do_pack():
    """
    All files in the folder web_static must be added to the final archive
    All archives must be stored in the folder versions (create it if not exist)
    Archive name - web_static_<year><month><day><hour><minute><second>.tgz
    Return the archive path if successful otherwise return None
    """
    try:
        local("mkdir versions")
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        arch_name = f"versions/web_static_{timestamp}.tgz"
        local(f"tar -czvf {arch_name} /AirBnb_clone/web_static")
        return arch_name
    except Exception:
        return None
