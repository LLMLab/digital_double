import requests

def chat(input, history=[]):
  headers = {
    "Authorization": "Bearer sk-TmUhOQKWsJ5t43QVoGBblSw3GFOMZwZhpGFlCGX7jxwedsdN"
  }
  _history = []
  for item in history:
    _history.append({"role": "user", "content": item[0]})
    _history.append({"role": "assistant", "content": item[1]})
  j = {
    "model": "gpt-3.5-turbo",
    "messages": [*_history, {"role": "user", "content": input}],
    "temperature": 0.7 
  }
  result = requests.post('https://api.aiproxy.io/v1/chat/completions', json=j, headers=headers)
  return result.json()['choices'][0]['message']['content']

if __name__ == '__main__':
  print(chat('你好'))
