from environs import Env

env = Env()
env.read_env()

DEBUG = env("DEBUG")
SECRET_KEY = env("SECRET_KEY")
SQLALCHEMY_DATABASE_URI = env("SQLALCHEMY_DATABASE_URI")
