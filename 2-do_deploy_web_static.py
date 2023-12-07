#!/usr/bin/python3
"""Write a Fabric script that generates a .tgz archive"""
from fabric import Connection
from fabric import run


def do_deploy(archive_path):
    if archive_path:
        servers = ['ubuntu@54.86.220.157', 'ubuntu@100.26.212.86']
        connection = Connection(servers).put(archive_path,'/tmp/' )
        with Connection(servers) as result:
            result.run('tar -xzvf /tmp/{archive_path} -C /data/web_static/releases/'
                           .format(archive_path))
            result.run('rm -r /tmp/')
            result.run ('rm -r /data/web_static/current')
            result.run ('sudo ln -sf /data/web_static/current /data/web_static/releases/')
        return True
    else:
        return False
