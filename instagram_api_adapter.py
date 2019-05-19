from InstagramAPI import InstagramAPI

from errors import FailedToConnectAccount, FailedToGetRecentActivity


class InstagramAdapter(object):
    def __init__(self, username, password):
        self._username = username
        self._password = password
        self._conn = None

    def connect(self):
        if not self._conn:
            self._conn = InstagramAPI(self._username, self._password)
            self._conn.login()
        if not self._conn:
            raise FailedToConnectAccount(self._username, self._password)

    def get_following_recent_activity(self):
        try:
            self._conn.getFollowingRecentActivity()
            return self._conn.LastJson
        except:
            raise FailedToGetRecentActivity
