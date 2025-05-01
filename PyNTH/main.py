from autobot.scraper0 import AutobotScraper0
from autobot.scraper1 import AutobotScraper1
from autobot.scraper2 import AutobotScraper2
from autobot.savedata import save_movies, save_espisodes

def main():
    movies = AutobotScraper0(base_url="https://motphim.se/danh-sach/phim-moi").scrape01(5)
    episodes = AutobotScraper1(base_url="https://motphim.se/phim/tu-cam/tap-1").scrape1()
    # Lấy link m3u8 từ trang phim
    # link = AutobotScraper2.scrape2("https://motphim.se/phim/ninh-an-nhu-mong/tap-2")
    # print("🎯 Link .m3u8:", link)
    print(f"Tìm thấy {len(movies)} phim.")
    print(f"Tìm thấy {len(episodes)} tập phim.")
     # Lưu dữ liệu vào file JSON
    save_movies(movies, "movies.json")
    save_espisodes(episodes, "episode.json")
    # Lưu dữ liệu vào file CSV
    # save_to_csv(movies, "movies.csv")
    # save_to_csv(episodes, "episodes.csv")

if __name__ == "__main__":
    main()