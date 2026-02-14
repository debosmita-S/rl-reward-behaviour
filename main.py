import numpy as np
import random

SIZE = 6
GOAL = (5,5)

ACTIONS = [(0,1),(1,0),(0,-1),(-1,0)]

def move(pos, action):
    x,y = pos
    dx,dy = action
    nx,ny = max(0,min(SIZE-1,x+dx)), max(0,min(SIZE-1,y+dy))
    return (nx,ny)

Q = np.zeros((SIZE,SIZE,4))
alpha = 0.1
gamma = 0.9
epsilon = 0.2

def choose_action(state):
    if random.random()<epsilon:
        return random.randint(0,3)
    return np.argmax(Q[state[0],state[1]])

def train(reward_type):
    global epsilon
    epsilon = 1.0   # start curious

    for episode in range(500):
        state = (0,0)

        for step in range(100):
            action = choose_action(state)
            new_state = move(state,ACTIONS[action])

            reward = reward_function(new_state, reward_type)

            Q[state[0],state[1],action] += alpha * (
                reward + gamma*np.max(Q[new_state[0],new_state[1]])
                - Q[state[0],state[1],action]
            )

            state = new_state
            if state == GOAL:
                break

        # gradually become greedy
        epsilon = max(0.05, epsilon*0.995)



def reward_function(state, reward_type):

    if reward_type=="goal_only":
        return 10 if state==GOAL else 0

    if reward_type=="step_penalty":
        return 10 if state==GOAL else -0.1

    if reward_type=="harsh_penalty":
        return 10 if state==GOAL else -1

    if reward_type=="wrong_reward":
        return -10 if state==GOAL else 0


def run_episode():
    state = (0,0)
    path=[state]

    for _ in range(30):
        action = np.argmax(Q[state[0],state[1]])
        state = move(state,ACTIONS[action])
        path.append(state)
        if state==GOAL:
            break

    return path



for r in ["goal_only","step_penalty","harsh_penalty","wrong_reward"]:
    Q[:] = 0
    train(r)

    print("\n====",r,"====")

    path = run_episode()
    print("Path taken:", path)

    print("Policy map:")
    for i in range(SIZE):
        row=[]
        for j in range(SIZE):
            row.append(np.argmax(Q[i,j]))
        print(row)

