import sys

from app_settings import app
from management import execute_from_command_line

if __name__ == '__main__':
    execute_from_command_line(sys.argv)
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1
    app.run()
