import animepache_website
import static_websites
import kaas_website
#current websites:
    #https://kaas.to/ #api
    #https://animepahe.ru/ #api
    #https://yugenanime.tv/ #static
    #https://animeowl.us/" #static
    #https://allmanga.to/anime/ #static
    #https://animeheaven.me/ #static

animepach_dict = animepache_website.animepache()
static_websites_dict = static_websites.staticwebsites()
kaas_dict = kaas_website.kaas()


def merge_dicts(*args):
    main_dict = {}
    for i in args:
        main_dict.update(i)
    return main_dict

main_dict = merge_dicts(animepach_dict, static_websites_dict, kaas_dict)

def main(dict):
    for key, values in dict.items():
        print(key)
        for value in values:
            print(value)
        print("---------------")
    
if __name__ == "__main__":
    main(main_dict)