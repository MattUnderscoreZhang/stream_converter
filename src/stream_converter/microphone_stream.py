import pyaudio
from typing import Optional


class StreamWrapper:
    def __init__(self, stream: pyaudio.Stream, frames_per_buffer: int):
        self.stream = stream
        self.frames_per_buffer = frames_per_buffer

    def read(self) -> bytes:
        return self.stream.read(self.frames_per_buffer, exception_on_overflow=False)


class MicrophoneStream:
    def __init__(
        self,
        format: int = pyaudio.paFloat32,
        channels: int = 1,
        rate: int = 44100,
        frames_per_buffer: int = 1024,
    ) -> None:
        self.format: int = format
        self.channels: int = channels
        self.rate: int = rate
        self.frames_per_buffer: int = frames_per_buffer
        self.audio: Optional[pyaudio.PyAudio] = None
        self.stream: Optional[pyaudio.Stream] = None

    def __enter__(self) -> StreamWrapper:
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(
            format=self.format,                        # audio format (e.g., paFloat32 for float32)
            channels=self.channels,                    # number of audio channels
            rate=self.rate,                            # bit rate (samples per second)
            frames_per_buffer=self.frames_per_buffer,  # number of frames per buffer
            input=True,
        )
        return StreamWrapper(self.stream, self.frames_per_buffer)

    def __exit__(
        self,
        exc_type: Optional[type],
        exc_val: Optional[Exception],
        exc_tb: Optional[object],
    ) -> None:
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        if self.audio:
            self.audio.terminate()
