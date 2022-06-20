"""MySourceName Authentication."""


from singer_sdk.authenticators import OAuthAuthenticator, SingletonMeta


# The SingletonMeta metaclass makes your streams reuse the same authenticator instance.
# If this behaviour interferes with your use-case, you can remove the metaclass.
class MySourceNameAuthenticator(OAuthAuthenticator, metaclass=SingletonMeta):
    """Authenticator class for MySourceName."""

    @property
    def oauth_request_body(self) -> dict:
        """Define the OAuth request body for the MySourceName API."""
        # TODO: Define the request body needed for the API.
        return {
            'resource': 'https://analysis.windows.net/powerbi/api',
            'scope': self.oauth_scopes,
            'client_id': self.config["client_id"],
            'username': self.config["username"],
            'password': self.config["password"],
            'grant_type': 'password',
        }

    @classmethod
    def create_for_stream(cls, stream) -> "MySourceNameAuthenticator":
        return cls(
            stream=stream,
            auth_endpoint="TODO: OAuth Endpoint URL",
            oauth_scopes="TODO: OAuth Scopes",
        )
