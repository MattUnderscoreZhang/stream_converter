import pyaudio

from streaming_whisper.converter import bytes_converter


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

    converter = bytes_converter()
    next(converter)  # get "START" from generator
    # for _ in range(1000):  # about 23 seconds
    for _ in range(40):  # about 1 second
        try:
            audio_chunk = microphone_stream.read(frames_per_buffer)
            converted_chunk = converter.send(audio_chunk)
            print(converted_chunk)
        except KeyboardInterrupt:
            break

    microphone_stream.stop_stream()
    microphone_stream.close()
    audio.terminate()
