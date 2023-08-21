import openai
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

# Record Some audio
import wave
import sys
import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1 if sys.platform == "darwin" else 2
RATE = 44100


def record_audio(seconds: int):
    output_path = "output.wav"
    with wave.open(output_path, "wb") as wf:
        p = pyaudio.PyAudio()
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)

        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)

        print("Recording...")
        for index in range(0, RATE // CHUNK * seconds):
            if index % (RATE // CHUNK) == 0:
                print(f"{index // (RATE // CHUNK)} / {seconds}s")
            wf.writeframes(stream.read(CHUNK))
        print("Done")

        stream.close()
        p.terminate()
    print(f"File saved at {output_path}")
    return output_path

print(f"running... {__name__}")

if __name__ == "__main__":

    prompt = input("What is your audio about? ")
    duration_s = int(input("Duration (secs):  "))

    record_audio(duration_s)

    # Read audio
    audio_file = open("output.wav", "rb")

    # Transcribe: Prompt isn't required, but improves transcribed text
    response = openai.Audio.transcribe(
        model="whisper-1",
        file=audio_file,
        prompt=prompt
    )

    text = response["text"]

    print(f"R: {text}")