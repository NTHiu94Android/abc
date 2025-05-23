from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver

# Cao danh sách các tran dau bong da tu trang web http://5goal.vip/xem-lai/bong-da
class AutobotScraper3:
    def __init__(self, base_url=None):
        if base_url:
            self.base_url = base_url
        
    def scrape30(self):
        """Cào dữ liệu từ trang chủ."""
        driver = webdriver.Chrome()
        driver.get(self.base_url)
        try:
            # Wait for page to load
            sleep(2)
            # Click on the second tab using Selenium
            tab = driver.find_element('css selector', 'div.tabsSwitch:nth-child(2)')
            tab.click()
            # Wait for content to load after click
            sleep(5)
            # Now parse the updated page content
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            matchs = []
            # Tìm tất cả các phần tử div có class 'home-replay-item'
            match_divs = soup.find_all('div', class_='home-replay-item')
            for match_div in match_divs:
                # Tìm thông tin trận đấu
                match_info = match_div.find('div', class_='home-replay-item-league').text.strip()
                # Tìm thông tin đội nhà và đội khách
                home_team = match_div.find('div', class_='home-replay-item-club-name').text.strip()
                away_team = match_div.find_all('div', class_='home-replay-item-club-name')[1].text.strip()
                # Tìm thông tin kết quả trận đấu
                score = match_div.find('div', class_='home-replay-item-score-ht').text.strip()
                # Tìm thông tin người phát trực tiếp
                commentator = match_div.find('div', class_='home-replay-item-commentator').text.strip()
                # Tìm link xem lại
                link = match_div.find('a')['href']
                # Tạo đối tượng trận đấu
                match = {
                    'match_info': match_info,
                    'home_team': home_team,
                    'away_team': away_team,
                    'score': score,
                    'commentator': commentator,
                    'link': "http://5goal.vip" + link   
                }
                # Thêm đối tượng trận đấu vào danh sách
                matchs.append(match)
            return matchs
        except Exception as e:
            print(f"Error: {e}")
            return []
        finally:
            driver.quit()