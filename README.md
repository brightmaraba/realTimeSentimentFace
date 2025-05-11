# Sentiment Analysis

![Python](https://img.shields.io/badge/python-3.13-blue.svg)
![GitHub License](https://img.shields.io/github/license/trflorian/sentiment-analysis-viz)


https://github.com/user-attachments/assets/df8c3c87-ce11-492d-b5ce-f3786d68e0e1


Visualising sentiment using a procedural smiley face in Python with OpenCV and Tkinter. The sentiment is calculated using a pre-trained model from Hugging Face. The specific model used is `cardiffnlp/twitter-roberta-base-sentiment`(<https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment>). This model outputs three classes: `negative`, `neutral`, `positive` and a score between -1 and 1 for each class based on the confidence of the model. Negative scores are displayed as a sad face and positive scores as a happy face.

## Requirements

    customtkinter>=5.2.2
    numpy>=2.2.2
    opencv-python>=4.11.0.86
    pillow>=11.1.0
    torch>=2.5.1
    transformers>=4.48.1
    pytest>=8.3.5
    ruff>=0.11.8

## Installation

    ```bash
    pip install -r requirements.txt
    ```

You may need to setup a virtual environment first. Use uv, poetry, pipenv or VirtaulEnv to do so.

## Usage

    ```bash
    python src/app.py
    ```
