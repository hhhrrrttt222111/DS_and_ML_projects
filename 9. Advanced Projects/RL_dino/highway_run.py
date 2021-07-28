import gym,highway_env
import numpy as np
from highway_env_2 import stack_frames,stacked_frames
from tensorflow import keras
state_size = [5,5,4]
v=keras.models.load_model("/home/anwesan/PycharmProjects/pythonProject/vw_model.h5") # the path tp my stored model . Pls do change this according to your system
env=gym.make("highway-v0")
for episode in range(10):
    state = env.reset()
    state,stacked_frames = stack_frames(stacked_frames, state, True)
    done=False
    while not done:
        state = state.reshape((1, *state_size))
        Q_v=v.predict(state)
        action=np.argmax(Q_v)
        next_state,reward,done,_=env.step(action)
        env.render()
        next_state, stacked_frames = stack_frames(stacked_frames, next_state, False)
        state=next_state
