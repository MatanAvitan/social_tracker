import settings
from instagram_managers.instagram_activity_manager import ActivityManager
from models import UserToTrack
from consts import USERS_TO_TRACK_COLLECTION


def start_tracking_username(username):
    user = UserToTrack(username=username)
    user.switch_collection(USERS_TO_TRACK_COLLECTION)
    user.insert()
