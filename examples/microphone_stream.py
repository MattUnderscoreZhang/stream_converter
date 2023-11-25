from stream_converter.converter import convert_generator_stream, convert_function_stream
from stream_converter.microphone_stream import get_microphone_stream_generator, MicrophoneStream


def microphone_stream_generator():
    try:
        converted_stream = convert_generator_stream(
            stream_generator=get_microphone_stream_generator(),
            conversion_function=lambda byte: str(byte),
        )
        for converted_chunk in converted_stream:
            print(converted_chunk)
    except KeyboardInterrupt:
        pass


def microphone_stream_function():
    try:
        with MicrophoneStream() as microphone_stream:
            converted_stream = convert_function_stream(
                stream_function=microphone_stream.read,
                conversion_function=lambda byte: str(byte),
            )
            for converted_chunk in converted_stream:
                print(converted_chunk)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    # microphone_stream_generator()
    microphone_stream_function()
