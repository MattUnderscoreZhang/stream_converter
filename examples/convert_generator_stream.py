from random import randint
from typing import Generator

from stream_converter.converter import convert_generator_stream


def get_random_number_generator() -> Generator[int, None, None]:
    while True:
        yield randint(0, 100)


if __name__ == "__main__":
    try:
        converted_stream = convert_generator_stream(
            stream_generator=get_random_number_generator(),
            conversion_function=lambda int: "odd" if int % 2 else "even"
        )
        for converted_chunk in converted_stream:
            print(converted_chunk)
    except KeyboardInterrupt:
        pass
