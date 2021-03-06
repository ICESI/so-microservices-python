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

Tests with pytest
```
pip3 install -r requirements_dev.txt --user
pytest -v
```

Test with tox
```
pip3 install -r requirements_dev.txt --user
tox -e pytest
```

## Logging example

```
import os

level = int(os.getenv('LOG_LEVEL'))
logging.basicConfig(level=level)

logging.debug('This is a DEBUG level message')
logging.info('This is an INFO level message')
logging.warning('This is a WARNING level message')
```
