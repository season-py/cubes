import os
WORKSPACE = os.path.dirname(os.path.abspath(__file__))
SETTINGS = {
        'login_url': 'http://localhost:8888',
        'template_path': os.path.join(WORKSPACE, 'templates'),
        'sqlite_path': os.path.join(WORKSPACE, 'sqlite')}
