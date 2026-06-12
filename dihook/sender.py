import requests

def send(url: str, content: str):
  payload = {
    "content": content
  }

  try:
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return "succes!"
    
  except Exception as e:
    return f"An error occurred: {e}"