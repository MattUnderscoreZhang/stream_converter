from streaming_whisper.converter import stream_function_converter
from streaming_whisper.microphone_stream import MicrophoneStream


if __name__ == "__main__":
    with MicrophoneStream() as microphone_stream:
        converted_chunk_generator = stream_function_converter(microphone_stream.read)
        for _ in range(40):  # about 1 second
            converted_chunk = next(converted_chunk_generator)
            print(converted_chunk)
