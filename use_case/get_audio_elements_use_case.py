import uuid
from http import HTTPStatus

from enums.response_code_enum import ResponseCodeEnum
from responses.audio_elements_response import GetAudioElementsResponse, GetAudioElementResponse
from use_case.audio_element import AudioElement
import time


def get_audio_elements_use_case():
    loader = AudioElement()
    audio_elements = loader.load_audio_elements()
    if audio_elements:
        return GetAudioElementsResponse(
            time=time.time(),
            operation_id=str(uuid.uuid4()),
            status_code=HTTPStatus.OK,
            response_string=ResponseCodeEnum.elements_present,
            data=audio_elements
        )
    else:
        return GetAudioElementsResponse(
            time=time.time(),
            operation_id=str(uuid.uuid4()),
            status_code=HTTPStatus.NO_CONTENT,
            response_string=ResponseCodeEnum.elements_empty
        )


def get_audio_element_use_case(audio_element_id: str):
    loader = AudioElement()
    audio_elements = loader.load_audio_elements()
    for audio_element in audio_elements:
        if audio_element["id"] == audio_element_id:
            return GetAudioElementResponse(
                time=time.time(),
                operation_id=str(uuid.uuid4()),
                status_code=HTTPStatus.OK,
                response_string=ResponseCodeEnum.elements_present,
                data=audio_element
            )

    return GetAudioElementResponse(
        time=time.time(),
        operation_id=str(uuid.uuid4()),
        status_code=HTTPStatus.NOT_FOUND,
        response_string=ResponseCodeEnum.elements_empty,
    )

