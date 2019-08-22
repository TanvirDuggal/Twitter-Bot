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
        print("test")
        bot = self.bot
        bot.get("https://twitter.com/")
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
        bot.get('')
    
def Main():
    ed = TwitterBot("duggaltanvir@gmail.com", "Coolmaster@008")
    ed.login()
    
if __name__ == '__main__':
    Main()