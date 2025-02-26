input = []

flatten_action_result = list(obs.observation['action_result'].flatten())
input.append(flatten_action_result)
flatten_alerts = list(obs.observation['alerts'].flatten())
input.append(flatten_alerts)
flatten_build_queue = list(obs.observation['build_queue'].flatten())
input.append(flatten_build_queue)
flatten_cargo = list(obs.observation['cargo'].flatten())
input.append(flatten_cargo)
flatten_cargo_slots_available = list(obs.observation['cargo_slots_available'].flatten())
input.append(flatten_cargo_slots_available)
flatten_control_groups = list(obs.observation['control_groups'].flatten())
input.append(flatten_control_groups)
flatten_game_loop = list(obs.observation['game_loop'].flatten())
input.append(flatten_game_loop)
flatten_last_actions = list(obs.observation['last_actions'].flatten())
input.append(flatten_last_actions)
flatten_map_name = list(obs.observation['map_name'])
input.append(flatten_map_name)
flatten_multi_select = list(obs.observation['multi_select'].flatten())
input.append(flatten_multi_select)
flatten_player = list(obs.observation['player'].flatten())
input.append(flatten_player)
flatten_production_queue = list(obs.observation['production_queue'].flatten())
input.append(flatten_production_queue)
flatten_score_cumulative = list(obs.observation['score_cumulative'].flatten())
input.append(flatten_score_cumulative)
flatten_score_by_category = list(obs.observation['score_by_category'].flatten())
input.append(flatten_score_by_category)
flatten_score_by_vital = list(obs.observation['score_by_vital'].flatten())
input.append(flatten_score_by_vital)
flatten_single_select = list(obs.observation['single_select'].flatten())
input.append(flatten_single_select)
flatten_available_actions = list(obs.observation['available_actions'].flatten())
input.append(flatten_available_actions)
flatten_feature_screen = list(obs.observation['feature_screen'].flatten())
input.append(flatten_feature_screen)
flatten_feature_minimap = list(obs.observation['feature_minimap'].flatten())
input.append(flatten_feature_minimap)
flatten_upgrades = list(obs.observation['upgrades'].flatten())
input.append(flatten_upgrades)
flatten_home_race_requested = list(obs.observation['home_race_requested'].flatten())
input.append(flatten_home_race_requested)
flatten_away_race_requested = list(obs.observation['away_race_requested'].flatten())
input.append(flatten_away_race_requested)

# print(len(flatten_action_result))
print(len(flatten_build_queue), flatten_build_queue)
print(len(flatten_cargo), flatten_cargo)
print("flatten screen ", len(flatten_feature_screen), type(flatten_feature_screen),
      numpy.array(flatten_feature_screen).shape)
