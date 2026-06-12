import requests
import base64
import mimetypes

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
      return "Webhook sent!"
    
    except Exception as e:
      return f"An error occurred: {e}"

  def modify(self, name: str = None, avatar: str = None):
    payload = {}

    if name:
      payload["name"] = name

    if avatar:
      if avatar.startswith(("http://", "https://")):
        try:
          img_response = requests.get(avatar)
          img_response.raise_for_status()
          image_bytes = img_response.content
          mime_type = img_response.headers.get("Content-Type", "image/png")

        except Exception as e:
          return f"Failed to download image from URL: {e}"

      else:
        mime_type, _ = mimetypes.guess_type(avatar)
        if not mime_type:
          mime_type = "image/png"

        try:
          with open(avatar, "rb") as image_file:
            image_bytes = image_file.read()

        except Exception as e:
          return f"Failed to read local file: {e}"

      encoded_string = base64.b64encode(image_bytes).decode('utf-8')
      payload["avatar"] = f"data:{mime_type};base64,{encoded_string}"

    try:
      response = requests.patch(self.url, json=payload)
      response.raise_for_status()

      if name:
        self.username = name
      if avatar:
        self.avatar = avatar
      return "Webhook settings updated permanently on Discord!"

    except Exception as e:
      return f"An error occurred while modifying: {e}"
