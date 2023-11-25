from typing import Protocol, Generator, Callable

from stream_converter.conversion_function import whisper_conversion


class AudioStream(Protocol):
    def read(self) -> bytes:
        ...


def stream_object_converter(input_stream: AudioStream) -> Generator[str, None, None]:
    while True:
        audio_chunk = input_stream.read()
        yield whisper_conversion(audio_chunk)


def bytes_converter() -> Generator[str, bytes, None]:
    audio_chunk = yield "START"
    while True:
        audio_chunk = yield str(audio_chunk)


def stream_function_converter(input_function: Callable) -> Generator[str, None, None]:
    while True:
        audio_chunk = input_function()
        yield whisper_conversion(audio_chunk)
