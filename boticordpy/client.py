import typing

from . import types as boticord_types
from .http import HttpClient
from .autopost import AutoPost


class BoticordClient:
    __slots__ = (
        "http",
        "_autopost",
        "_token"
    )

    http: HttpClient

    def __init__(self, token=None, **kwargs):
        self._token = token
        self._autopost: typing.Optional[AutoPost] = None
        self.http = HttpClient(token)

    async def get_bot_info(self, bot_id: int) -> boticord_types.Bot:
        response = await self.http.get_bot_info(bot_id)
        return boticord_types.Bot(**response)

    async def get_bot_comments(self, bot_id: int) -> list:
        response = await self.http.get_bot_comments(bot_id)
        return [boticord_types.SingleComment(**comment) for comment in response]

    async def post_bot_stats(self, servers: int = 0, shards: int = 0, users: int = 0) -> dict:
        response = await self.http.post_bot_stats({
            "servers": servers,
            "shards": shards,
            "users": users
        })
        return response

    async def get_server_info(self, server_id: int) -> boticord_types.Server:
        response = await self.http.get_server_info(server_id)
        return boticord_types.Server(**response)

    async def get_server_comments(self, server_id: int) -> list:
        response = await self.http.get_server_comments(server_id)
        return [boticord_types.SingleComment(**comment) for comment in response]

    async def post_server_stats(self, payload: dict) -> dict:
        response = await self.post_server_stats(payload)
        return response

    async def get_user_info(self, user_id: int) -> boticord_types.UserProfile:
        response = await self.get_user_info(user_id)
        return boticord_types.UserProfile(**response)

    async def get_user_comments(self, user_id: int) -> boticord_types.UserComments:
        response = await self.get_user_comments(user_id)
        return boticord_types.UserComments(**response)

    async def get_user_bots(self, user_id: int) -> list:
        response = await self.get_user_bots(user_id)
        return [boticord_types.SimpleBot(**bot) for bot in response]

    def autopost(self) -> AutoPost:
        if self._autopost is not None:
            return self._autopost

        self._autopost = AutoPost(self)
        return self._autopost
