import requests

api_key = 'fad3fb54b614135f4c9ce3a112ea6212a63f3640'  # Thay bằng API Key của bạn
birth_year = 1990
url = f'https://api.astrologyapi.com/v1/sun_sign_prediction/daily/?year={birth_year}&api_key={api_key}'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Con giáp: {data['zodiac']}")
    print(f"Mệnh: {data['element']}")
else:
    print('Lỗi:', response.status_code)


