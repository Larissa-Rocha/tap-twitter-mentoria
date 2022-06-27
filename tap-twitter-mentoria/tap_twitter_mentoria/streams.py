"""Stream type classes for tap-twitter-mentoria."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_twitter_mentoria.client import TwitterStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


class TweetsStream(TwitterStream):
    """Define custom stream."""
    name = "tweets"
    path = "/tweets"
    primary_keys = ["id"]
    replication_key = None
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"
    schema = th.PropertiesList(
        th.Property(
            "id",
            th.StringType,
            description="The tweet ID"
        ),
        th.Property(
            "text",
            th.StringType,
            description="The tweet text"
        ),
    ).to_dict()
