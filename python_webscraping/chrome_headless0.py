# -*- coding: utf_8 -*-
from time import sleep
import sys
import io
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

options = Options()
# ヘッドレスモードを有効にする（次の行をコメントアウトすると画面が表示される）。
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
# ChromeのWebDriverオブジェクトを作成する。
driver = webdriver.Chrome(chrome_options=options)

# Googleのトップ画面を開く。
driver.get('https://www.google.co.jp/')

# 検索語として「selenium」と入力し、Enterキーを押す。
driver.find_element_by_id("lst-ib").send_keys("selenium")
driver.find_element_by_id("lst-ib").send_keys(Keys.ENTER)
# タイトルに「Selenium - Web Browser Automation」と一致するリンクをクリックする。
# なぜか触れないのでスクロール。
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.find_element_by_link_text("Selenium - Web Browser Automation").click()
# 5秒間待機してみる。
#sleep(5)

# 証拠のスクリーンショットを撮る。
driver.save_screenshot('search_results_ebi.png')

# スクレイピング
elm = driver.find_element_by_xpath('//*[@id="mainContent"]/p[1]')
print(elm.text)

driver.quit()  # ブラウザーを終了する。
