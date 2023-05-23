import time
import uuid
from http import HTTPStatus

from enums.response_code_enum import ResponseCodeEnum
from models.audio_element import AudioElementModel
from responses.audio_elements_response import AddAudioElementResponse
from use_case.audio_element import AudioElement


def add_audio_element_use_case(audio_element: AudioElementModel):
    # Check if an audio element with the same ID already exists
    loader = AudioElement()
    audio_elements = loader.load_audio_elements()
    for existing_element in audio_elements:
        if existing_element["id"] == audio_element.id:
            data = "Failed to create Audio element. Audio element already exists"
            return AddAudioElementResponse(
                time=time.time(),
                operation_id=str(uuid.uuid4()),
                status_code=HTTPStatus.CONFLICT,
                response_code=ResponseCodeEnum.error,
                response_string=data
            )

    # Check if the audio element overlaps with any existing audio elements of the same type
    for existing_element in audio_elements:
        if (
                existing_element["type"] == audio_element.type
                and existing_element.get("duration")
                and audio_element.duration
                and (
                (audio_element.duration["start_time"] <= existing_element["duration"]["start_time"] <
                 audio_element.duration["end_time"])
                or (audio_element.duration["start_time"] < existing_element["duration"]["end_time"] <=
                    audio_element.duration["end_time"])
                or (existing_element["duration"]["start_time"] <= audio_element.duration["start_time"]
                    and existing_element["duration"]["end_time"] >= audio_element.duration["end_time"])
        )
        ):
            # Adjust the start and end times to avoid overlap
            audio_element.duration["start_time"] = existing_element["duration"]["end_time"]
            audio_element.duration["end_time"] = audio_element.duration["start_time"] + (
                        existing_element["duration"]["end_time"] - existing_element["duration"]["start_time"])

    audio_elements.append(audio_element.dict())
    loader.save_audio_elements(audio_elements)
    msg = "Added audio element successfully"
    return AddAudioElementResponse(
        time=time.time(),
        operation_id=str(uuid.uuid4()),
        status_code=HTTPStatus.CREATED,
        response_code=ResponseCodeEnum.success,
        response_string=msg,
        data=audio_element
    )
