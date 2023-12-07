#!/usr/bin/python3
"""Write a Fabric script that generates a .tgz archive"""
from fabric.api import local
from datetime import datetime
from os.path import isdir


def do_pack():
    """Trying to do that"""
    try:
        data = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(data)
        local(f"tar -cvzf {file_name} web_static")
        return file_name
    except:
        return None
# """
# Fabric script that generates a tgz archive from the contents of the web_static
# folder of the AirBnB Clone repo
# """

# from datetime import datetime
# from fabric.api import local
# from os.path import isdir


# def do_pack():
#     """generates a tgz archive"""
#     try:
#         date = datetime.now().strftime("%Y%m%d%H%M%S")
#         if isdir("versions") is False:
#             local("mkdir versions")
#         file_name = "versions/web_static_{}.tgz".format(date)
#         local("tar -cvzf {} web_static".format(file_name))
#         return file_name
#     except:
#         return None