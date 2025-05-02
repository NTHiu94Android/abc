import requests
import re
from bs4 import BeautifulSoup

# Cao danh sach phim tu trang web motphim.dk
class AutobotScraper0:
    def __init__(self, base_url=None):
        if base_url:
            self.base_url = base_url

    def scrape00(self):
        """Cào dữ liệu từ trang chủ."""
        # Gửi yêu cầu HTTP để tải nội dung trang web
        response = requests.get(self.base_url)
        if response.status_code == 200:
            # Phân tích cú pháp HTML bằng BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            # Ví dụ: Lấy danh sách phim
            movies = []
            for item in soup.find_all('div', class_='myui-vodlist__box'):  # Thay đổi selector tùy theo cấu trúc HTML
                title = item.find('h4').text.strip() if item.find('h4') else "Không có tiêu đề"
                link = item.find('a')['href'] if item.find('a') else "#"
                image_url = item.find('a')['style'].split('url(')[1].split(')')[0] if item.find('a') else "#"
                movies.append({
                    "title": title, 
                    "link": link, 
                    "thumbnail": "https://motphim.se/" + image_url
                })
            return movies
        else:
            print(f"Không thể truy cập trang web. Mã lỗi: {response.status_code}")
            return []
        
    def scrape01(self, from_page, to_pages):
        all_movies = []  # Lưu trữ tất cả các phim từ các trang

        for page in range(from_page, to_pages + 1):
            # Tạo URL động cho từng trang
            if page == 1:
                url = self.base_url
            else:
                url = f"{self.base_url}?page={page}"

            # Tạo đối tượng scraper và lấy danh sách phim
            scraper = AutobotScraper0(base_url=url)
            movies = scraper.scrape00()

            # Kiểm tra xem có phim nào không
            if not movies:
                print(f"Không tìm thấy phim ở trang {page}. Dừng lại.")
                break

            # Thêm danh sách phim vào all_movies
            all_movies.extend(movies)
            print(f"Đã lấy {len(movies)} phim từ trang {page}")

        return all_movies