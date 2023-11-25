import pyaudio

from stream_converter.converter import stream_function_converter


if __name__ == "__main__":
    audio = pyaudio.PyAudio()
    frames_per_buffer = 1024
    microphone_stream = audio.open(
        format=pyaudio.paFloat32,             # audio format (e.g., paFloat32 for float32)
        channels=1,                           # number of audio channels
        rate=44100,                           # bit rate (samples per second)
        frames_per_buffer=frames_per_buffer,  # number of frames per buffer
        input=True,
    )
    read_from_microphone = lambda: microphone_stream.read(frames_per_buffer, exception_on_overflow=False)

    try:
        converted_stream = stream_function_converter(
            input_function=read_from_microphone,
            conversion_function=lambda byte: str(byte),
        )
        for converted_chunk in converted_stream:
            print(converted_chunk)
    except KeyboardInterrupt:
        pass

    microphone_stream.stop_stream()
    microphone_stream.close()
    audio.terminate()
