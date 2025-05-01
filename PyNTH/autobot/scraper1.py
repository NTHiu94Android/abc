import requests
from bs4 import BeautifulSoup

# Cao danh sách các tập phim từ trang web motphim.se
class AutobotScraper1:
    def __init__(self, base_url=None):
        if base_url:
            self.base_url = base_url

    def fetch_page(self, url):
        """Tải nội dung trang web."""
        response = requests.get(url)
        episode_list = []
        if response.status_code == 200:
            # Phân tích cú pháp HTML bằng BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            # Tìm thẻ <ul> chứa danh sách các tập phim
            tab_pane = soup.find('ul', class_='myui-content__list')
            if tab_pane:
                # Tìm tất cả các thẻ <a> trong danh sách
                episodes = tab_pane.find_all('a', class_='btn btn-default')
                # Lưu thông tin tập phim vào danh sách
                for episode in episodes:
                    episode_title = episode.get('title')  # Lấy tiêu đề tập phim
                    episode_link = episode.get('href')    # Lấy link tập phim
                    episode_list.append({
                        "title": "Tập " + episode_title,
                        "link": episode_link
                    })
            else:
                print("Không tìm thấy danh sách tập phim.")
        else:
            print(f"Không thể truy cập trang web. Mã lỗi: {response.status_code}")
        return episode_list

    def scrape1(self):
        # return self.fetch_page(self.base_url)
        return self.fetch_page(self.base_url)