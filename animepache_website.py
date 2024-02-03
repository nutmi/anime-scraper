import requests

domain_url = "https://animepahe.ru/play/"
URL = "https://animepahe.ru/api?m=airing&page=1"

payload = "{\"client_id\":\"efcapamiilmdfbbilogcddbdckjhpajj\",\"user_id\":\"caa7f7fffbc64cc589d53eb287a9241b\",\"events\":[{\"name\":\"main\",\"params\":{\"action\":\"\",\"pname\":\"fatkun-pro-mv3\"}}]}"
headers = {
  'authority': 'animepahe.ru',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'en,en-GB;q=0.9,en-US;q=0.8,ru;q=0.7,sl;q=0.6',
  'cache-control': 'max-age=0',
  'cookie': 'cf_clearance=myO9k1hufkd88wFF6bfHvSKpcNRWoULgztDvdfiVgk4-1704728768-0-2-6b038933.a4b5ad94.25a43cc6-0.2.1704728768; res=720; aud=jpn; av1=0; __ddgid_=nhulCATpo5qM1ce7; __ddg2_=D288vllMQe19n8dX; __ddg1_=soHTP3XWth1xb1glymX6; SERVERID=janna; latest=5361; XSRF-TOKEN=eyJpdiI6IjFEUVNQOWV2bmZwTm5VNEhWTGVudHc9PSIsInZhbHVlIjoicDhEMjVsZkpXSUlnZklqNXpMdUN4N0tGN2tRbHBuMG0waWJxeVlFYTNWT243YnEwTFQ4UEt4Y1pqcTZsWmZKSDB1anUySUowNzF2QlpIMzR4d2J4YW9rNWRBa1R1djBDcDBjTytDMXpPSzJVYlNNWnoxWFozWHZKVTRpeGdTMFkiLCJtYWMiOiI1YmI3NzMwNjQyMzFhODk2YWNmNmMyYTczOWUyOWQ1M2I0MTU4OTFjMjEwNjQxNDA0NDY4MjA1MGEyZjkzZDIxIiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6IkdveVl5c2dnNllrdEJSZUhMeExjMmc9PSIsInZhbHVlIjoiNWdyRmUwbFJPdVVDUE9LOEFlL0p1T2hJUGVDQlg5MW5aY2dFYXVRdTRSM1JDLzMxS2xoZUJGeGpaWkdhM1NkOFQ1OFZvaDd5bVB6UjVuYVRIb2oxeHpHb3BHQkdkSTkxajB2Z2djUGZTUGdOeWNJbjdyME1SMVh0NFVXTEd5YzciLCJtYWMiOiI2NzA2ODIyN2NlYWQ5M2VkYjAzNTY5NDM4NjZiMTJjMTJhZGMyZWUzY2U1ZWY1YmRiMTdlMzdjOTA0YjQzMzE0IiwidGFnIjoiIn0%3D; XSRF-TOKEN=eyJpdiI6ImM5NHl4aUwvK2V3MkZITEVLem94cFE9PSIsInZhbHVlIjoiaEZoUkNhMVBsVEwvOEtTY011R1hOTXo4cFVOeG16VmwvTHZKU1BjR3Nhd2ZRL2F3aGNncU0wQkNZRTUxWU1aT2wxK3B1WlNRV0dWNnRpZXBBcTFWVlBFZWNDM05YSGZETndsbldocTYyZnIzWElTUGpFN3VnYXVwUVdCZVVLUzAiLCJtYWMiOiJkMTYyMzA1OTU5MDgyYjAxY2ZlZmQ3MTc4NjExZTQ5NmRhZmM0YzQyOWRkM2IzODc2YmMwMjQzOGM5M2VmOGI1IiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6Ilk2U1BuVmZaTjZ6QVZ4dGNwRGlwdVE9PSIsInZhbHVlIjoid1MzOVUreFhkRjd6a0dpam9iUFpFVXlBVVYybEVsT04waUUrK2pvRWE5UjBKVEd3cVZ3aTVRSnNHSkdJYmJuVEQyQldJQS8rb1NvdnVVcnZleW8xQ0VHUVkrY0Q5QjIxVk5ySUFXbjVRK1pDRC83aER2ZndjcVVObnpFV0dxZVkiLCJtYWMiOiI0MTZhNWIyMTg3ZWRlNzE5M2RiZDk5MTZhMDgyODlhMWY1Mjk2NTg1NDlhYjU1YTFjMTAwMjRmYTRjYjVjNmI5IiwidGFnIjoiIn0%3D',
  'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'none',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
  'Referer': 'https://animepahe.ru/',
  'Origin': 'https://animepahe.ru',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
  'referer': 'https://animepahe.ru/',
  'x-requested-with': 'XMLHttpRequest',
  'Content-Type': 'text/plain;charset=UTF-8'
}
def animepache():
  response = requests.request("GET", URL, headers=headers, data=payload).json()
  anime_list = []
  anime_dict = {}
  for i in response["data"]:
      title = i["anime_title"]
      episode = i["episode"]
      anime_session = i["anime_session"]
      session = i["session"]
      link = f"{domain_url}{anime_session}/{session}"
      anime_list.append([title, episode, link])
      anime_dict = {URL: anime_list}
  return anime_dict

