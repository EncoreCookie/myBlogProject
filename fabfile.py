from fabric.api import env, run
from fabric.operations import sudo

GIT_REPO = "https://github.com/EncoreCookie/myBlogProject.git"

env.user = 'encore'
env.password = '920909'

env.hosts = ['www.mingxin666.com']

env.port = '27485'


def deploy():
    source_folder = '/home/encore/sites/www.mingxin666.com/myBlogProject'

    run('cd %s && git pull' % source_folder)
    run("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder))
    sudo('restart gunicorn-www.mingxin666.com')
    sudo('service nginx reload')