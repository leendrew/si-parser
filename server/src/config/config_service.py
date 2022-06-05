from enum import Enum
from dotenv import load_dotenv
import os

class CONFIG_ENV(Enum):
  POSTGRES_NAME = 'POSTGRES_NAME'
  POSTGRES_USER = 'POSTGRES_USER'
  POSTGRES_PASS = 'POSTGRES_PASS'
  POSTGRES_HOST = 'POSTGRES_HOST'
  POSTGRES_PORT = 'POSTGRES_PORT'
  POSTGRES_URL = 'POSTGRES_URL'
  APP_HOST = 'APP_HOST'
  APP_PORT = 'APP_PORT'

class _ConfigService:

  def __init__(self):
    self.__load_dotenv()

    self.POSTGRES_NAME = str(self.__get_env(CONFIG_ENV.POSTGRES_NAME.value))
    self.POSTGRES_USER = str(self.__get_env(CONFIG_ENV.POSTGRES_USER.value))
    self.POSTGRES_PASS = str(self.__get_env(CONFIG_ENV.POSTGRES_PASS.value))
    self.POSTGRES_HOST = str(self.__get_env(CONFIG_ENV.POSTGRES_HOST.value))
    self.POSTGRES_PORT = int(self.__get_env(CONFIG_ENV.POSTGRES_PORT.value))
    self.POSTGRES_URL = str(self.__get_env(CONFIG_ENV.POSTGRES_URL.value))
    self.APP_HOST = str(self.__get_env(CONFIG_ENV.APP_HOST.value))
    self.APP_PORT = int(self.__get_env(CONFIG_ENV.APP_PORT.value))

  def __load_dotenv(self):
    load_dotenv('.env')

  def __get_env(self, env: str):
    try:
      return os.getenv(env)
    except:
      raise Exception(f'Invalid value for {env}')

config_service = _ConfigService()
