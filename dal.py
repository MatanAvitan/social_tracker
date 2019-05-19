from models import UserToTrack, UserActivity
from consts import USERS_TO_TRACK_COLLECTION, LAST_USERS_ACTIVITY_COLLECTION
from datetime import datetime

def get_all_users_to_track():
    all_user_list = []
    for user in UserToTrack.objects:
        all_user_list.append(user['username'])
    return all_user_list


def save_user_activity(username, text, timestamp):
    user = UserActivity(username=username, text=text, timestamp=datetime.fromtimestamp(timestamp))
    user.save()
