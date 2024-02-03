import requests

URL_DOMAIN = "https://kaas.to/"
url = "https://kaas.to/api/today_releases"

payload = "{\"client_id\":\"efcapamiilmdfbbilogcddbdckjhpajj\",\"user_id\":\"efc4b3ac3bc649c7b89998b11fd8dcfe\",\"events\":[{\"name\":\"main\",\"params\":{\"action\":\"\",\"pname\":\"fatkun-pro-mv3\"}}]}"
headers = {
  'authority': 'kaas.to',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'en,en-GB;q=0.9,en-US;q=0.8,ru;q=0.7,sl;q=0.6',
  'cache-control': 'max-age=0',
  'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
  'Referer': '',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
  'Origin': 'https://kaas.to',
  'referer': 'https://kaas.to/',
  'x-client-ts': '1706914800000',
  'x-timezone': '-60',
  'Content-Type': 'text/plain;charset=UTF-8'
}

def kaas():
  anime_data = {}
  anime_list = []
  response = requests.request("GET", url, headers=headers, data=payload).json()
  for i in response:
    title = i["title"]
    link = f"{URL_DOMAIN}{i['slug']}"
    print(link)
    anime_list.append([title, link])
  anime_data = {"https://kaas.to/": anime_list}
  return anime_data
kaas()