from fabric.api import local, task
import css, heroku

@task
def run():
    local('python manage.py runserver [::]:8000')


@task
def reset():
    local('rm -f sqlite.db')
    local('python manage.py syncdb --noinput')
    local('python manage.py createsuperuser --username=user --email=user@host.com')


