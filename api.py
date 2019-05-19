import mongoengine
import settings
from flask import Flask
# from flask_restful_swagger_2 import Api
from flask_restplus import Api
from components.UserToTrack.resource import UserToTrack

mongoengine.connect(
    db=settings.DATABASE_NAME,
    host=settings.DATABASE_HOST,
    port=settings.DATABASE_PORT,
)
app = Flask(__name__)

api = Api(app, api_verlsion='0.0', title="SocialTracker", api_spec_url='/docs')
api.add_resource(UserToTrack, '/UserToTrack/<user_to_track>/StartTracking')
if __name__ == '__main__':
    app.run(debug=True)
