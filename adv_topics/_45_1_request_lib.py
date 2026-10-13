import requests

# r = requests.get('https://xkcd.com/353/')
r = requests.get("https://imgs.xkcd.com/comics/python.png")

# payload = {'page': 2, 'count': 25}
# payload = {'username': 'corey', 'password': 'testing'}

# r = requests.get('https://httpbin.org/get', params = payload)
# r = requests.post('https://httpbin.org/post', data = payload)
# r = requests.get('https://httpbin.org/basic-auth/shashank/testing', auth = ('shashankms', 'testing'))
# r = requests.get('https://httpbin.org/basic-auth/shashank/testing', timeout = 3)

# print(r)
# print(dir(r))
# print(help(r))

# print(r.text)
with open("D:/Python/adv_topics/_45_2_comic.png", "wb") as f:
    f.write(r.content)

# print(r.status_code)
# print(r.ok)
# print(r.headers)

# print(r.text)
# print(r.url)
# print(r.json())
# r_dict = r.json()
# print(r_dict['form'])

# print(r.text)
# print(r)
