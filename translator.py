import time
import joblib
import streamlit as st
import pandas as pd
import mediapipe as mp
import numpy as np
import cv2

# Setup MediaPipe and load the model
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
word = ""
sentence = ""
last_sentence = ""
last_word_time = time.time()

# Load the pre-trained Random Forest model
RFC = joblib.load("/hand_gesture_model.sav")

# Streamlit layout
st.title("Penerjemah Bahasa Isyarat")
st.subheader("Silahkan peragakan Bahasa Isyarat didepan Kamera")
st.write("Gunakan Bahasa isyarat BISINDO")
frame_placeholder = st.empty()
text_previous_sentence = st.empty()
text_current_sentence = st.empty()
text_word = st.empty()

# Capture video
cap = cv2.VideoCapture(0)
with mp_holistic.Holistic(min_detection_confidence=0.3, min_tracking_confidence=0.3) as holistic:
    while cap.isOpened():
        curr_word_time = time.time()

        # Read camera input
        ret, frame = cap.read()
        if not ret:
            st.error("Tidak dapat membaca input kamera.")
            break

        # Convert BGR to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Flip horizontally for a mirror effect
        image = cv2.flip(image, 1)

        # Mark the image as not writeable to pass by reference
        image.flags.writeable = False

        # Process the image and find hand landmarks
        results = holistic.process(image)

        # Mark the image as writeable for drawing
        image.flags.writeable = True

        # Draw hand landmarks
        if results.left_hand_landmarks:
            mp_drawing.draw_landmarks(
                image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        if results.right_hand_landmarks:
            mp_drawing.draw_landmarks(
                image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

        # Check if it has been at least 2 seconds
        if curr_word_time - last_word_time >= 2.0:
            if results.right_hand_landmarks or results.left_hand_landmarks:
                # Get landmark coordinates
                lh = list(np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten()
                          if results.left_hand_landmarks else np.zeros(21 * 3))
                rh = list(np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten()
                          if results.right_hand_landmarks else np.zeros(21 * 3))

                # Combine the landmarks into a single row
                row = lh + rh

                # Predict the gesture
                try:
                    X = pd.DataFrame([row])
                    hand_class = RFC.predict(X)[0]
                    word = word + hand_class
                    text_word.write(f"Kata Saat Ini: {word}")
                    last_word_time = curr_word_time
                except Exception as e:
                    st.error(f"Kesalahan Prediksi: {e}")
            else:
                if word:
                    sentence = sentence + " " + word
                    text_current_sentence.write(
                        f"Kalimat Saat Ini: {sentence.strip()}")
                    word = ""
                    text_word.write(f"Kata Saat Ini: {word}")
                    last_word_time = curr_word_time
                else:
                    last_sentence = sentence.strip()
                    text_previous_sentence.write(
                        f"Kalimat Sebelumnya: {last_sentence}")
                    sentence = ""
                    text_current_sentence.write(
                        f"Kalimat Saat Ini: {sentence}")
                    last_word_time = curr_word_time

        # Display the processed image in the Streamlit app
        frame_placeholder.image(image, channels="RGB")

    cap.release()
    cv2.destroyAllWindows()
    st.write("---")
