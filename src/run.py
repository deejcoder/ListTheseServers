"""
Simply runs the Flask app, pointing to the sub-package
"""

from app import create_app


if __name__ == '__main__':
    app = create_app('settings')
    app.run()