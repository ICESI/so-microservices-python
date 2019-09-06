import os
from fabric import task

@task
def pack_and_upload(c):
    # c.local('python setup.py sdist --formats=gztar')
    response = c.local('python setup.py --fullname')
    print(response)
    # filename = '%s.tar.gz' % response

    # upload the package to the temporary folder on the server
    # c.put('dist/%s' % filename, '/tmp/%s' % filename)

    # install the package in the application's virtualenv with pip
    # run('/var/www/yourapplication/env/bin/pip install /tmp/%s' % filename)

    # remove the uploaded package
    # run('rm -r /tmp/%s' % filename)

    # touch the .wsgi file to trigger a reload in mod_wsgi
    # run('touch /var/www/yourapplication.wsgi')


