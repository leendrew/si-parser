import json

def get_accepted_types(_json):
  _dict = json.loads(_json)
  accepted_types = []

  for key, value in _dict.items():
    if value:
      accepted_types.append(key)

  return accepted_types
