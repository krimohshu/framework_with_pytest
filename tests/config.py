class Config:
    def __init__(self, env):
        SUPPORTIVE_ENVS = ['dev', 'qa']

        if env.lower() not in SUPPORTIVE_ENVS:
            raise Exception(f'{env} is not a supportive environment (supportive env are: {SUPPORTIVE_ENVS})')
        self.base_url = {
            'dev': 'https://mydev-env.com',
            'qa': 'https://myqa-env.com'
        }[env]

        self.app_port = {
            'dev': 8080,
            'qa': 80
        }[env]