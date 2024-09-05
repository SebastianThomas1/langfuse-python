# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.datetime_utils import serialize_datetime
from ...core.jsonable_encoder import jsonable_encoder
from ...core.pydantic_utilities import pydantic_v1
from ...core.request_options import RequestOptions
from ..commons.errors.access_denied_error import AccessDeniedError
from ..commons.errors.error import Error
from ..commons.errors.method_not_allowed_error import MethodNotAllowedError
from ..commons.errors.not_found_error import NotFoundError
from ..commons.errors.unauthorized_error import UnauthorizedError
from ..commons.types.observations_view import ObservationsView
from .types.observations_views import ObservationsViews


class ObservationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(self, observation_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ObservationsView:
        """
        Get a observation

        Parameters
        ----------
        observation_id : str
            The unique langfuse identifier of an observation, can be an event, span or generation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObservationsView

        Examples
        --------
        from finto.client import FernLangfuse

        client = FernLangfuse(
            x_langfuse_sdk_name="YOUR_X_LANGFUSE_SDK_NAME",
            x_langfuse_sdk_version="YOUR_X_LANGFUSE_SDK_VERSION",
            x_langfuse_public_key="YOUR_X_LANGFUSE_PUBLIC_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.observations.get(
            observation_id="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/public/observations/{jsonable_encoder(observation_id)}", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ObservationsView, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise Error(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 403:
                raise AccessDeniedError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowedError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_many(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        trace_id: typing.Optional[str] = None,
        parent_observation_id: typing.Optional[str] = None,
        from_start_time: typing.Optional[dt.datetime] = None,
        to_start_time: typing.Optional[dt.datetime] = None,
        version: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ObservationsViews:
        """
        Get a list of observations

        Parameters
        ----------
        page : typing.Optional[int]
            Page number, starts at 1.

        limit : typing.Optional[int]
            Limit of items per page. If you encounter api issues due to too large page sizes, try to reduce the limit.

        name : typing.Optional[str]

        user_id : typing.Optional[str]

        type : typing.Optional[str]

        trace_id : typing.Optional[str]

        parent_observation_id : typing.Optional[str]

        from_start_time : typing.Optional[dt.datetime]
            Retrieve only observations with a start_time or or after this datetime (ISO 8601).

        to_start_time : typing.Optional[dt.datetime]
            Retrieve only observations with a start_time before this datetime (ISO 8601).

        version : typing.Optional[str]
            Optional filter to only include observations with a certain version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObservationsViews

        Examples
        --------
        import datetime

        from finto.client import FernLangfuse

        client = FernLangfuse(
            x_langfuse_sdk_name="YOUR_X_LANGFUSE_SDK_NAME",
            x_langfuse_sdk_version="YOUR_X_LANGFUSE_SDK_VERSION",
            x_langfuse_public_key="YOUR_X_LANGFUSE_PUBLIC_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.observations.get_many(
            page=1,
            limit=1,
            name="string",
            user_id="string",
            type="string",
            trace_id="string",
            parent_observation_id="string",
            from_start_time=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            to_start_time=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            version="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/public/observations",
            method="GET",
            params={
                "page": page,
                "limit": limit,
                "name": name,
                "userId": user_id,
                "type": type,
                "traceId": trace_id,
                "parentObservationId": parent_observation_id,
                "fromStartTime": serialize_datetime(from_start_time) if from_start_time is not None else None,
                "toStartTime": serialize_datetime(to_start_time) if to_start_time is not None else None,
                "version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ObservationsViews, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise Error(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 403:
                raise AccessDeniedError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowedError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncObservationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self, observation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ObservationsView:
        """
        Get a observation

        Parameters
        ----------
        observation_id : str
            The unique langfuse identifier of an observation, can be an event, span or generation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObservationsView

        Examples
        --------
        import asyncio

        from finto.client import AsyncFernLangfuse

        client = AsyncFernLangfuse(
            x_langfuse_sdk_name="YOUR_X_LANGFUSE_SDK_NAME",
            x_langfuse_sdk_version="YOUR_X_LANGFUSE_SDK_VERSION",
            x_langfuse_public_key="YOUR_X_LANGFUSE_PUBLIC_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.observations.get(
                observation_id="string",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/public/observations/{jsonable_encoder(observation_id)}", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ObservationsView, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise Error(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 403:
                raise AccessDeniedError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowedError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_many(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        trace_id: typing.Optional[str] = None,
        parent_observation_id: typing.Optional[str] = None,
        from_start_time: typing.Optional[dt.datetime] = None,
        to_start_time: typing.Optional[dt.datetime] = None,
        version: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ObservationsViews:
        """
        Get a list of observations

        Parameters
        ----------
        page : typing.Optional[int]
            Page number, starts at 1.

        limit : typing.Optional[int]
            Limit of items per page. If you encounter api issues due to too large page sizes, try to reduce the limit.

        name : typing.Optional[str]

        user_id : typing.Optional[str]

        type : typing.Optional[str]

        trace_id : typing.Optional[str]

        parent_observation_id : typing.Optional[str]

        from_start_time : typing.Optional[dt.datetime]
            Retrieve only observations with a start_time or or after this datetime (ISO 8601).

        to_start_time : typing.Optional[dt.datetime]
            Retrieve only observations with a start_time before this datetime (ISO 8601).

        version : typing.Optional[str]
            Optional filter to only include observations with a certain version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObservationsViews

        Examples
        --------
        import asyncio
        import datetime

        from finto.client import AsyncFernLangfuse

        client = AsyncFernLangfuse(
            x_langfuse_sdk_name="YOUR_X_LANGFUSE_SDK_NAME",
            x_langfuse_sdk_version="YOUR_X_LANGFUSE_SDK_VERSION",
            x_langfuse_public_key="YOUR_X_LANGFUSE_PUBLIC_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.observations.get_many(
                page=1,
                limit=1,
                name="string",
                user_id="string",
                type="string",
                trace_id="string",
                parent_observation_id="string",
                from_start_time=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                to_start_time=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                version="string",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/public/observations",
            method="GET",
            params={
                "page": page,
                "limit": limit,
                "name": name,
                "userId": user_id,
                "type": type,
                "traceId": trace_id,
                "parentObservationId": parent_observation_id,
                "fromStartTime": serialize_datetime(from_start_time) if from_start_time is not None else None,
                "toStartTime": serialize_datetime(to_start_time) if to_start_time is not None else None,
                "version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ObservationsViews, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise Error(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 403:
                raise AccessDeniedError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowedError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
