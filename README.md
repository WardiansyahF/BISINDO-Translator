# Sign Language Translator

The Sign Language Translator is a real-time application that translates sign language gestures captured through the webcam into text. It utilizes computer vision and machine learning techniques to detect and interpret hand movements, enabling users to communicate using sign language. The application provides a user-friendly interface built with Streamlit, allowing users to see the translated text as they sign. It aims to bridge communication barriers and make sign language more accessible to a wider audience.

![Demo](demo.gif)

## Key Features

- Real-time translation of sign language gestures into text.
- Utilizes MediaPipe for hand gesture detection and tracking.
- Machine learning model for predicting gestures and translating them into text.
- Streamlit interface for easy interaction and visualization.
- Supports multiple sign languages and gestures.

## Dependencies

- OpenCV (cv2)
- MediaPipe
- Pandas
- scikit-learn (version 1.4.2)
- Streamlit

## Usage

1. Install the required dependencies using `pip install -r requirements.txt`.
2. Clone the repository: `https://github.com/WardiansyahF/BISINDO-Translator.git`.
3. Navigate to the project directory: `cd BISINDO-Translator`.
4. Run the Streamlit app: `streamlit run translator.py`.
5. Follow the on-screen instructions to start translating sign language gestures into text.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.
