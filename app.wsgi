activate_this = '/home/user/flask_test/flask_test/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))
import sys
sys.path.insert(0, '/home/user/flask_test')
from app import app as application