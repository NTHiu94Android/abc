from math import e
from os import name
import json
from autobot.scraper3 import AutobotScraper3
from autobot.scraper0 import AutobotScraper0
from autobot.scraper1 import AutobotScraper1
from autobot.scraper2 import AutobotScraper2
from autobot.savedata import save_movies, save_espisodes, save_movies_first, save_to_db, save_matchs

def main():
    # ------------------------------------------------------------------------------------------
    # movies = AutobotScraper0(base_url="https://motphim.se/danh-sach/phim-moi").scrape01(1,15)
    # save_movies(movies, "movies.json")
    # print(f"Tìm thấy {len(movies)} phim.")

    # -----------------------------------------------------------------------------------------
    # moviesFirst = AutobotScraper0(base_url="https://motphim.se/danh-sach/phim-le").scrape01(21,25)
    # save_movies_first(moviesFirst, "moviesFirst.json")
    # print(f"Tìm thấy {len(moviesFirst)} phim.")

    # -----------------------------------------------------------------------------------------
    # episodes = AutobotScraper1(base_url="https://motphim.se/phim/tu-cam/tap-1").scrape1()
    # save_espisodes(episodes, "episode.json")
    # print(f"Tìm thấy {len(episodes)} tập phim.")

    # -----------------------------------------------------------------------------------------
    matchs = AutobotScraper3(base_url="http://5goal.vip/xem-lai/bong-da").scrape30()
    # https://bongdalivetv.pro/xem-lai-tran-dau/
    # matchs = AutobotScraper3(base_url="https://bongdalivetv.pro/xem-lai-tran-dau/").scrape30()
    save_matchs(matchs, "matchs.json")
    print(f"Tìm thấy {len(matchs)} tran dau.")

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

    # moviesFirstDB = [];
    # with open('moviesFirstDB.json', 'r', encoding='utf-8') as file:
    #     moviesFirstDB = json.load(file)
    # # Them truong type_mv_code = "MV04002" vao moviesFirstDB
    # for movie in moviesFirstDB:
    #     movie["type_mv_code"] = "MV04002"
    #     movie["release_code"] = "MV06001"
    #     movie["pay_code"] = "MV05002"
    # save_to_db(moviesFirstDB);


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


    # for item in soup.find_all('a', class_='replayItem'):
    #     # Extract data from each item
    #     match_data = {}
    #     # Extract league and time
    #     match_data['league_time'] = item.select_one('.matchTime').text.strip()
    #     # cat chuoi 22/05/2025 09:30:00 thành 22/05/2025 và 09:30:00
    #     match_data['time'] = match_data['league_time'].split(' ')[1]
    #     match_data['league'] = match_data['league_time'].split(' ')[0]
    #     # Extract link
    #     match_data['link'] = item['href']
    #     # Extract teams and logos
    #     teams = item.select('.teamA, .teamB')
    #     match_data['team1'] = {
    #         'name': teams[0].select_one('div').text.strip(),
    #         'logo': teams[0].select_one('img')['data-src']
    #     }
    #     match_data['team2'] = {
    #         'name': teams[1].select_one('div').text.strip(),
    #         'logo': teams[1].select_one('img')['data-src']
    #     }
    #     # Extract play button
    #     match_data['play_button'] = item.select_one('.playBtn').text.strip()
    #     # Append match data to the list
    #     matchs.append(match_data)

if __name__ == "__main__":
    main()