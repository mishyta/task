import requests

response = requests.get("https://randomuser.me/api/")  # A free, open-source API for generating random user data.

print(response.status_code)


# Status codes:
# 200 OK 	
# 201 Created 	
# 400 Bad Request 	
# 401 Unauthorized 	
# 404 Not Found 	
# 405 Method Not Allowed 	
# 500 Internal Server Error 	


#
#
# user = json.dumps(response.json(), indent=4)
# print(user)


def get_curse_btc_usd():
    curse = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=1').json()[0]
    return f'1BTC = {curse["buy"]}USD'


def send_massege_to_telegram(message):
    bot_token = 'bot1918829163:AAE_xG8UmFM3tgPx-5MYR_yjRFzIMRLurHA'
    post_params = {'chat_id': '507481126', 'text': message}
    return requests.post(f'https://api.telegram.org/{bot_token}/sendMessage?', params=post_params)


send_massege_to_telegram(get_curse_btc_usd())
