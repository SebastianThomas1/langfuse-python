# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1


class PatchMediaBody(pydantic_v1.BaseModel):
    uploaded_at: dt.datetime = pydantic_v1.Field(alias="uploadedAt")
    """
    The date and time when the media record was uploaded
    """

    upload_http_status: int = pydantic_v1.Field(alias="uploadHttpStatus")
    """
    The HTTP status code of the upload
    """

    upload_http_error: typing.Optional[str] = pydantic_v1.Field(
        alias="uploadHttpError", default=None
    )
    """
    The HTTP error message of the upload
    """

    upload_time_ms: typing.Optional[int] = pydantic_v1.Field(
        alias="uploadTimeMs", default=None
    )
    """
    The time in milliseconds it took to upload the media record
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        kwargs_with_defaults_exclude_none: typing.Any = {
            "by_alias": True,
            "exclude_none": True,
            **kwargs,
        }

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset),
            super().dict(**kwargs_with_defaults_exclude_none),
        )

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}