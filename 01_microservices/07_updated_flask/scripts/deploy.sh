# https://stackoverflow.com/questions/47736059/flask-config-not-being-loaded-using-flask-app-and-app-factory
# https://github.com/pallets/flask/issues/2661
# https://docs.python.org/2.0/dist/creating-rpms.html

# run service with flask run
export FLASK_ENV=development
export FLASK_APP="gm_analytics:create_app()"
export FLASK_RUN_PORT=8050
flask run --host 0.0.0.0

# run service with python
export PYTHONPATH=$PYTHONPATH:`pwd`
python gm_analytics/app.py

# create service package
python setup.py release sdist

# create service development package
python setup.py sdist 

# install service
python setup.py install

# install service with development dependencies
python setup.py develop

# create rpm package
sudo apt instal rpm -y
python setup.py bdist --formats=rpm

# create rpm with specfile
python setup.py bdist_rpm --spec-only --requires="python3"
python setup.py bdist_rpm --spec-file=dist/gm_analytics.spec

# deploy with factory 
ssh-keygen -t rsa
ssh-copy-id -i ~/.ssh/id_rsa.pub pi@d4n13lbc.ddns.net -p 30022
ssh -p 30022 pi@d4n13lbc.ddns.net
pip install factory

>>> from fabric import Connection
>>> c = Connection('pi@d4n13lbc.ddns.net:30022')
>>> result = c.run('uname -s')

sudo apt-get install libapache2-mod-wsgi
