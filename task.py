import urllib.request
import json

def url1():
  html = urllib.request.urlopen("https://api.vk.com/method/users.get?user_ids=1&v=5.8&fields=status,education").read()
  data = json.loads(html)
  u = data.get('response')

  for user in u:
    print("First name: " + str(user['first_name']))
    print("Last name: " + str(user['last_name']))
    print("Nickname: " + str(user['nickname']))
    print("Status: " + str(user['status']))
    print("Online: " + str(user['online']))
    print("Сountry: " + str(user['country']))    
print(url1())
