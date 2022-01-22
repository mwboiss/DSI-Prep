def observation_adder(dict_of_obs,seen):
    if seen in dict_of_obs:
        dict_of_obs[seen] +=1
    else:
        dict_of_obs[seen] = 1
    return dict_of_obs