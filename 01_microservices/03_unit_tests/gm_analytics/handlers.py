def get_user_info(username):
    return {'username': username, 'id': '123', 'role': 'admin'}

def get_commits(username, start_date, end_date):
    return [{'timestamp': 'yyyy-mm-dd:hh:mm:ss', 'commit_message': 'Some updates'}]
