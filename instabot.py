from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tkinter import *
import time

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(self.password)
        password_elem.send_keys(Keys.RETURN)
        time.sleep(2)

    def likePhoto(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

            hrefs = driver.find_elements_by_tag_name('a')
            pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
            pic_hrefs = [href for href in pic_hrefs if hashtag in href]
            print(hashtag + ' photos: ' + str(len(pic_hrefs)))

            for pic_href in pic_hrefs:
                driver.get(pic_href)
                driver.execute_script("window.scrollTo(0, document.body.scroll.Height);")
                try:
                    driver.find_element_by_link_text("Like").click()
                    time.sleep(18)
                except Exception as e:
                    time.sleep(2)

    def unFollow(self):
        driver = self.driver
        driver.get("https://www.instagram.com/" + self.username + "/")
        time.sleep(2)
        varpath = "//a[@href=\"/" + self.username + "/following/\"]"
        driver.find_element(By.XPATH, varpath).click()
        time.sleep(2)
        while True:
            driver.find_element(By.XPATH, '//button[text()="Following"]').click()
            driver.find_element(By.XPATH, '//button[text()="Unfollow"]').click()
            time.sleep(1)

    def Follow(self):
        driver = self.driver
        driver.get("https://www.instagram.com/mairovergara/")
        time.sleep(2)
        varpath = "//a[@href=\'/mairovergara/followers/\']"
        driver.find_element(By.XPATH, varpath).click()
        time.sleep(2)
        while True:
            driver.find_element(By.XPATH, '//*[@class=\'PZuss\']//*[text()=\'Follow\']').click()
            time.sleep(1)

window = Tk() # INIT TKINTER WINDOW

def tkFollow():
    tkUsername = inputName.get()
    tkPassword = inputPassword.get()

    user = InstagramBot(tkUsername, tkPassword)
    user.login()
    user.Follow()

def tkUnFollow():
    tkUsername = inputName.get()
    tkPassword = inputPassword.get()

    user = InstagramBot(tkUsername, tkPassword)
    user.login()
    user.unFollow()

def tkLikePhoto():
    tkUsername = inputName.get()
    tkPassword = inputPassword.get()

    user = InstagramBot(tkUsername, tkPassword)
    user.login()

    hashtags = ['sony', 'tech', 'games', 'consoles']
    [user.likePhoto(tag) for tag in hashtags]

lb1 = Label(window, text="username:")
lb1.place(x=20,y=20)
inputName = Entry(window) # USERNAME INPUT
inputName.place(x=20, y=40)

lb2 = Label(window, text="password:")
lb2.place(x=20,y=60)
inputPassword = Entry(window) # PASSWORD INPUT
inputPassword.place(x=20, y=80)
bt1 = Button(window, text="Like Photos", command=tkLikePhoto)
bt1.place(x=20, y=120)
bt2 = Button(window, text="Follow", command=tkFollow)
bt2.place(x=20, y=150)
bt3 = Button(window, text="Unfollow", command=tkUnFollow)
bt3.place(x=20, y=180)


window.geometry("200x220+300+300")
window.mainloop()
