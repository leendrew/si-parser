import time
import requests
from fake_useragent import UserAgent

def get_page(url: str):
  try:
    headers = {'user-agent': UserAgent().random}
    res = requests.get(url, headers=headers, timeout=10)

    if res.status_code != 200:
      print(f'STATUS CODE: {res.status_code}')
      time.sleep(3)
      get_page(url)

    return res.text

  except Exception as ex:
    print(ex)
    time.sleep(3)
    get_page(url)
