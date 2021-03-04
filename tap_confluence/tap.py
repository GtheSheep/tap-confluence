from typing import List

from singer_sdk.tap_base import Tap
from singer_sdk.helpers.typing import (
    ArrayType,
    PropertiesList,
    StringType,
)

from tap_confluence.streams import (
    ContentStream,
    GroupsStream,
    SpacesStream,
    ThemesStream,
)

PLUGIN_NAME = "tap-confluence"

STREAM_TYPES = [
    GroupsStream,
    ContentStream,
    SpacesStream,
    ThemesStream,
]


class TapConfluence(Tap):
    """confluence tap class."""

    name = "tap-confluence"
    config_jsonschema = PropertiesList(
        StringType("base_url", required=True),
        StringType("email", required=True),
        StringType("api_token", required=True),
        StringType("user_agent"),
        ArrayType(StringType, "resources", required=True),
    ).to_dict()

    def discover_streams(self) -> List:
        """Return a list of discovered streams."""
        return [
            stream(tap=self)
            for stream in STREAM_TYPES
            if stream.name in self.config["resources"]
        ]


cli = TapConfluence.cli
