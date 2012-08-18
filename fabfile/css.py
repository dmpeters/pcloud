from fabric.api import local, task

@task
def watch():
    local('sass -l --watch ./public/resources/css/src/:./public/resources/css/')

