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
#        print("test")
        bot = self.bot
        bot.get("https://twitter.com/")
        bot.maximize_window()
        time.sleep(6)
        email    = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(4)
        
    def like_tweet(self, hastag):
        bot = self.bot
        bot.get('https://twitter.com/search?q=' + hastag + '&src=typeahead_click')
        time.sleep(5)
        for i in range(1, 2):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(2)
            tweets = bot.find_element_by_class_name('css-1dbjc4n')
#            links = [elem.get_attribute('data-permalink-path') for elem in tweets]
            print(tweets.get_property('attributes')[0])
        
    
def Main():
    ed = TwitterBot("duggaltanvir@gmail.com", "Coolmaster@008")
    ed.login()
    ed.like_tweet("webdevelopment")
    
if __name__ == '__main__':
    Main()