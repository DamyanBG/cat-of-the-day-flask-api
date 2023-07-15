from decouple import config
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_apscheduler import APScheduler

from db import db
from resources.routes import routes
from jobs.won_job import won
from jobs.jobs import jobs

class DevApplicationConfiguration:
    DEBUG = True
    TESTING = True
    SCHEDULER_API_ENABLED = True
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}"
        f"@{config('DB_HOST')}/{config('DB_NAME')}"
    )


# class TestApplicationConfiguration:
#     DEBUG = True
#     TESTING = True
#     SQLALCHEMY_DATABASE_URI = (
#         f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}"
#         f"@localhost:{config('DB_PORT')}/{config('TEST_DB_NAME')}"
#     )


def create_app(config="config.DevApplicationConfiguration"):
    app = Flask(__name__)
    app.config.from_object(DevApplicationConfiguration)
    migrate = Migrate(app, db)
    CORS(app)
    api = Api(app)
    [api.add_resource(*r) for r in routes]
    scheduler = APScheduler()
    scheduler.add_job(func=won(app), trigger="cron", hour="23", id="won-cat-of-the-day")
    # [scheduler.add_job(*j) for j in jobs]
    scheduler.init_app(app)
    scheduler.start()
    return app
