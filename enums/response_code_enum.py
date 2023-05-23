from enum import Enum


class ResponseCodeEnum(Enum):
    success = "Audio element created successfully"
    error = "Failed to create audio element"
    elements_present = "Element(s) Present"
    elements_empty = "No audio element(s) present"
    update_success = "Audio Element Updated Successfully"
    updated_failed = "Cannot update video component ID for video_music element"
    delete_success = "Audio Element Deleted Successfully"
    delete_failed = "Cannot delete the original video component"
