from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
import re
env = gym_super_mario_bros.make('SuperMarioBros-v0')
env = JoypadSpace(env, SIMPLE_MOVEMENT)

f = "C:/Users/Jack He/Desktop/474project/m500k.txt"
with open(f) as file:
    s = file.read()
actions = [int(i) for i in re.findall(r"\d+", s)]


done = True
for step in actions:
    if done:
        state = env.reset()
    state, reward, done, info = env.step(step)
    env.render()

env.close()
