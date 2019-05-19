from datetime import datetime, timedelta

import mongoengine
from consts import USERS_TO_TRACK_COLLECTION, LAST_USERS_ACTIVITY_COLLECTION


class UserActivity(mongoengine.Document):
    username = mongoengine.StringField()
    text = mongoengine.StringField()
    timestamp = datetime.now() + timedelta(hours=3)
    meta = {'collection': LAST_USERS_ACTIVITY_COLLECTION}


class UserToTrack(mongoengine.Document):
    username = mongoengine.StringField()
    meta = {'collection': USERS_TO_TRACK_COLLECTION}
