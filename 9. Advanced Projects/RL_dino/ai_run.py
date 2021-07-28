import gym,gym_dino
import numpy as np
from main import stack_frames,stacked_frames
from tensorflow import keras
state_size=[20,50,4]
v=keras.models.load_model("vidw_model.h5")
env=gym.make("DinoGame-v0")
for episode in range(10):
    state=env.reset()
    state,stacked_frames=stack_frames(stacked_frames, state, True)

    done=False
    while not done:
        state = state.reshape((1, *state_size))
        Q_v=v.predict(state)
        action=np.argmax(Q_v)
        next_state,reward,done,_=env.step(action)
        next_state, stacked_frames = stack_frames(stacked_frames, next_state, False)
        state=next_state
