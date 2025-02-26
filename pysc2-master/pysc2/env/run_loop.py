# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""A run loop for agent/environment interaction."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import time
from collections import deque
import numpy as np
import random

MINIBATCH = 50
REPLAY = 1
DISCOUNT = 0.9


def state_processing(obs):
  input_data = []
  for key, value in obs.observation.items():
    if key != 'map_name':
      tmp = list(obs.observation[key].flatten())
      while len(tmp) < 100:
        tmp.append(0)
      input_data.extend(tmp)
  return input_data


# 미니배치를 이용한 학습
def replay_train(DQN, replay_memory, replay):
  for next_state, action, reward, done, state in random.sample(replay_memory, replay):
    next_state = np.array(next_state).reshape(1, len(next_state))
    state = np.array(state).reshape(1, len(state))
    Q = DQN.predict(state)

    # DQN 알고리즘으로 학습
    Q[0, action] = reward + DISCOUNT * np.max(DQN.predict(next_state))
    print("액션 :", action, "Q값 :", Q[0, action])

    DQN.update(np.reshape(state, [1, DQN.input_size]), Q)


def run_loop(agents, env, max_frames=0, max_episodes=0):
  """A run loop to have agents and an environment interact."""
  total_frames = 0
  total_episodes = 0
  start_time = time.time()

  observation_spec = env.observation_spec()
  action_spec = env.action_spec()
  # print()
  # print("observation_space :", observation_spec)
  # print()
  # print("action_space :", action_spec)
  for agent, obs_spec, act_spec in zip(agents, observation_spec, action_spec):
    # print("act spaces :",act_spec, type(act_spec))
    agent.setup(obs_spec, act_spec)

  # 핵심 변수
  # env : pysc2가 제공하는 스타크래프트 게임 환경 객체
  # agents : 강화학습을 위한 에이전트
  # timesteps : env.step() 메소드의 리턴값.
  #             env 을 agents 전달하기 좋은 형태로 만든 것으로 보인다.

  # 0. env 리셋
  #    agents 리셋
  # loop
  #   1. timesteps(processed env) -> agents에 전달 => action 결정
  #   2. action -> env에 반영 => timesteps 생성. :: 환경 변화

  # 결론 : timesteps에서 적합한 action 을 찾아내는게 현재 해야할 일.(현재 이게 완전히 랜덤)

  try:
    replay_buffer = deque(maxlen=10000)
    while not max_episodes or total_episodes < max_episodes:
      total_episodes += 1
      state = env.reset()   # 0. 초기 환경
      for a in agents:          # 0. agent 초기화
        a.reset()
      while True:
        actions = [agent.step(timestep, epsilon=0.1)
                   for agent, timestep in zip(agents, state)]
        function_id = actions[0][1]
        args = actions[0][2]
        actions = [actions[0][0]]

        next_state = env.step(actions)
        reward = next_state[0][1]
        done = next_state[0].last()

        replay_buffer.append((state_processing(next_state[0]), function_id, reward, done, state_processing(state[0])))

        # 10 번의 스탭마다 미니배치로 학습
        if total_frames % 10 == 1:
          for _ in range(MINIBATCH):
            replay_train(agents[0].function_network, replay_buffer, REPLAY)

        state = next_state
        total_frames += 1

        if max_frames and total_frames >= max_frames:
          return
        if next_state[0].last():
          break




  except KeyboardInterrupt:
    pass
  finally:
    elapsed_time = time.time() - start_time
    print("Took %.3f seconds for %s steps: %.3f fps" % (
        elapsed_time, total_frames, total_frames / elapsed_time))

# python -m pysc2.bin.agent --map CollectMineralShards --agent pysc2.agents.scripted_agent.CollectMineralShards