import pyaudio

from stream_converter.converter import stream_object_converter, ByteStream


class MicrophoneStream(ByteStream):
    def __init__(self):
        self.audio = pyaudio.PyAudio()
        self.frames_per_buffer = 1024
        self.microphone_stream = self.audio.open(
            format=pyaudio.paFloat32,                  # audio format (e.g., paFloat32 for float32)
            channels=1,                                # number of audio channels
            rate=44100,                                # bit rate (samples per second)
            frames_per_buffer=self.frames_per_buffer,  # number of frames per buffer
            input=True,
        )

    def read(self) -> bytes:
        """
        This is the only method that needs to be implemented.
        """
        return self.microphone_stream.read(self.frames_per_buffer, exception_on_overflow=False)

    def close(self):
        self.microphone_stream.stop_stream()
        self.microphone_stream.close()
        self.audio.terminate()


if __name__ == "__main__":
    microphone_stream = MicrophoneStream()
    try:
        converted_stream = stream_object_converter(
            input_stream=microphone_stream,
            conversion_function=lambda byte: str(byte),
        )
        for converted_chunk in converted_stream:
            print(converted_chunk)
    except KeyboardInterrupt:
        pass
    microphone_stream.close()
