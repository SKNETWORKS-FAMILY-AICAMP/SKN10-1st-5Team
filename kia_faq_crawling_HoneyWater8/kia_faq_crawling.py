from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import pandas as pd

# ChromeDriver는 본인이 다운로드 해야함.
driver_path = "chromedriver.exe"

# 웹 드라이버 설정
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# kia의 FaQ 페이지 링크
url = "https://www.kia.com/kr/customer-service/center/faq"
driver.get(url)

# 페이지가 로드될 때까지 대기
time.sleep(5)

# 빈 데이터프레임 생성 -> 나중에 한 row씩 추가됨.
columns = ["Category", "Question", "Answer"]
df = pd.DataFrame(columns=columns)

# 버튼 클릭 후 페이지 내용이 바뀌는 시간을 기다리기위해 2초 설정
wait = WebDriverWait(driver, 2)

# 메뉴 버튼 찾기
menus = driver.find_elements(By.CLASS_NAME, 'tabs__btn')

# kia FaQ의 메뉴는
# Top 10, 전체, 차량 구매, 차량 정비, 기아멤버스, 홈페이지, PBV, 기타
# 총 8개임.
for menu in menus:
    # 메뉴 선택
    driver.execute_script("arguments[0].click();", menu)
    
    # 페이지가 업데이트 될 때까지 대기 (2초)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'faqinner__wrap')))  # faqinner__wrap 클래스가 로드될 때까지 기다림
    time.sleep(5)  # 혹시 몰라서 5초 더 대기, kia FaQ 메뉴 바뀌는 속도 느림.

    # 메뉴마다 페이지가 여러개 일 수 있으므로 마지막 페이지 까지 반복복
    while True:
        # 현재 활성화된 페이지 번호 추적
        current_page = int(driver.find_element(By.CSS_SELECTOR, '.paging-list li.is-active a').text)

        # 페이지 업데이트 후 새로운 HTML 가져오기
        html_content = driver.page_source

        # BeautifulSoup 객체 생성
        soup = BeautifulSoup(html_content, 'html.parser')

        # 새로운 내용을 받아오기 위해 다시 div 요소 찾기
        description_divs = soup.find_all('div', class_='faqinner__wrap')
        i = 0   # 질문의 ID값을 올리는 변수
        for description_div in description_divs:
            # data-link-label에 질문이 담겨있음. -> 뽑아야 됨.
            question_button = driver.find_element(By.ID, f'accordion-item-{i}-button')
            question = question_button.get_attribute('data-link-label')
            
            # 여러줄의 description을 하나의 문자열로 저장
            p_tags = description_div.find_all('p')
            description_text = ""
            for p in p_tags:
                description_text += p.get_text(strip=True) + "\n"
            # 데이터프레임에 row 추가
            df = pd.concat([df, pd.DataFrame({
                "Category": [menu.text],
                "Question": [question],
                "Answer": [description_text]
            })], ignore_index=True)
            i += 1
        try:
            # 다음 페이지 번호 선택 (현재 페이지 이후의 활성화되지 않은 페이지 중 첫 번째)
            next_page = driver.find_element(By.XPATH, f'//ul[@class="paging-list"]/li[a[text()="{current_page + 1}"]]/a')
            driver.execute_script("arguments[0].click();", next_page)
            time.sleep(3)  # 페이지가 바뀌도록 대기
        except Exception:   # 마지막 페이지 였다면 다음 메뉴로 넘어가기위해 break
            print(f"No more pages in category: {menu.text}")
            break

driver.quit()

df.to_csv("kia_faq.csv", index=False, encoding="utf-8")