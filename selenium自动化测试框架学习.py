from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# 浏览器后台运行
opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disable-gpu")
# 允许自动化测试，chrome的版本大于等于88
# option.add_experimental_option('excludeSwitches', ['enable-automation'])
opt.add_argument('--disable-blink-features=AutomationControlled')

web = Chrome(options=opt)

web.get("https://juejin.cn/android")
s_el = web.find_element_by_xpath('//*[@id="juejin"]/div[1]/div/header/div/nav/ul/li[2]/ul/li[1]/form/input').send_keys('flutter', Keys.ENTER)

time.sleep(1)

list_el = web.find_element_by_xpath('//*[@id="juejin"]/div[1]/main/div/div/div/div/ul')
list_li = list_el.find_elements_by_xpath('./li/div/a/object/div/div/div[2]/a/span')
for li in list_li:
    print(li.text)

list_li[0].click()
time.sleep(1)
# 切换到打开窗口
web.switch_to.window(web.window_handles[-1])
lst_p = web.find_elements_by_xpath('//*[@id="juejin"]/div[1]/main/div/div[1]/article/div[4]/div/p')
for p in lst_p:
    print(p.text)
web.close()
# 回到原来窗口
web.switch_to.window(web.window_handles[0])
web.close()



