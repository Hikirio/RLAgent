import gym

env = gym.make('CartPole-v1')
observation = env.reset()
observation_space = env.observation_space.shape[0]
action_space = env.action_space.n
points = 0
highscore = 0

for _ in range(10000):
    env.render()
action = 1 if observation[2] > 0 else 0

# action = env.action_space.sample()
observation, reward, done, info = env.step(action)
points += reward
if done:
    print('{}:done - {}'.format(_, reward))
if points > highscore:
    highscore = points
# break

observation = env.reset()
Points = 10
print(highscore)
env.close()

# import gym
#
# env = gym.make('CartPole-v1')
# env.reset()
# for _ in range(10000):
#     env.render()
#     env.step(env.action_space)  # take a random action
#
# env.close()
