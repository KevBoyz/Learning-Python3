from requests import get

data = get('http://localhost:5000/users?name=KevBoyz&age=15').text
print(data)
