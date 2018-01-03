from selenium import webdriver
browser = webdriver.PhantomJS()
url = 'https://www.baidu.com'
browser.get(url)
browser.implicitly_wait(3)  #implictly_wait函数则完美解决了这个问题，给他一个时间参数，他会只能等待，当js完全解释完毕就会自动执行下一步
