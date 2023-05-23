from typing import Optional, List

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

class GetAudioElementsResponse(BaseModel):
    time: float
    operation_id: str
    status_code: HTTPStatus
    response_string: Optional[ResponseCodeEnum]
    data: Optional[List[AudioElementModel]]

class GetAudioElementResponse(BaseModel):
    time: float
    operation_id: str
    status_code: HTTPStatus
    response_string: Optional[ResponseCodeEnum]
    data: Optional[AudioElementModel]

class UpdateAudioElementResponse(BaseModel):
    time: float
    operation_id: str
    status_code: HTTPStatus
    response_string: Optional[ResponseCodeEnum]
    data: Optional[AudioElementModel]

class DeleteAudioElementsUseCase(BaseModel):
    time: float
    operation_id: str
    status_code: HTTPStatus
    response_string: Optional[ResponseCodeEnum]
    data: Optional[AudioElementModel]
