import os
WORKSPACE = os.path.dirname(os.path.abspath(__file__))
SETTINGS = {
	'autoreload': True,
    'login_url': 'http://localhost:8888',
    'debug': True,
    'template_path': os.path.join(WORKSPACE, 'templates'),
    'static_path': os.path.join(WORKSPACE, 'static'),
    'sqlite_path': os.path.join(WORKSPACE, 'sqlite')}
