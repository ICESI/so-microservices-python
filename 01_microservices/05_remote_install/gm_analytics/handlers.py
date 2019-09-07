def get_user_info(username):
    user_data = {'username': username, 'id': '123'}
    user_data['role'] = query_role(username)
    return user_data

def query_role(username):
    return 'admin'

def get_commits(username, start_date, end_date):
    return [{'timestamp': 'yyyy-mm-dd:hh:mm:ss', 'commit_message': 'Some updates'}]
