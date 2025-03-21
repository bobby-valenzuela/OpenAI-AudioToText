# OpenAI-AudioToText

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/).

2. Clone this repository.

3. Navigate into the project directory:

   ```bash
   cd OpenAI-DALL-E-ImageGenerator
   ```

4. Create a new virtual environment:

   ```bash
   python3 -m venv env && . env/bin/activate
   ```

5. Install the requirements:

   ```bash
   pip3 install -r requirements.txt
   ```

6. Create a .env file with your OpenAI api key
   ```bash
   echo "OPENAI_API_KEY={api_secret}" > .env 
   ```
7. Install [pyaudio](https://pypi.org/project/PyAudio/#:~:text=INSTALLATION)


<br />


## Usage

<br />

```bash
python3 audiototext.py
```

<br />

## Running Whisper Locally

[Import whisper](https://analyzingalpha.com/openai-whisper-python-tutorial)
```sh
pip install -U openai-whisper
```

<br>

Import whisper + Load model (using base here)
```sh
import whisper
model = whisper.load_model("base")
```

<br>

Transcribe
```sh
result = model.transcribe("mysample.wav")
result["text"]
```
