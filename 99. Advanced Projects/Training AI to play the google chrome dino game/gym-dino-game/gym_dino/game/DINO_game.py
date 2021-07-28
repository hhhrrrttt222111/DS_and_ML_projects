from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from io import BytesIO
import base64
import numpy as np
from PIL import Image
import os
import time
from gym_dino.utils.chromedriver_installer import get_chromiumdrive
class DINO:
    def __init__(self, render=False
                 ,accelerate=False, autoscale=False):
        if not os.path.exists('chromedriver') and not os.path.exists('chromedriver.exe'):
            get_chromiumdrive()

        chrome_driver_path = "./chromedriver"
        url = 'https://elvisyjlin.github.io/t-rex-runner/'
        self.url = url
        chrome_options = Options()
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_argument("--mute-audio")
        chrome_options.add_argument('--no-sandbox')
        if not render:
            chrome_options.add_argument("--headless")
        self._driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_options)
        self._driver.set_window_position(x=-10, y=0)
        self._driver.set_window_size(200, 300)
        self._driver.get(url)
        self.defaults = self.get_parameters()  # default parameters

        if not accelerate:
            self.set_parameter('config.ACCELERATION', 0)
        if not autoscale:
            self._driver.execute_script('Runner.instance_.setArcadeModeContainerScale = function(){};')
        self.press_space()
    def get_parameters(self):
        params = {}
        params['config.ACCELERATION'] = self._driver.execute_script('return Runner.config.ACCELERATION;')
        return params

    def set_parameter(self, key, value):
        self._driver.execute_script('Runner.{} = {};'.format(key, value))

    def press_up(self):
        self._driver.find_element_by_tag_name("body").send_keys(Keys.ARROW_UP)

    def press_down(self):
        self._driver.find_element_by_tag_name("body").send_keys(Keys.ARROW_DOWN)

    def press_space(self):
        self._driver.find_element_by_tag_name("body").send_keys(Keys.SPACE)

    def crash(self):
        return self._driver.execute_script("return Runner.instance_.crashed;")

    def playing(self):
        return self._driver.execute_script("return Runner.instance_.playing;")

    def score(self):
        reward_score = self._driver.execute_script("return Runner.instance_.distanceMeter.digits;")
        score = ''.join(reward_score)
        return int(score)

    def pause(self):
        return self._driver.execute_script("return Runner.instance_.stop();")

    def resume(self):
        return self._driver.execute_script("return Runner.instance_.play();")

    def end(self):
        self._driver.close()

    def restart(self):
        self._driver.execute_script("Runner.instance_.restart();")
        time.sleep(0.25)

    def get_canvas(self):
        return self._driver.execute_script(
            'return document.getElementsByClassName("runner-canvas")[0].toDataURL().substring(22);')
