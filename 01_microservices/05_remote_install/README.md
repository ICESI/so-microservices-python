# Remote installation

### Deploy with factory 

```
ssh-keygen -t rsa
ssh-copy-id -i ~/.ssh/id_rsa.pub pi@d4n13lbc.ddns.net -p 30022
ssh -p 30022 pi@d4n13lbc.ddns.net
pip install factory

python3
>>> from fabric import Connection
>>> c = Connection('pi@d4n13lbc.ddns.net:30022')
>>> result = c.run('uname -s')
```