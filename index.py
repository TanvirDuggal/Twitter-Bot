# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 13:08:56 2019

@author: Tanvir.Duggal
"""

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time


class TwitterBot():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot      = webdriver.Chrome()
    
    def login(self):
        bot = self.bot
        bot.get("https://twitter.com/login")
        bot.maximize_window()
        time.sleep(6)
        email    = bot.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
        password = bot.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')
            
        email.clear()
        password.clear()
        
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(2)
        
    def like_tweet(self, hastag):
        bot = self.bot
        bot.get('https://twitter.com/search?q=' + hastag + '&src=typeahead_click')
        time.sleep(3)
#        for i in range(1, 2):
        bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(2)
        tweets = bot.find_element_by_class_name("css-1dbjc4n")
        print(tweets)
        print(tweets)
        tweets.click()
        print("here")
        time.sleep(4)
        likeTag = bot.find_element_by_class_name("r-4qtqp9")
        print(likeTag)
        print(bot.current_url)
        likeTag.click()
#            links = [i.get_attribute('href') for i in tweets]
#            
#            for link in links:
#                if str(link) == None or str(link) == "None":
#                    pass
#                else:
#                    lin = str(link)
#                    print(lin)
#                    bot.get(lin)
#                    try:
#                        bot.find_element_by_class_name('HeartAnimation').click()
#                        time.sleep(8)
#                    except:
#                        time.sleep(6)
#                print(">>>> ", i.find_elements_by_class_name("css-4rbku5"))
#                links = [elem.get_attribute('a') for elem in tweets]
    #            print(tweets.get_property('attributes')[0])
#                print(links)
        
    
def Main():
    ed = TwitterBot("duggaltanvir@gmail.com", "Coolmaster@008")
    ed.login()
    ed.like_tweet("webdevelopment")
    
if __name__ == '__main__':
    Main()