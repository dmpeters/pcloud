from fabric.api import local, cd, get, env, roles, execute, task
import os

@task
def resetdb():
	local('heroku pg:reset DATABASE')
	local('heroku run python manage.py syncdb')

@task
def open():
	local('heroku open')
