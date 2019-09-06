import logging

def get_user_info(username):
    logging.info('This is an INFO level message - executing get_user_info method')
    logging.debug('This is a DEBUG level message - username=%s', username)
    logging.warning('This is a WARNING level message - method hasn\'t been implemented yet')
    return {'id': '000', 'role': 'admin'}
