from stream_converter.converter import stream_object_converter
from stream_converter.microphone_stream import MicrophoneStream


if __name__ == "__main__":
    try:
        with MicrophoneStream() as microphone_stream:
            converted_stream = stream_object_converter(
                input_stream=microphone_stream,
                conversion_function=lambda byte: str(byte),
            )
            for converted_chunk in converted_stream:
                print(converted_chunk)
    except KeyboardInterrupt:
        pass
