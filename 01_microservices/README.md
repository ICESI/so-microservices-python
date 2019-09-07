## Logging

```
import os

level = int(os.getenv('LOG_LEVEL'))
logging.basicConfig(level=level)

logging.debug('This is a DEBUG level message')
logging.info('This is an INFO level message')
logging.warning('This is a WARNING level message')
```
