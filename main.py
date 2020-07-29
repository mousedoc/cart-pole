import gym
import random

env = gym.make('CartPole-v1')
goal_steps = 100

def test_play():
    obs = env.reset()

    for i in range(goal_steps):
        obs, reward, done, info = env.step(random.randrange(0, 2))

        if done:
            break
        
        env.render()




# N : CartPole을 실행해 볼 횟수
# K : 그 중에 뽑을 데이터의 갯수
# f : CartPole을 어떤식으로 동작시킬 지 결정하는 함수.
def data_preparation(N, K, f, render = False):
    game_data = []

    for i in range(N):
        score = 0
        game_steps = []
        obs = env.reset()

        for step in range(goal_steps):
            if render:
                env.render()

            action = f(obs)
            game_steps.append((obs, action))        

            obs, reward, done, info = env.step(action)
            score += reward

            if done:
                break

        game_data.append((score, game_steps))

    # -score로 정렬
    game_data.sort(key = lambda element: -element[0])

    training_set = []
    
    for i in range(K):
        for step in game_data[i][1]:                        # game_steps
            if step[1] == 0:
                training_set.append((step[0], [1, 0]))      # 상황, [Left 확률로 0, Right 확률로 1]
            else:
                training_set.append((step[0], [0, 1]))

    print("{0}/{1}th score : {2}".format(K, N, game_data[K - 1][0]))
    
    if render:
        for i in game_data:
            print("Score : {0}".format(i[0]))

    return training_set


if __name__ == '__main__':

    training_set = data_preparation(1000, 50, lambda action : random.randrange(0, 2), True)

