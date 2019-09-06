from flask import Flask
import logging.config
logging.config.fileConfig('logging.conf')
log = logging.getLogger(__name__)

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/hello')
    def hello():
        log.info('info message')
        log.debug('debug message')
        return 'Hello, World!'

    return app
