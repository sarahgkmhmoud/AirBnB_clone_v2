#!/usr/bin/python3
"""Write a Fabric script that generates a .tgz archive"""
from fabric.api import run, env, put
from os.path import exists
env.hosts = ['54.86.220.157', '100.26.212.86']
 


def do_deploy(archive_path):
    if exists(archive_path) is False:
        return False
    try:
        _file = archive_path.split("/")[-1]
        match_path = _file.split('.')[0]
        remote_path = '/data/web_static/releases/'
        put(archive_path, '/tmp/')
        run(f'mkdir -p {remote_path}{match_path}/')
        run(f'tar -xzf /tmp/{_file} -C {remote_path}{match_path}')
        run(f'rm -r /tmp/{_file}')
        run(f'mv {remote_path}{match_path}/web_static/* {remote_path}{match_path}/')
        run(f'rm -rf {remote_path}{match_path}/web_static/*')
        run (f'rm -rf /data/web_static/current')
        run (f'sudo ln -sf {remote_path}/ /data/web_static/current')
        return True
    except:
        return False