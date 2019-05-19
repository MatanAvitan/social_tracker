import settings

from instagram_managers.instagram_base_manager import BaseManager
from instagram_api_adapter import InstagramAdapter
import copy


class ActivityManager(BaseManager):
    def __init__(self):
        pass

    def get_last_activity_of_user(self, i_adapter, username_to_track):
        user_activity_list = []
        single_user_activity = {}
        acount_recent_activity = i_adapter.get_following_recent_activity()
        acount_recent_activity_list = acount_recent_activity['stories']
        for activity in acount_recent_activity_list:
            single_user_activity['text'] = activity['args']['text']
            single_user_activity['timestamp'] = activity['args']['timestamp']
            if username_to_track in single_user_activity['text']:
                user_activity_list.append(copy.deepcopy(single_user_activity))
        return user_activity_list
