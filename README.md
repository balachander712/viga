# Project Name

REST API for Interacting with Audio Elements using FastAPI.

## API Documentation

The following endpoints are available in the API:

### Add Audio Element

- Endpoint: `POST /audio_elements`
- Description: Add an audio element.
- Request Body:
  - `audio_element`: The audio element to be added.
    - `id` (string): The ID of the audio element.
    - `type` (string): Type of the element.
    - `high_volume` (int): High Volume.
    - `low_volume` (int): Low Volume.
    - `video_component_id` (str): Video Component Id.
    - `url` (str): URL.
    - `duration` (dict): Duration Dictionary
    - `start_time` (str): Start Time
    - `end` (str): End Time
- Response:
  - `status_code` (int): The HTTP status code.
  - `message` (string): The response message.
- Example cURL for the request:
```
  curl --location 'http://localhost:8000/audio_elements' \
    --header 'Content-Type: application/json' \
    --data '{
      "id": "11221",
      "type": "vo",
      "high_volume": 80,
      "low_volume": 50,
      "video_component_id": null,
      "url": "https://example.com/audio.mp3",
      "duration": {
        "start_time": 0,
        "end_time": 10
      }
    }'
  ```
### Get All Audio Elements

- Endpoint: `GET /audio_elements`
- Description: Get all audio elements.
- Response:
  - `status_code` (int): The HTTP status code.
  - `message` (string): The response message.
- Example cURL for the request:
```
curl --location 'http://localhost:8000/audio_elements'
  ```

### Get Audio Element

- Endpoint: `GET /audio_element`
- Description: Get an audio element by ID.
- Query Parameters:
  - `audio_element_id` (string): The ID of the audio element.
- Response:
  - `status_code` (int): The HTTP status code.
  - `message` (string): The response message.
- Example cURL for the request:
```
curl --location 'http://localhost:8000/audio_element/?audio_element_id=112'
```

### Update Audio Element

- Endpoint: `PUT /audio_elements`
- Description: Update an audio element.
- Request Body:
  - `audio_element_id` (string): The ID of the audio element to update.
  - `update_fields` (dict): The fields to update for the audio element.
- Response:
  - `status_code` (int): The HTTP status code.
  - `message` (string): The response message.
- Example cURL for the request:
```
curl --location --request PUT 'http://localhost:8000/audio_elements?audio_element_id=11' \
--header 'Content-Type: application/json' \
--data '{
"high_volume": 0.8,
"low_volume": 0.1
}'
```

### Delete Audio Element

- Endpoint: `DELETE /audio_elements`
- Description: Delete an audio element by ID.
- Query Parameters:
  - `audio_element_id` (string): The ID of the audio element to delete.
- Response:
  - `status_code` (int): The HTTP status code.
  - `message` (string): The response message.
```
curl --location --request PUT 'http://localhost:8000/audio_elements?audio_element_id=11' \
--header 'Content-Type: application/json' \
--data '{
"high_volume": 0.8,
"low_volume": 0.1
}'
```

## Usage

1. Clone the Repository
2. Navigate into the Repository
3. Run `main.py` file
4. Test the endpoints using cURL or Postman
