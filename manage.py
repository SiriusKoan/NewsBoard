import unittest
from os import getenv
from flask_script import Manager
from app import create_app

app = create_app(getenv("env"))
manager = Manager(app)

@manager.command
def run_test():
    print("Start testing.")
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner().run(tests)
    
if __name__ == '__main__':
    manager.run()