import os #
from dotenv import load_dotenv




basedir = os.path.abspath(os.path.dirname(__file__)) # this is establishing our base directory to our root folder

load_dotenv(os.path.join(basedir, '.env')) #this is just pointing us to the direction of our environment variables (located in .env file)

#making this a seperate class we can have many Config classes (aka 1 for development, 1 for production)
class Config():

   
    """
    Set Config variables for our flask app.
    Using Environment variables where available otherwise
    Create config variables.
    """

    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    FLASK_DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or "Nana nana boo boo, you'll never guess this"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #hide update messages