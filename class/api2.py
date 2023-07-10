import requests
response = requests.get('https://api-customer-038j.onrender.com/customer/',{'name':'chisom','age':20, 'order':'cake'} )

print(response.json())