import requests

response = requests.get('https://httpbin.org/ip', verify=False)

print('Your IP is {0}'.format(response.json()['origin']))