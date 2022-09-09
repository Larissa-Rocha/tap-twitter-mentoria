"""Tests standard tap features using the built-in SDK tests library."""

from os import environ as env
from dotenv import load_dotenv
load_dotenv()

import datetime

from singer_sdk.testing import get_standard_tap_tests

from tap_twitter_mentoria.tap import TapMySourceName

SAMPLE_CONFIG = {
    "start_date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"),
    "bearer_token": env["BEARER_TOKEN"],
    "user_agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "api_url": "https://api.twitter.com/2"
}


# Run standard built-in tap tests from the SDK:
def test_standard_tap_tests():
    """Run standard tap tests from the SDK."""
    tests = get_standard_tap_tests(
        TapMySourceName,
        config=SAMPLE_CONFIG
    )
    for test in tests:
        test()


# TODO: Create additional tests as appropriate for your tap.
