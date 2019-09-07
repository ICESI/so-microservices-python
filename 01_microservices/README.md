<<<<<<< HEAD
# Microservices with Python

### How to execute the examples

Development
```
./scripts/deploy.sh
```

Production
```
export PRODUCTION=true
./scripts/deploy.sh
```

Tests
```
pip3 install -r requirements_dev.txt --user
tox -e pytest
```

## Logging example
=======
## Logging
>>>>>>> 2acce4f6382559a58ca11ed53799862e81f107d9

```
import os

level = int(os.getenv('LOG_LEVEL'))
logging.basicConfig(level=level)

logging.debug('This is a DEBUG level message')
logging.info('This is an INFO level message')
logging.warning('This is a WARNING level message')
```
