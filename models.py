from datetime import datetime

import mongoengine

from consts import USERS_TO_TRACK_COLLECTION, LAST_USERS_ACTIVITY_COLLECTION


class UserActivity(mongoengine.Document):
    username = mongoengine.StringField()
    text = mongoengine.StringField()
    timestamp = mongoengine.DateField(default=datetime .now)
    meta = {'collection': LAST_USERS_ACTIVITY_COLLECTION}

    def insert(self):
        if len(UserActivity.objects(username=self.username, text=self.text)) == 0:
            self.save()


class UserToTrack(mongoengine.Document):
    username = mongoengine.StringField()
    meta = {'collection': USERS_TO_TRACK_COLLECTION}

    def insert(self):
        if len(UserToTrack.objects(username=self.username)) == 0:
            self.save()
