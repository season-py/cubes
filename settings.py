import os

WORKSPACE = os.path.dirname(os.path.abspath(__file__))

SETTINGS = {
    'cookie_secret': '61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=',
    'xsrf_cookies': True,
    'autoreload': True,
    'login_url': '/auth',
    'debug': True,
    'template_path': os.path.join(WORKSPACE, 'templates'),
    'static_path': os.path.join(WORKSPACE, 'static'),
    'sqlite_path': os.path.join(WORKSPACE, 'sqlite')}

