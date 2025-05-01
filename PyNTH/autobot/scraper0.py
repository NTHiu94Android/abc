import requests
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
                image_url = ""
                a_tag = soup.find('a', class_='myui-vodlist__thumb')
                if a_tag:
                    # Lấy giá trị của thuộc tính style
                    style = a_tag.get('style')

                    # Tách chuỗi để lấy đường dẫn hình ảnh
                    if style and 'background: url(' in style:
                        # Lấy phần chuỗi bên trong dấu ngoặc đơn
                        start_index = style.find('background: url(') + len('background: url(')
                        end_index = style.find(')', start_index)
                        image_url = style[start_index:end_index]
                        # In đường dẫn hình ảnh
                        # print("Đường dẫn hình ảnh:", image_url)
                    else:
                        print("Không tìm thấy đường dẫn hình ảnh trong thuộc tính style.")
                else:
                    print("Không tìm thấy thẻ <a> với class 'myui-vodlist__thumb'.")
                movies.append({
                    "title": title, 
                    "link": link, 
                    "thumbnail": "https://motphim.se/" + image_url
                })

            return movies
        else:
            print(f"Không thể truy cập trang web. Mã lỗi: {response.status_code}")
            return []
        
    def scrape01(self, max_pages):
        all_movies = []  # Lưu trữ tất cả các phim từ các trang

        for page in range(1, max_pages + 1):
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