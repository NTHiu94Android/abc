from playwright.sync_api import sync_playwright

class AutobotScraper2:
    def scrape2(url):
        with sync_playwright() as p:
            # Khởi chạy trình duyệt Chromium
            browser = p.chromium.launch(headless=False)  # headless=False để hiển thị trình duyệt
            page = browser.new_page()
            found_link = None

            # Bắt sự kiện request để tìm link .m3u8
            def handle_request(request):
                nonlocal found_link
                if ".m3u8" in request.url and not found_link:
                    found_link = request.url

            page.on("request", handle_request)

            # Truy cập trang web
            page.goto(url, wait_until="networkidle")

            # Tự động click vào nút Play (nếu có)
            try:
                page.click('.jw-icon.jw-icon-display', timeout=3000)
            except Exception as e:
                print("Không tìm thấy nút Play:", e)

            # Đợi 5 giây để bắt request
            page.wait_for_timeout(5000)

            # Đóng trình duyệt
            browser.close()
            # Trả về link .m3u8
            return found_link