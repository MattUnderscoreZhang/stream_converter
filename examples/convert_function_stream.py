from random import randint

from stream_converter.converter import convert_function_stream


def get_random_number() -> int:
    return randint(0, 100)


if __name__ == "__main__":
    try:
        converted_stream = convert_function_stream(
            stream_function=get_random_number,
            conversion_function=lambda byte: str(byte),
        )
        for converted_chunk in converted_stream:
            print(converted_chunk)
    except KeyboardInterrupt:
        pass
