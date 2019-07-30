import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	DEBUG = False
	TESTING = False
	CSRF_ENABLED = True
	SECRET_KEY = "f95b0391fc26cddb3b563fab72fa7a4f3fa5f29d29e18a4b4fbd98125d8b39f8"
	
class ProductionConfig(Config):
	DEBUG = False
	
class StagingConfig(Config):
	DEVELOPMENT = True
	DEBUG = True
	
class DevelopmentConfig(Config):
	DEVELOPMENT = True
	DEBUG = True
	
class TestingConfig(Config):
	TESTING = True