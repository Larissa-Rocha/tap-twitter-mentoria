"""Twitter Authentication."""


from singer_sdk.authenticators import OAuthAuthenticator, SingletonMeta, APIAuthenticatorBase
from singer_sdk.streams import Stream as RESTStreamBase


# The SingletonMeta metaclass makes your streams reuse the same authenticator instance.
# If this behaviour interferes with your use-case, you can remove the metaclass.
#class TwitterAuthenticator(OAuthAuthenticator, metaclass=SingletonMeta):
#    """Authenticator class for MySourceName."""
#
#    @property
#    def oauth_request_body(self) -> dict:
#        """Define the OAuth request body for the MySourceName API."""
#        # TODO: Define the request body needed for the API.
#        return {
#            'resource': 'https://analysis.windows.net/powerbi/api',
#            'scope': self.oauth_scopes,
#            'client_id': self.config["client_id"],
#            'username': self.config["username"],
#            'password': self.config["password"],
#            'grant_type': 'password',
#        }
#
#    @classmethod
#    def create_for_stream(cls, stream) -> "TwitterAuthenticator":
#        return cls(
#            stream=stream,
#            auth_endpoint="TODO: OAuth Endpoint URL",
#            oauth_scopes="TODO: OAuth Scopes",
#        )

class BearerTokenAuthenticator(APIAuthenticatorBase):
    """Implements bearer token authentication for REST Streams.
    This Authenticator implements Bearer Token authentication. The token
    is a text string, included in the request header and prefixed with
    'Bearer '. The token will be merged with HTTP headers on the stream.
    """

    def __init__(self, stream: RESTStreamBase, token: str) -> None:
        """Create a new authenticator.
        Args:
            stream: The stream instance to use with this authenticator.
            token: Authentication token.
        """
        super().__init__(stream=stream)
        auth_credentials = {"Authorization": f"Bearer {token}"}

        if self._auth_headers is None:
            self._auth_headers = {}
        self._auth_headers.update(auth_credentials)

    @classmethod
    def create_for_stream(
        cls: type[BearerTokenAuthenticator], stream: RESTStreamBase, token: str
    ) -> BearerTokenAuthenticator:
        """Create an Authenticator object specific to the Stream class.
        Args:
            stream: The stream instance to use with this authenticator.
            token: Authentication token.
        Returns:
            BearerTokenAuthenticator: A new
                :class:`singer_sdk.authenticators.BearerTokenAuthenticator` instance.
        """
        return cls(stream=stream, token=token)