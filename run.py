"""
Simply runs the Flask app, pointing to the sub-package
"""

from nitroxserverlist import app


if __name__ == '__main__':
    app.run()