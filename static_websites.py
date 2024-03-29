from bs4 import BeautifulSoup
import requests

urls = {
    #"https://www.animeonsen.xyz/": ["span"], #403 error
    #"https://aniwatch.to/home": [], #403 error
    #"https://aniwave.to/home": [], #automaticly redirects
    #"https://anix.to/home": [], #automaticly redirects
    #"https://www.wcostream.tv/": ["div", "recent-release-episodes"], #none

    "https://yugenanime.tv/": [["a", "ep-title"], ["a", "ep-title"]],
    "https://animeowl.us/": [["h3", "anime-title"], ["a", "title-link"]],
    "https://allmanga.to/anime/": [["div", "card-header"], ["a", "btn-hv-link"]],
    "https://animeheaven.me/": [["a", "c"], ["a", "c"]],
}

def staticwebsites():

    animes_dict = {}
    for key,values in urls.items():

        r = requests.get(key)
        soup = BeautifulSoup(r.text, 'html5lib')
        anime_list = []

        for title, link in zip((soup.find_all(values[0][0], class_=values[0][1])), (soup.find_all(values[1][0], class_=values[1][1]))):
            anime_list.append([title.text, f"{key}{link['href']}"])

        animes_dict[key] = anime_list
    return animes_dict