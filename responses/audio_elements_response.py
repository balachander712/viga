from typing import Optional

from pydantic import BaseModel

from enums.response_code_enum import ResponseCodeEnum
from http import HTTPStatus

from models.audio_element import AudioElementModel


class AddAudioElementResponse(BaseModel):
    time: float
    operation_id: str
    response_code: ResponseCodeEnum
    status_code: HTTPStatus
    response_string: str
    data: Optional[AudioElementModel]
