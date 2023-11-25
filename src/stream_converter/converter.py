from typing import Protocol, Generator, Callable


class ByteStream(Protocol):
    def read(self) -> bytes:
        ...


def stream_object_converter(
    input_stream: ByteStream,
    conversion_function: Callable,
) -> Generator[str, None, None]:
    while True:
        audio_chunk = input_stream.read()
        yield conversion_function(audio_chunk)


def stream_function_converter(
    input_function: Callable,
    conversion_function: Callable,
) -> Generator[str, None, None]:
    while True:
        audio_chunk = input_function()
        yield conversion_function(audio_chunk)
