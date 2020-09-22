from app import create_app,db
from flask_script import Manager,Server







#creating an app instance  
app = create_app('development')  
# configure_uploads(app, (csvfiles,), lambda app: '/var/uploads')
