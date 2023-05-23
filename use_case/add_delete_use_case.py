import time
import uuid
from http import HTTPStatus

from enums.response_code_enum import ResponseCodeEnum
from models.audio_element import AudioElementModel
from responses.audio_elements_response import AddAudioElementResponse, GetAudioElementResponse, \
    DeleteAudioElementsUseCase, UpdateAudioElementResponse
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


def update_audio_element_use_case(audio_element_id: str, update_fields: dict):
    loader = AudioElement()
    audio_elements = loader.load_audio_elements()
    # Find the audio element with the specified ID
    for audio_element in audio_elements:
        if audio_element["id"] == audio_element_id:
            # Exclude updating the video_component_id for video_music elements
            if audio_element["type"] != "video_music" or "video_component_id" not in update_fields:
                # Update the specified fields of the audio element
                for field, value in update_fields.items():
                    audio_element[field] = value

                # Save the updated audio elements
                loader.save_audio_elements(audio_elements)

                # Return the updated audio element
                return UpdateAudioElementResponse(
                    time=time.time(),
                    operation_id=str(uuid.uuid4()),
                    status_code=HTTPStatus.OK,
                    response_string=ResponseCodeEnum.update_success,
                    data=audio_element
                )

            # If the audio element is of type video_music and video_component_id is present in update_fields,
            # raise an exception
            return UpdateAudioElementResponse(
                time=time.time(),
                operation_id=str(uuid.uuid4()),
                status_code=HTTPStatus.BAD_REQUEST,
                response_string=ResponseCodeEnum.updated_failed,
                data=audio_element
            )
    # If the audio element is not found, raise an exception
    return GetAudioElementResponse(
        time=time.time(),
        operation_id=str(uuid.uuid4()),
        status_code=HTTPStatus.NOT_FOUND,
        response_string=ResponseCodeEnum.elements_empty,
    )


def delete_audio_element_use_case(audio_element_id: str):
    loader = AudioElement()
    audio_elements = loader.load_audio_elements()
    for audio_element in audio_elements:
        if audio_element["id"] == audio_element_id:
            if audio_element["type"] == "video_audio":
                # Handle the case of video_audio
                return DeleteAudioElementsUseCase(
                    time=time.time(),
                    operation_id=str(uuid.uuid4()),
                    status_code=HTTPStatus.FORBIDDEN,
                    response_string=ResponseCodeEnum.delete_failed,
                )
            else:
                audio_elements.remove(audio_element)
                loader.save_audio_elements(audio_elements)
                return DeleteAudioElementsUseCase(
                    time=time.time(),
                    operation_id=str(uuid.uuid4()),
                    status_code=HTTPStatus.OK,
                    response_string=ResponseCodeEnum.delete_success,
                )

    # Audio element with the specified ID not found
    return DeleteAudioElementsUseCase(
        time=time.time(),
        operation_id=str(uuid.uuid4()),
        status_code=HTTPStatus.NOT_FOUND,
        response_string=ResponseCodeEnum.elements_empty,
    )
