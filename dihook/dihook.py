import requests

class Dihook:
  def __init__(self, url: str, username: str = None, avatar: str = None):
    self.url = url
    self.username = username
    self.avatar = avatar

  def send(self, text: str, username: str = None, avatar: str = None):
    self.text = text
    payload = {
      "content": text
  }

    active_username = username or self.username
    active_avatar = avatar or self.avatar

    if active_username:
      payload["username"] = active_username
    if active_avatar:
      payload["avatar_url"] = active_avatar 

    try:
      response = requests.post(self.url, json=payload)
      response.raise_for_status()
      return "succes!"
    
    except Exception as e:
      return f"An error occurred: {e}"