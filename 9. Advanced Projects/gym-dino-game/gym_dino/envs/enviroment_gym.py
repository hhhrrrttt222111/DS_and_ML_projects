import numpy as np
from gym_dino.game import DINO
import gym
from gym import error, spaces, utils


import base64
import os
from PIL import Image
import io




class enviroment(gym.Env):

    def __init__(self, render ,accelerate, autoscale):
        self.game=DINO(render,accelerate)
        self.observation_space=spaces.Box(low=0,high=255, shape=(150,600,3),dtype=np.uint8)
        self.action_space=spaces.Discrete(2)
        self.crashed =-100
        self.running=0.1
        self.current_frame=self.observation_space.low
        self.action_set=[0,1]

    def get_score(self):
        return self.game.score()
    def step(self,action):


        if action== 1:
            self.game.press_up()

        observation=self.screen()

        if self.game.crash():
            reward=(self.crashed)*(11.0/self.get_score())

            done=True
        else:
            reward=( self.get_score())/10
            done=False

        info={}
        return observation, reward, done,info
    def reset(self ,record=False):
        self.game.restart()
        return self.screen()

    def screen(self):
        s= self.game.get_canvas()#retruns a base64 encoded pic
        i=io.BytesIO(base64.b64decode(s))
        l=Image.open(i)
        bg = Image.new("RGB", l.size, (255, 255, 255))  # fill background as white color
        bg.paste(l, mask=l.split()[3])  # 3 is the alpha channel
        k=bg
        a=np.array(k)
        self.current_frame=a
        return self.current_frame

    def close(self):
        self.game.close()

    def set_acceleration(self, enable):
        if enable:
            self.game.restore_parameter('config.ACCELERATION')
        else:
            self.game.set_parameter('config.ACCELERATION', 0)
