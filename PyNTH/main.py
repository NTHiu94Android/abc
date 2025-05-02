from math import e
from os import name
import json
from autobot.scraper0 import AutobotScraper0
from autobot.scraper1 import AutobotScraper1
from autobot.scraper2 import AutobotScraper2
from autobot.savedata import save_movies, save_espisodes, save_movies_first, save_to_db

def main():
    # ------------------------------------------------------------------------------------------
    # movies = AutobotScraper0(base_url="https://motphim.se/danh-sach/phim-moi").scrape01(1,15)
    # save_movies(movies, "movies.json")
    # print(f"Tìm thấy {len(movies)} phim.")

    # -----------------------------------------------------------------------------------------
    moviesFirst = AutobotScraper0(base_url="https://motphim.se/danh-sach/phim-le").scrape01(21,25)
    save_movies_first(moviesFirst, "moviesFirst.json")
    print(f"Tìm thấy {len(moviesFirst)} phim.")

    # -----------------------------------------------------------------------------------------
    # episodes = AutobotScraper1(base_url="https://motphim.se/phim/tu-cam/tap-1").scrape1()
    # save_espisodes(episodes, "episode.json")
    # print(f"Tìm thấy {len(episodes)} tập phim.")

    # -----------------------------------------------------------------------------------------
    # Lấy link m3u8 từ trang phim
    # link = AutobotScraper2.scrape2("https://motphim.se/phim/ninh-an-nhu-mong/tap-full")
    # print("🎯 Link .m3u8:", link)

    # ------------------------------------------------------
    # Quet danh sach phim le tu  file moviesFirst.json
    # moviesFirst = [];
    # with open('moviesFirst.json', 'r', encoding='utf-8') as file:
    #     moviesFirst = json.load(file)
    # episodes = []
    # for movie in moviesFirst:
    #     name = "Tập full"
    #     link = AutobotScraper2.scrape2(movie["link"] + "/tap-full")
    #     vip_yn = "N"
    #     episodes.append({
    #         "title": movie["title"],
    #         "name": name,
    #         "link": link,
    #         "thumbnail": movie["thumbnail"],
    #         "vip_yn": vip_yn 
    #     })
    # save_to_db(episodes);
    # ------------------------------------------------------



    # ------------------------------------------------------
    # moviesFirst = [];
    # with open('moviesFirst.json', 'r', encoding='utf-8') as file:
    #     moviesFirst = json.load(file)
    # moviesFirstDB = [];
    # with open('moviesFirstDB.json', 'r', encoding='utf-8') as file:
    #     moviesFirstDB = json.load(file)
    # for movie in moviesFirst:
    #     for movieDB in moviesFirstDB:
    #         if movie["title"] == movieDB["title"]:
    #             movieDB["thumbnail"] = movie["thumbnail"]
    #             break
    # save_to_db(moviesFirstDB, "moviesFirstDB.json")
    # ------------------------------------------------------
    
    
    # Lưu dữ liệu vào file CSV
    # save_to_csv(movies, "movies.csv")
    # save_to_csv(episodes, "episodes.csv")

if __name__ == "__main__":
    main()