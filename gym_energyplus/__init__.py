from gym.envs.registration import register

register(
    id='energyplus-v0',
    entry_point='gym_energyplus.envs:EnergyplusEnv',
)
register(
    id='energyplus-extrahard-v0',
    entry_point='gym_energyplus.envs:EnergyplusExtraHardEnv',
)
