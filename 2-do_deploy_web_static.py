#!/usr/bin/python3
"""Write a Fabric script that generates a .tgz archive"""
from fabric.api import run, env, put
from os.path import exists
env.hosts = ['54.86.220.157', '100.26.212.86']
 


def do_deploy(archive_path):
    if exists(archive_path) is False:
        return False
    try:

        run('tar -xzvf /tmp/{archive_path} -C /data/web_static/releases/'
                           .format(archive_path))
        run('rm -r /tmp/')
        run ('rm -r /data/web_static/current')
        run ('sudo ln -sf /data/web_static/current /data/web_static/releases/')
        return True
    except:
        return False
