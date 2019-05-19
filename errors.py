class FailedToConnectAccount(Exception):
    def __init__(self, username, password):
        super().__init__(f'Cannot connect to {username} with password {password}')


class FailedToGetRecentActivity(Exception):
    def __init__(self):
        super().__init__(f'Failed to get recent activity')

class ErrorParametersNotGiven(Exception):
    def __init__(self):
        super().__init__(f'Not all of the parameters were supplied')
