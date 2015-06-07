import os
project_name_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if "production" in project_name_dir:
    DEBUG = False
else:
    DEBUG = True
