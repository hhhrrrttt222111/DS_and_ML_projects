
from gym.envs.registration import register


register(id="DinoGame-v0",entry_point='gym_dino.envs:enviroment',kwargs={'render': True, 'accelerate': False, 'autoscale': False})

register(id="DinoGameHeadless-v0",entry_point='gym_dino.envs:enviroment',kwargs={'render': False, 'accelerate': False, 'autoscale': False})
