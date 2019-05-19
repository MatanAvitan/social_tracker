from flask_restful import Resource, fields

from components.UserToTrack.controller import start_tracking_username
from errors import ErrorParametersNotGiven


class UserToTrack(Resource):
    def __init__(self, request):
        pass

    def post(self, user_to_track):
        try:
            start_tracking_username(user_to_track)
            return {"result": f"{user_to_track}"}, 200
        except Exception as e:
            return {"error": f"{ErrorParametersNotGiven()}"}, 400
