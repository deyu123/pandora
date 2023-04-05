import os
from os import getenv
from os.path import join

from appdirs import user_config_dir

if __name__ == '__main__':
    USER_CONFIG_DIR = getenv('USER_CONFIG_DIR', user_config_dir('Pandora-ChatGPT'))
    token_file = os.path.join(USER_CONFIG_DIR, 'access_token.dat')
    print(token_file)
