import logging
import os
import sys

sys.path.append(
    os.path.join(os.path.dirname(__file__), '..')
)

os.environ["CLAIM_ENV"] = "development"

from support.http_test_client import HTTPTestClient
from claim import claim
# pick one for test configuration, if they don't match things will fail
from claim.config import development as config


handler = logging.FileHandler('log/behave.log')
handler.setFormatter(logging.Formatter(
    "%(asctime)s [%(levelname)s - %(name)s - %(filename)s:%(lineno)d] "
    "-> %(message)s"))


log = logging.getLogger()
log.addHandler(handler)


def before_feature(context, feature):
    context.client = create_client(feature)


def before_scenario(context, _):
    context.client.before_scenario()
    storage = context.client.storage()
    storage.connection.drop_database(storage.name)


def after_scenario(context, scenario):
    context.client.after_scenario(scenario)


def after_feature(context, _):
    context.client.spin_down()


def create_client(feature):
    if 'use_http_client' in feature.tags:
        return HTTPTestClient(config.DATABASE_NAME)
    raise AssertionError(
        "Test client not selected! Please annotate the failing feature with "
        + "@use_http_client.")
