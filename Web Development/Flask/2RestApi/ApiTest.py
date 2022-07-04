from requests import get

# data = get('http://localhost:5000/users')
data = get('http://localhost:5000/users?name=KevBoyz&age=16').text
print(data)
