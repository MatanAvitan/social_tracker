import sched
import time
from datetime import datetime, timedelta

import mongoengine

import settings
from dal import get_all_users_to_track, save_user_activity
from instagram_api_adapter import InstagramAdapter
from instagram_managers.instagram_activity_manager import ActivityManager

mongoengine.connect(
    db=settings.DATABASE_NAME,
    host=settings.DATABASE_HOST,
    port=settings.DATABASE_PORT,
)

TIME_TO_SLEEP = 10 * 60


class TrackerCollector(object):
    def __init__(self):
        self._i_adapter = None

    def start_collect(self):
        try:
            all_users_to_track = get_all_users_to_track()
            if not self._i_adapter:
                self._i_adapter = InstagramAdapter(settings.USERNAME, settings.PASSWORD)
                self._i_adapter.connect()
            i_a_manager = ActivityManager()
            for user_to_track in all_users_to_track:
                last_user_activity_list = i_a_manager.get_last_activity_of_user(self._i_adapter, user_to_track)
                if last_user_activity_list:
                    for activity in last_user_activity_list:
                        save_user_activity(user_to_track, activity['text'], activity['timestamp'])
            print(f'going to sleep at: {datetime.now() + timedelta(hours=3)}')
        except Exception as e:
            print(e)
        finally:
            s.enter(TIME_TO_SLEEP, 1, self.start_collect)


tc = TrackerCollector()
s = sched.scheduler(time.time, time.sleep)
s.enter(TIME_TO_SLEEP, 1, tc.start_collect)
s.run()
