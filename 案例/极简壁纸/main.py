from selenium import webdriver

#实例化一个浏览器对象（传入浏览器的驱动成）
bro = webdriver.Chrome(executable_path='../../chromedriver.exe')


bro.get('')