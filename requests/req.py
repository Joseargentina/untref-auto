import requests


r = requests.get('https://jsonplaceholder.typicode.com/posts/5')

# print(r.status_code)
# print(r.text)

# print(r.json())

# resp = r.json()
# print(resp['title'])
# print(r.json()['title'])
#r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user','pass'))
#print(r.status_code)
#print(r.text)

r = requests.post('https://jsonplaceholder.typicode.com/posts', data = {'title': 'foo','body': 'bar','userId': 1})
print(r.status_code)
print(r.text)